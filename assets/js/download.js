(function () {
  var PLATFORMS = [
    "windows-x86_64",
    "windows-arm64",
    "macos-arm64",
    "linux-x86_64",
    "linux-arm64"
  ];

  function detectPlatform() {
    var ua = navigator.userAgent || "";
    var platform = navigator.platform || "";
    var uaData = navigator.userAgentData;
    var os = "windows";
    var arch = "x86_64";

    if (/Android|iPhone|iPad|iPod/i.test(ua)) {
      return "windows-x86_64";
    }

    if (uaData && uaData.platform) {
      var p = uaData.platform.toLowerCase();
      if (p.indexOf("mac") !== -1) os = "macos";
      else if (p.indexOf("win") !== -1) os = "windows";
      else if (p.indexOf("linux") !== -1 || p.indexOf("cros") !== -1) os = "linux";
    } else if (/Mac OS X|Macintosh/i.test(ua) || /Mac/i.test(platform)) {
      os = "macos";
    } else if (/Win/i.test(ua) || /Win/i.test(platform)) {
      os = "windows";
    } else if (/Linux|X11/i.test(ua) || /Linux/i.test(platform)) {
      os = "linux";
    }

    if (os === "macos") {
      return "macos-arm64";
    }

    if (/arm64|aarch64/i.test(ua) || /arm64/i.test(platform)) {
      arch = "arm64";
    }

    var id = os + "-" + arch;
    if (PLATFORMS.indexOf(id) !== -1) return id;

    for (var i = 0; i < PLATFORMS.length; i++) {
      if (PLATFORMS[i].indexOf(os + "-") === 0) return PLATFORMS[i];
    }
    return "windows-x86_64";
  }

  function applyHighEntropyArch(os, callback) {
    var uaData = navigator.userAgentData;
    if (!uaData || typeof uaData.getHighEntropyValues !== "function" || os === "macos") {
      callback();
      return;
    }

    uaData
      .getHighEntropyValues(["architecture", "bitness"])
      .then(function (hints) {
        var architecture = (hints.architecture || "").toLowerCase();
        if (!architecture) {
          callback();
          return;
        }
        var arch = architecture === "arm" || architecture === "arm64" ? "arm64" : "x86_64";
        var id = os + "-" + arch;
        if (PLATFORMS.indexOf(id) !== -1) {
          selectPlatform(id);
        }
        callback();
      })
      .catch(function () {
        callback();
      });
  }

  function selectPlatform(id) {
    var primary = document.getElementById("download-primary");
    var others = document.getElementById("download-others");
    if (!primary || !others) return;

    var links = others.querySelectorAll("[data-platform]");
    var match = null;
    for (var i = 0; i < links.length; i++) {
      if (links[i].getAttribute("data-platform") === id) {
        match = links[i];
        break;
      }
    }
    if (!match) return;

    primary.href = match.href;
    primary.setAttribute("data-platform", id);
    primary.querySelector(".download-label").textContent = match.getAttribute("data-label");
    primary.querySelector(".download-meta").textContent = match.getAttribute("data-meta");
    setHidden(links, id);
  }

  function setHidden(links, selectedId) {
    for (var i = 0; i < links.length; i++) {
      var item = links[i].closest("li");
      if (item) item.hidden = links[i].getAttribute("data-platform") === selectedId;
    }
  }

  var ASSET_SUFFIX = {
    "windows-x86_64": /-windows-x86_64\.zip$/i,
    "windows-arm64": /-windows-arm64\.zip$/i,
    "macos-arm64": /-macos-arm64\.zip$/i,
    "linux-x86_64": /-linux-x86_64\.tar\.gz$/i,
    "linux-arm64": /-linux-arm64\.tar\.gz$/i
  };
  var RELEASE_PREFIX = "https://github.com/Tech-mop/Cue2/releases/download/";

  function assetUrl(assets, id) {
    var pattern = ASSET_SUFFIX[id];
    if (!pattern) return null;
    for (var i = 0; i < assets.length; i++) {
      var asset = assets[i];
      if (!asset || !pattern.test(asset.name || "")) continue;
      var url = asset.browser_download_url || "";
      if (url.indexOf(RELEASE_PREFIX) === 0) return url;
    }
    return null;
  }

  // Baked-in links are the release resolved at build time. This moves every
  // button onto the current latest release without waiting for a site rebuild.
  function applyLatestRelease(release) {
    if (!release || !release.tag_name || !release.assets) return;
    var tag = String(release.tag_name);
    var links = document.querySelectorAll("#download-others [data-platform]");
    for (var i = 0; i < links.length; i++) {
      var link = links[i];
      var url = assetUrl(release.assets, link.getAttribute("data-platform"));
      if (!url) continue;
      link.href = url;
      var detail = link.getAttribute("data-detail");
      if (detail) link.setAttribute("data-meta", tag + " · " + detail);
    }
    var primary = document.getElementById("download-primary");
    var current = primary && primary.getAttribute("data-platform");
    selectPlatform(current || detectPlatform());
  }

  function refreshLatest() {
    var root = document.getElementById("download");
    if (!root || !window.fetch) return;
    var api = root.getAttribute("data-release-api");
    if (!api) return;
    window.fetch(api, { headers: { Accept: "application/vnd.github+json" } })
      .then(function (res) {
        if (!res.ok) throw new Error(String(res.status));
        return res.json();
      })
      .then(applyLatestRelease)
      .catch(function () {});
  }

  var detected = detectPlatform();
  selectPlatform(detected);

  var os = detected.split("-")[0];
  applyHighEntropyArch(os, function () {});
  refreshLatest();
})();
