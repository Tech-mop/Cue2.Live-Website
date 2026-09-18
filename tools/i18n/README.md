# Website translations

Same locales as the Cue2 app: English, Māori, Spanish, German, Russian, Japanese, Arabic, Hindi.

English is the source of truth. Other languages live beside it and are filled by `update_catalog.py` — the same idea as `python tools/i18n/update_catalog.py` in the Cue2 app.

## Files

| Path | Role |
|------|------|
| `_data/i18n/en.yml` | English copy. Edit this when website wording changes. |
| `_data/i18n/<lang>.yml` | Other locales. Hand-tweak here; the updater keeps them while English is unchanged. |
| `tools/i18n/catalog.py` | Authored tables used to fill gaps (and by `--from-catalog`). |
| `index.md`, `about.md`, includes | Structure only. They use `{% t home.hero_h1 %}` keys, not raw English. |

Do not put user-facing sentences in the Markdown if they need translating. Add a key under `_data/i18n/en.yml` and `{% t that.key %}` in the template.

## Everyday English update

1. Change the string in `_data/i18n/en.yml` (or add a new nested key).
2. From the website repo root:

   ```bash
   python3 tools/i18n/update_catalog.py
   ```

3. Check the printed **stale** / **still English placeholders** list.
4. Either edit the listed keys in `_data/i18n/<lang>.yml` by hand, or machine-fill:

   ```bash
   pip install deep-translator
   python3 tools/i18n/update_catalog.py --machine
   ```

5. Restart `bundle exec jekyll serve` and glance at `/es/`, `/de/`, `/ar/`, etc.

`--machine` and a normal run **never overwrite** a translation whose English hash still matches. They only fill missing keys, or stale keys when English for that key changed.

Leave product names and protocols in English: Cue2, FFmpeg, SDL3, OSC, MIDI, GO, GitHub, MIT, Windows, macOS, Linux, StripyHat.

Te reo Māori should get a native review.

## New UI string

1. Add the English value in `_data/i18n/en.yml`.
2. Use it in the template: `{% t nav.download %}`.
3. Run `python3 tools/i18n/update_catalog.py` (and `--machine` if you want auto-fill).

## Rebuild from authored tables

Overwrites every locale file from `catalog.py`. Use only if you meant to throw away YAML hand edits:

```bash
python3 tools/i18n/update_catalog.py --from-catalog
```

If you keep authored tables in sync, update `STRINGS` in `catalog.py` as well as `en.yml`.

## Adding a language

1. Add the code to `LOCALES` / `LOCALE_META` in `catalog.py`.
2. Add it to `languages`, `locale_names`, and `locale_og` in `_config.yml`.
3. Add it to `SUPPORTED` in `assets/js/i18n.js`.
4. Put `ar` (only) in `rtl_languages` if it is right-to-left.
5. Run `python3 tools/i18n/update_catalog.py --from-catalog` or `--machine`.
