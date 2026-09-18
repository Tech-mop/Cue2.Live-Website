#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025-2026 Samuel Moxham
# SPDX-License-Identifier: MIT
"""Refresh website locale YAML — same idea as Cue2 tools/i18n/update_catalog.py.

English source of truth: _data/i18n/en.yml  (or catalog.py on first run / --from-catalog)

  python tools/i18n/update_catalog.py
      Merge keys into every locale file. Keep existing translations while the
      English text for that key is unchanged. Fill gaps from catalog.py.

  python tools/i18n/update_catalog.py --from-catalog
      Rewrite every _data/i18n/<lang>.yml from catalog.py (overwrites locale files).

  python tools/i18n/update_catalog.py --machine
      Machine-translate missing or stale keys (pip install deep-translator).
      Never overwrites a translation whose English hash still matches.

After English copy changes: edit _data/i18n/en.yml, then run this script.
Restart `bundle exec jekyll serve` to see the site.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
I18N = ROOT / "_data" / "i18n"
HASH_PATH = HERE / "en_hash.json"

sys.path.insert(0, str(HERE))
from catalog import LOCALES, LOCALE_META, STRINGS, is_leaf, tree_for, walk  # noqa: E402

IDENTITY = (
    "Cue2",
    "FFmpeg",
    "SDL3",
    "OSC",
    "MIDI",
    "GO",
    "GitHub",
    "MIT",
    "Windows",
    "macOS",
    "Linux",
    "StripyHat",
    "RtMidi",
    "LGPLv2.1",
    "docs.cue2.live",
)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def flatten(node: dict, prefix: str = "") -> dict[str, str]:
    out: dict[str, str] = {}
    for key, value in node.items():
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and value and not any(isinstance(v, dict) for v in value.values()):
            # Could be a leaf of strings already (locale tree) — treat as nested if values are dict
            pass
        if isinstance(value, dict):
            out.update(flatten(value, path))
        else:
            out[path] = "" if value is None else str(value)
    return out


def nest(flat: dict[str, str]) -> dict:
    root: dict = {}
    for path, value in flat.items():
        cur = root
        parts = path.split(".")
        for part in parts[:-1]:
            cur = cur.setdefault(part, {})
        cur[parts[-1]] = value
    return root


def emit_yaml(node: dict, indent: int = 0) -> str:
    lines: list[str] = []
    pad = "  " * indent
    for key, value in node.items():
        if isinstance(value, dict):
            lines.append(f"{pad}{key}:")
            lines.append(emit_yaml(value, indent + 1).rstrip("\n"))
        else:
            dumped = json.dumps(value, ensure_ascii=False)
            lines.append(f"{pad}{key}: {dumped}")
    return "\n".join(lines) + "\n"


def load_yaml_flat(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        import yaml  # type: ignore
    except ImportError:
        yaml = None
    text = path.read_text(encoding="utf-8")
    if yaml is not None:
        data = yaml.safe_load(text) or {}
        return flatten(data)
    # Minimal fallback: json-quoted YAML we ourselves write
    data: dict = {}
    stack: list[tuple[int, dict]] = [(-1, data)]
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if stripped.endswith(":") and not stripped.startswith('"'):
            key = stripped[:-1]
            parent[key] = {}
            stack.append((indent, parent[key]))
        else:
            key, _, val = stripped.partition(":")
            parent[key.strip()] = json.loads(val.strip())
    return flatten(data)


def authored_flat(lang: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for path, leaf in walk(STRINGS):
        if not is_leaf(leaf):
            continue
        out[path] = leaf.get(lang) or leaf["en"]
    return out


def protect(text: str) -> tuple[str, list[str]]:
    held: list[str] = []

    def stash(chunk: str) -> str:
        held.append(chunk)
        return f"⟦{len(held) - 1}⟧"

    import re

    text = re.sub(r"<[^>]+>", lambda m: stash(m.group(0)), text)
    for name in sorted(IDENTITY, key=len, reverse=True):
        text = text.replace(name, stash(name))
    return text, held


def restore(text: str, held: list[str]) -> str:
    for i, chunk in enumerate(held):
        text = text.replace(f"⟦{i}⟧", chunk)
        text = text.replace(f"[[{i}]]", chunk)
    return text


def machine_translate(text: str, dest: str) -> str:
    from deep_translator import GoogleTranslator  # type: ignore

    google = LOCALE_META[dest]["google"]
    if dest == "en" or not text.strip():
        return text
    masked, held = protect(text)
    translated = GoogleTranslator(source="en", target=google).translate(masked)
    return restore(translated or text, held)


def write_locale(lang: str, flat: dict[str, str]) -> None:
    I18N.mkdir(parents=True, exist_ok=True)
    header = (
        f"# Generated by tools/i18n/update_catalog.py — {lang} ({LOCALE_META[lang]['name']})\n"
        f"# Edit English in _data/i18n/en.yml then re-run the script. Hand-tweak other locales;\n"
        f"# existing translations are kept while English for that key is unchanged.\n"
    )
    (I18N / f"{lang}.yml").write_text(header + emit_yaml(nest(flat)), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--from-catalog", action="store_true", help="Rewrite all locale YAML from catalog.py")
    parser.add_argument("--machine", action="store_true", help="Translate missing/stale keys with deep-translator")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.from_catalog or not (I18N / "en.yml").exists():
        en_flat = authored_flat("en")
    else:
        en_flat = load_yaml_flat(I18N / "en.yml")
        if not en_flat:
            en_flat = authored_flat("en")

    old_hashes: dict[str, str] = {}
    if HASH_PATH.exists():
        old_hashes = json.loads(HASH_PATH.read_text(encoding="utf-8"))
    new_hashes = {k: sha(v) for k, v in en_flat.items()}

    stale: list[str] = []
    missing_report: list[str] = []

    for lang in LOCALES:
        if lang == "en":
            merged = dict(en_flat)
            source = "en.yml"
        else:
            existing = {} if args.from_catalog else load_yaml_flat(I18N / f"{lang}.yml")
            authored = authored_flat(lang)
            merged = {}
            for key, english in en_flat.items():
                prev = existing.get(key, "")
                hash_ok = old_hashes.get(key) == new_hashes.get(key)
                already = bool(prev) and prev != english
                if already and hash_ok and not args.from_catalog:
                    merged[key] = prev
                    continue
                if args.from_catalog and authored.get(key):
                    merged[key] = authored[key]
                    continue
                if (not prev or prev == english or not hash_ok) and args.machine:
                    try:
                        merged[key] = machine_translate(english, lang)
                        print(f"  machine {lang} {key}")
                    except Exception as exc:
                        print(f"  machine-failed {lang} {key}: {exc}", file=sys.stderr)
                        merged[key] = authored.get(key) or prev or english
                    continue
                if authored.get(key) and (not prev or prev == english):
                    merged[key] = authored[key]
                    continue
                if prev:
                    merged[key] = prev
                    if not hash_ok:
                        stale.append(f"{lang}:{key}")
                    continue
                merged[key] = english
                missing_report.append(f"{lang}:{key}")

        if not args.dry_run:
            write_locale(lang, merged)
            print(f"wrote _data/i18n/{lang}.yml ({len(merged)} keys) from {source if lang == 'en' else 'merge'}")
        else:
            print(f"dry-run {lang}: {len(merged)} keys")

    if not args.dry_run:
        HASH_PATH.write_text(json.dumps(new_hashes, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {HASH_PATH.relative_to(ROOT)}")

    if stale:
        print("stale (English changed, translation kept — re-run with --machine or edit by hand):")
        for row in stale:
            print(" ", row)
    if missing_report:
        print("still English placeholders:")
        for row in missing_report:
            print(" ", row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
