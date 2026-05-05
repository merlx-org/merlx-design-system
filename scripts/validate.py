#!/usr/bin/env python3
"""Validate every chunk in the MERLx design system repo.

Checks:
1. Every expected chunk in scripts/manifest.yaml exists at <category>/<slug>.md
2. Every chunk file has YAML frontmatter with required fields:
   - title (str), category (str), tokens (list), related (list)
3. category in frontmatter matches the folder.

Exits non-zero on any failure.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REQUIRED_FIELDS = {"title", "category", "tokens", "related"}
VALID_CATEGORIES = {"foundations", "components", "data-viz", "patterns", "meta"}
ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "scripts" / "manifest.yaml"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing frontmatter block")
    return yaml.safe_load(match.group(1))


def main() -> int:
    manifest = yaml.safe_load(MANIFEST.read_text())
    errors: list[str] = []
    count = 0

    for category, slugs in manifest.items():
        if category not in VALID_CATEGORIES:
            errors.append(f"manifest: unknown category '{category}'")
            continue
        for slug in slugs:
            path = ROOT / category / f"{slug}.md"
            if not path.exists():
                errors.append(f"missing: {path.relative_to(ROOT)}")
                continue
            try:
                fm = parse_frontmatter(path.read_text())
            except Exception as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")
                continue
            missing_fields = REQUIRED_FIELDS - set(fm or {})
            if missing_fields:
                errors.append(
                    f"{path.relative_to(ROOT)}: missing frontmatter fields: "
                    f"{sorted(missing_fields)}"
                )
                continue
            if fm["category"] != category:
                errors.append(
                    f"{path.relative_to(ROOT)}: frontmatter category "
                    f"'{fm['category']}' does not match folder '{category}'"
                )
                continue
            if not isinstance(fm["tokens"], list) or not isinstance(fm["related"], list):
                errors.append(
                    f"{path.relative_to(ROOT)}: 'tokens' and 'related' must be lists"
                )
                continue
            count += 1

    if errors:
        print("VALIDATION FAILED", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK — {count} chunks valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
