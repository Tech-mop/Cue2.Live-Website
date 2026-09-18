(function () {
  var KEY = "cue2-lang";
  var SUPPORTED = ["en", "mi", "es", "de", "ru", "ja", "ar", "hi"];
  var DEFAULT = "en";

  function isBot() {
    return /bot|crawl|spider|slurp|bingpreview|facebookexternalhit|embedly/i.test(
      navigator.userAgent || ""
    );
  }

  function currentLang() {
    var parts = (location.pathname || "/").split("/").filter(Boolean);
    if (parts.length && SUPPORTED.indexOf(parts[0]) !== -1 && parts[0] !== DEFAULT) {
      return parts[0];
    }
    return DEFAULT;
  }

  function restPath() {
    var parts = (location.pathname || "/").split("/").filter(Boolean);
    if (parts.length && SUPPORTED.indexOf(parts[0]) !== -1 && parts[0] !== DEFAULT) {
      parts = parts.slice(1);
    }
    return parts.length ? "/" + parts.join("/") + (location.pathname.slice(-1) === "/" ? "/" : "") : "/";
  }

  function pathFor(lang) {
    var rest = restPath();
    if (lang === DEFAULT) {
      return rest + location.search + location.hash;
    }
    if (rest === "/") {
      return "/" + lang + "/" + location.search + location.hash;
    }
    return "/" + lang + rest + location.search + location.hash;
  }

  function matchBrowser() {
    var langs = navigator.languages && navigator.languages.length
      ? navigator.languages
      : [navigator.language || navigator.userLanguage || DEFAULT];
    for (var i = 0; i < langs.length; i++) {
      var code = String(langs[i] || "").toLowerCase().replace("_", "-");
      var short = code.split("-")[0];
      if (SUPPORTED.indexOf(short) !== -1) return short;
    }
    return DEFAULT;
  }

  var select = document.getElementById("lang-switch");
  if (select) {
    select.addEventListener("change", function () {
      var lang = select.value;
      try {
        localStorage.setItem(KEY, lang);
      } catch (e) {}
      var href = pathFor(lang);
      if (href !== location.pathname + location.search + location.hash) {
        location.assign(href);
      }
    });
  }

  if (isBot()) return;

  var current = currentLang();
  var stored = null;
  try {
    stored = localStorage.getItem(KEY);
  } catch (e) {}

  if (stored) {
    if (SUPPORTED.indexOf(stored) !== -1 && stored !== current) {
      location.replace(pathFor(stored));
    }
    return;
  }

  if (current !== DEFAULT) {
    try {
      localStorage.setItem(KEY, current);
    } catch (e) {}
    return;
  }

  var pref = matchBrowser();
  try {
    localStorage.setItem(KEY, pref);
  } catch (e) {}
  if (pref !== DEFAULT && pref !== current) {
    location.replace(pathFor(pref));
  }
})();
