# Social preview card

`assets/img/og-card.png` (1200×630) is the image shown when a cue2.live link is
shared on X, Slack, Discord, etc. It is rendered from `og-card.html`, which uses
the site logo and the app screenshot from `assets/img/`.

To regenerate after changing the logo, screenshot or wording, run this from the
repo root (Chrome or Chromium; on macOS use the full path to the Chrome app binary):

```bash
google-chrome --headless=new --hide-scrollbars --allow-file-access-from-files \
  --window-size=1200,630 --virtual-time-budget=5000 \
  --screenshot="$PWD/assets/img/og-card.png" \
  "file://$PWD/tools/og-card/og-card.html"
```

The card is English only; the tagline matches `home.hero_h1` and the badge
matches `home.hero_badge` in `_data/i18n/en.yml`.
Optional: shrink the PNG (for example with `pngquant`) before committing.
