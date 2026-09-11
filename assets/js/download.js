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

    var currentId = primary.getAttribute("data-platform");
    if (currentId === id) {
      setHidden(links, id);
      return;
    }

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

  var detected = detectPlatform();
  selectPlatform(detected);

  var os = detected.split("-")[0];
  applyHighEntropyArch(os, function () {});
})();
