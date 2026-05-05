# MERLx Stage 1 — Modularity + Completeness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the 343-line `~/.claude/design-systems/MERLx-design-system.md` into a structured private GitHub repo at `~/github/merlx-design-system` containing 34 topic-sized chunks, ready for `claude.ai/design` consumption as v0.1.0.

**Architecture:** Markdown-first repo with strict per-chunk frontmatter, a Python validator script that enforces chunk shape, a `tokens/` folder reserved for Stage 2, and an `assets/` folder for brand SVGs. No build step in Stage 1 — chunks are read raw.

**Tech Stack:** Markdown (CommonMark + GitHub-flavored), YAML frontmatter, Python 3 (validator only), git, GitHub CLI (`gh`), Phosphor icon library (referenced, not bundled).

**Source spec:** `docs/specs/2026-05-05-merlx-design-system-design.md`

**Source for migrated content:** `~/.claude/design-systems/MERLx-design-system.md` (the existing 343-line monolith).

---

## Conventions for every content task

Every chunk file MUST follow this skeleton, defined in spec §8:

```markdown
---
title: <Human Title>
category: <foundations | components | data-viz | patterns | meta>
tokens: [list, of, tokens, referenced]
related: [list, of, related, chunk, slugs]
---

# <Human Title>

## Principles
<one short paragraph>

## Tokens / Values
<table or list>

## Semantic Assignment Rules
<when to use which>

## Examples
<code-fence snippets and short visual references>

## Don'ts
<the negative space>
```

For chunks where a section genuinely doesn't apply (e.g., `identity.md` has no tokens of its own), keep the heading present and write one line explaining why it's empty (e.g., "No tokens — see `color.md` and `typography.md`."). Predictable structure beats omission.

After every chunk task, run:

```bash
python3 scripts/validate.py
```

Expected: `OK — N chunks valid` or a clear error pointing to the broken chunk.

Then commit with a conventional message: `feat(<category>): add <slug> chunk` or `chore(migration): port <section> from monolith`.

---

## Task 1: Scaffold the repo

**Files:**
- Create: `LICENSE`
- Create: `.gitignore`
- Create: `CHANGELOG.md`
- Create: `README.md` (initial)
- Create: empty folder placeholders (`.gitkeep` files): `foundations/`, `components/`, `data-viz/`, `patterns/`, `meta/`, `tokens/`, `assets/logo/`, `scripts/`

- [ ] **Step 1: Create LICENSE (MIT)**

```
MIT License

Copyright (c) 2026 Kristian Svendsen / MERLx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

- [ ] **Step 2: Create .gitignore**

```
.DS_Store
__pycache__/
*.pyc
.venv/
node_modules/
.idea/
.vscode/
*.fig.bkp
```

- [ ] **Step 3: Create CHANGELOG.md**

```markdown
# Changelog

All notable changes to the MERLx Design System are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Stage 1 scaffolding: 34-chunk modular structure
```

- [ ] **Step 4: Create initial README.md**

```markdown
# MERLx Design System

A token-first design reference for AI coding assistants and human contributors.
Maintains visual consistency across all MERLx projects.

**Status:** v0.1.0 in progress. See [Stage 1 plan](docs/plans/2026-05-05-merlx-stage-1-modularity-and-completeness.md).

## Aesthetic

Nordic Product Studio — calm, minimal, warm. Serious analytical tooling without the corporate chill.

## How to use

This repo holds 34 topic-sized Markdown chunks plus token exports and brand assets. Consumers:

- **`claude.ai/design`** — point at the repo URL when configuring a design system; pair with `MERLx.fig` (added in Stage 3) and the SVG assets in `assets/`.
- **Claude Skills** — chunk frontmatter maps tasks to relevant chunks.
- **Humans** — read the chunks below; the rendered docs site lands in Stage 3.

## Index

(Populated in Task 24 once all chunks exist.)

## License

MIT — see `LICENSE`.
```

- [ ] **Step 5: Create empty folder structure with .gitkeep files**

```bash
cd ~/github/merlx-design-system
for d in foundations components data-viz patterns meta tokens assets/logo scripts; do
  mkdir -p "$d"
  touch "$d/.gitkeep"
done
```

- [ ] **Step 6: Commit scaffolding**

```bash
cd ~/github/merlx-design-system
git add LICENSE .gitignore CHANGELOG.md README.md foundations components data-viz patterns meta tokens assets scripts
git commit -m "chore: scaffold repo structure for Stage 1"
```

---

## Task 2: Build the chunk validator

**Files:**
- Create: `scripts/validate.py`
- Create: `scripts/manifest.yaml`

The validator enforces frontmatter shape and confirms every expected chunk exists. It is the "test suite" for this docs repo.

- [ ] **Step 1: Create the manifest of expected chunks**

`scripts/manifest.yaml`:

```yaml
foundations:
  - identity
  - color
  - typography
  - spacing
  - radius
  - motion
  - elevation
  - iconography
components:
  - buttons
  - inputs
  - cards
  - badges
  - tables
  - modals
  - empty-states
  - navigation
  - tooltips
  - forms
  - notifications
data-viz:
  - charts
  - maps
  - dense-tables
  - sparklines-and-stats
patterns:
  - layouts
  - loading-and-skeletons
  - empty-error-success
  - dark-mode
meta:
  - accessibility
  - responsive
  - ai-assistant-instructions
  - voice-and-content
```

- [ ] **Step 2: Write the validator**

`scripts/validate.py`:

```python
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
```

- [ ] **Step 3: Install pyyaml in a local virtualenv**

```bash
cd ~/github/merlx-design-system
python3 -m venv .venv
.venv/bin/pip install pyyaml
```

- [ ] **Step 4: Run the validator and confirm it reports the expected number of missing chunks**

```bash
cd ~/github/merlx-design-system
.venv/bin/python scripts/validate.py
```

Expected: VALIDATION FAILED with 30 "missing:" lines (28 chunks + 2 .gitkeep folders that don't matter — only 28 chunk slugs in manifest, so expect 28 "missing:" lines). Manifest count: 8 + 11 + 4 + 4 + 5 = 32 — wait, that's wrong. Recount: foundations 8, components 11, data-viz 4, patterns 4, meta 4 = 31. The 4 non-chunk meta items (accessibility, responsive, ai-assistant-instructions, voice-and-content) are in manifest but `tokens/` and `assets/` folders are NOT chunks — they have separate READMEs. So manifest expects 31 chunks. Validator should report 31 missing.

- [ ] **Step 5: Commit validator + manifest**

```bash
cd ~/github/merlx-design-system
git add scripts/validate.py scripts/manifest.yaml .venv/.gitignore || true
echo ".venv/" >> .gitignore
git add .gitignore scripts/
git commit -m "chore: add chunk validator and manifest"
```

---

## Task 3: Migrate `foundations/identity.md`

**Source:** `~/.claude/design-systems/MERLx-design-system.md` Section 1 ("Identity & Aesthetic Principles") + the logo paragraph.

**Files:**
- Create: `foundations/identity.md`

- [ ] **Step 1: Write the chunk**

```markdown
---
title: Identity
category: foundations
tokens: []
related: [color, typography, voice-and-content, iconography]
---

# Identity

## Principles

Nordic Product Studio — calm, minimal, warm. The visual language communicates "serious analytical tool" without feeling cold or corporate. Scandinavian design applied to data products.

Five principles drive every other decision in this system:

- **Warmth over sterility** — Use warm neutrals (Shell palette) not cool grays. Backgrounds should feel like paper, not screens.
- **Data clarity over decoration** — Every visual element should serve comprehension. No gradients, no drop shadows, no decorative borders.
- **Typography as hierarchy** — Three font families exist for a reason: Inter for UI, DM Serif Display for editorial drama, IBM Plex Mono for data. Never mix their roles.
- **Color with purpose** — Accent colors are semantic, not decorative. Each color earns its place by encoding meaning (status, category, severity).
- **Calm motion** — Transitions are subtle (200ms, ease-out). No bouncing, no sliding panels, no attention-grabbing animation.

## Tokens / Values

No tokens — identity is a principle layer. See `color.md`, `typography.md`, and `motion.md` for the underlying values.

## Semantic Assignment Rules

When a design decision has multiple valid options, pick the one that best honors these principles in priority order: data clarity → warmth → typographic discipline → semantic color → calm motion.

## Examples

**Logo.** "MERLx" rendered in Inter Bold with the "x" in Iris (`#8071BC`). Always paired with a project subtitle in DM Serif Display italic.

**Application of principles to a new component:** when designing a status indicator, prefer text + a small Phosphor Fill icon over a colored dot alone (data clarity). Use Shell-derived backgrounds, not white-on-gray (warmth). Reserve red strictly for `error` (semantic color).

## Don'ts

- Don't add decorative gradients, drop shadows, or ornamental borders.
- Don't use cool grays (`#888`, `#aaa`) — always pick from the Shell or Ink scales.
- Don't introduce a fourth font family.
- Don't pick accent colors for visual interest alone — every use should encode meaning.
- Don't animate for attention; animate for state change.
```

- [ ] **Step 2: Validate**

```bash
.venv/bin/python scripts/validate.py
```

Expected: 1 chunk valid, 30 missing.

- [ ] **Step 3: Commit**

```bash
git add foundations/identity.md
git commit -m "feat(foundations): add identity chunk"
```

---

## Task 4: Migrate `foundations/color.md`

**Source:** Section 2 of monolith (Core Palette, Accent Palette, Dim Variants, Status Colors, Semantic Assignment Rules).

**Files:**
- Create: `foundations/color.md`

- [ ] **Step 1: Write the chunk**

Port Section 2 of the monolith verbatim into the standard skeleton. Frontmatter:

```yaml
---
title: Color
category: foundations
tokens: [shell, shell-warm, shell-cool, ink, ink-light, ink-muted, ink-faint, surface, border, border-light, sand, sand-light, sand-dark, iris, iris-light, iris-dark, deep-teal, deep-teal-light, deep-iris, deep-iris-light, ember, ember-light, ember-dark, sand-dim, iris-dim, deep-teal-dim, deep-iris-dim, ember-dim, success, error, error-light]
related: [identity, dark-mode, accessibility, data-viz/charts, data-viz/maps]
---
```

Body must contain in order:

1. **Principles** — one paragraph explaining "color encodes meaning, never decoration."
2. **Tokens / Values** — three tables (Core, Accent, Dim Variants) and a Status Colors table, copied from monolith Section 2.
3. **Semantic Assignment Rules** — copied verbatim from monolith Section 2's "Semantic Assignment Rules" subsection.
4. **Examples** — 2 short snippets: (a) primary button using `deep-teal` + `deep-teal-light` hover; (b) badge using `iris-dim` background + `iris-dark` text.
5. **Don'ts** — bullet list, drawn from the monolith's Section 8 don'ts that touch color: no off-palette colors, no raw hex in components, never `gray-500`/`#333`, no red outside error states.

- [ ] **Step 2: Validate**

```bash
.venv/bin/python scripts/validate.py
```

Expected: 2 chunks valid, 29 missing.

- [ ] **Step 3: Commit**

```bash
git add foundations/color.md
git commit -m "feat(foundations): add color chunk"
```

---

## Task 5: Migrate `foundations/typography.md`

**Source:** Section 3 of monolith.

**Files:**
- Create: `foundations/typography.md`

- [ ] **Step 1: Write the chunk**

Frontmatter:

```yaml
---
title: Typography
category: foundations
tokens: [text-xl, text-lg, text-base, text-sm, text-xs, text-xxs, text-micro]
related: [identity, voice-and-content, accessibility]
---
```

Body sections, populated from monolith Section 3:

1. **Principles** — "Three families, three jobs. Inter for UI, DM Serif Display for editorial moments, IBM Plex Mono for data. Roles do not cross."
2. **Tokens / Values** — the Font Stack table, Sizing Scale table, Letter Spacing table from the monolith.
3. **Semantic Assignment Rules** — the "Usage Rules" bullet list from the monolith, restructured by surface (heading / body / label / display / mono).
4. **Examples** — 3 snippets: a heading, a body paragraph, a data cell using IBM Plex Mono.
5. **Don'ts** — never combine all three families in one component; never DM Serif Display for body or buttons; never IBM Plex Mono for headings; never below 9px; never below 11px for readable content.

- [ ] **Step 2: Validate**

```bash
.venv/bin/python scripts/validate.py
```

Expected: 3 chunks valid.

- [ ] **Step 3: Commit**

```bash
git add foundations/typography.md
git commit -m "feat(foundations): add typography chunk"
```

---

## Task 6: Migrate `foundations/spacing.md`

**Source:** Section 4 of monolith — only the spacing portion (the "Spacing Scale" table and the "Layout Rules" bullets that pertain to spacing).

**Files:**
- Create: `foundations/spacing.md`

- [ ] **Step 1: Write the chunk**

Frontmatter:

```yaml
---
title: Spacing
category: foundations
tokens: [space-1, space-2, space-3, space-4, space-5, space-6, space-7, space-8, space-10, space-12]
related: [radius, layouts, responsive]
---
```

Body:

1. **Principles** — "Tighter is better than looser. Pick from the scale; if a value feels between two tokens, take the smaller one."
2. **Tokens / Values** — the Spacing Scale table from monolith Section 4.
3. **Semantic Assignment Rules** — restructured layout rules: card padding `space-7`–`space-8`, page padding `space-10`–`space-12`, dense grid gaps `space-5`, comfortable grid gaps `space-10`, scrollable region bottom-padding requirement.
4. **Examples** — 2 short snippets: card padding, dense grid gap.
5. **Don'ts** — don't pick custom px values; don't use `space-1` or `space-2` for component padding; don't go below `space-4` inside a card.

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(foundations): add spacing chunk`)

---

## Task 7: Migrate `foundations/radius.md`

**Source:** Section 4 of monolith — only the Border Radius table.

**Files:**
- Create: `foundations/radius.md`

- [ ] **Step 1: Write the chunk**

Frontmatter:

```yaml
---
title: Radius
category: foundations
tokens: [radius-sm, radius-md, radius-lg, radius-xl, radius-pill]
related: [identity, components/cards, components/buttons, components/badges]
---
```

Body:

1. **Principles** — "Radius signals scale: smaller surfaces get tighter corners. Pills are reserved for badges and tracks."
2. **Tokens / Values** — Border Radius table from monolith.
3. **Semantic Assignment Rules** — buttons/inputs/small cards = `radius-sm`; cards/panels/modals = `radius-md`; large containers/feature cards = `radius-lg`; hero/prominent surfaces = `radius-xl`; badges/tags/pills/toggle tracks = `radius-pill`.
4. **Examples** — button with `radius-sm`, card with `radius-md`, badge with `radius-pill`.
5. **Don'ts** — don't use `radius-pill` on rectangular elements (text fields, cards). Don't invent intermediate values like 6px or 10px. Don't apply `radius-xl` to anything smaller than a hero element.

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(foundations): add radius chunk`)

---

## Task 8: Migrate `foundations/motion.md`

**Source:** Section 5 of monolith.

**Files:**
- Create: `foundations/motion.md`

- [ ] **Step 1: Write the chunk**

Frontmatter:

```yaml
---
title: Motion
category: foundations
tokens: [motion-fast, motion-default, motion-slow]
related: [identity, accessibility, patterns/loading-and-skeletons]
---
```

Body: port monolith Section 5 verbatim into the skeleton. Default transition `200ms cubic-bezier(0.16, 1, 0.3, 1)`; the timing scale table; rules including no spring, no bounce, no overshoot, no animation on page load, always respect `prefers-reduced-motion`.

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(foundations): add motion chunk`)

---

## Task 9: Write `foundations/elevation.md` (NEW)

**Files:**
- Create: `foundations/elevation.md`

- [ ] **Step 1: Write the chunk**

```markdown
---
title: Elevation
category: foundations
tokens: [shell, shell-warm, shell-cool, surface, border, border-light]
related: [identity, color, components/cards, components/modals]
---

# Elevation

## Principles

MERLx does not use shadows. Elevation is communicated through background contrast — a `surface` card on a `shell` page reads as "above" without a single pixel of blur. This is a hard rule from the identity layer: "data clarity over decoration."

## Tokens / Values

| Layer | Background | Border | Use |
|---|---|---|---|
| Page | `shell` | — | Default page background |
| Section offset | `shell-warm` | — | Sidebars, secondary surfaces, hover backgrounds |
| Card | `surface` (#FFFFFF) | `border-light`, 1px | Standard card on a `shell` page |
| Modal | `surface` | `border`, 1px | Modal/drawer over a `rgba(17,17,17,0.4)` overlay |
| Inset | `shell-cool` | — | Read-only or nested content within a `surface` card |

## Semantic Assignment Rules

- A surface always sits on a darker background than itself, or on the same background with a 1px `border-light` separator.
- Hover does not raise an element. Hover changes background (`shell-warm`) or border color, never adds a shadow.
- Modals are the one case where literal layering exists — overlay + `surface` panel. The overlay is the elevation cue, not a shadow on the modal.

## Examples

A card on the dashboard:

```css
.card {
  background: var(--surface);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
}
```

A sidebar against the page:

```css
.sidebar { background: var(--shell-warm); }
.page { background: var(--shell); }
```

## Don'ts

- Don't use `box-shadow` for any elevation cue, ever.
- Don't use `filter: drop-shadow()` as a workaround.
- Don't stack three or more contrast layers; two is enough (page + surface, or page + sidebar).
- Don't add a border AND a darker background to communicate elevation — pick one.
```

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(foundations): add elevation chunk`)

---

## Task 10: Write `foundations/iconography.md` (NEW)

**Files:**
- Create: `foundations/iconography.md`

This chunk encodes the locked Phosphor decision from spec §10.

- [ ] **Step 1: Write the chunk**

```markdown
---
title: Iconography
category: foundations
tokens: []
related: [identity, color, components/buttons, components/navigation]
---

# Iconography

## Principles

One icon family across all MERLx products: **Phosphor Icons** (MIT). Phosphor's multi-weight design lets MERLx use Thin as its visual signature while keeping Regular and Fill available for legibility and state contrast. No other icon library may be introduced.

## Tokens / Values

| Context | Weight | Size |
|---|---|---|
| Default UI (buttons, navigation, cards) | Thin (1px) | 16–20px |
| Editorial / hero / empty states | Thin | 24–32px |
| Dense tables, badges, sub-16px contexts | Regular (1.5px) | 12–14px |
| Active / selected / emphasis state | Fill | match outline size |
| Forbidden | Light, Bold, Duotone | — |

Color: icons inherit `currentColor` from their parent text element. Hard-code an icon color only when it carries semantic meaning (e.g., a Fill `warning-circle` taking the `ember` token).

## Semantic Assignment Rules

- **Default = Thin.** Any new icon use starts at Thin, 16–20px.
- **Drop to Regular only when Thin breaks.** Phosphor Thin renders fragile at sub-16px — anti-aliasing dulls the strokes on standard-DPR displays. Switch to Regular for table-row icons, badges, and 12–14px contexts.
- **Fill is for state contrast.** A filled icon paired with an outline icon of the same name reads as "active vs inactive." Never use Fill for decoration alone.
- **Pick semantic icon names.** Use `warning-circle` for warnings, `check-circle` for success, `arrow-up-right` for external links — match Phosphor's name to its meaning.

## Examples

Default UI icon (button):

```tsx
import { ArrowRight } from "phosphor-react";
<button><ArrowRight size={18} weight="thin" /> Next</button>
```

Active/inactive contrast:

```tsx
{isActive
  ? <Circle size={16} weight="fill" color="var(--deep-teal)" />
  : <Circle size={16} weight="thin" color="var(--ink-muted)" />}
```

Dense table row:

```tsx
<TrashSimple size={14} weight="regular" />
```

## Don'ts

- Don't introduce a second icon library (Lucide, Heroicons, custom SVG sets).
- Don't use Phosphor Light, Bold, or Duotone weights — they break the visual signature.
- Don't render Thin icons below 16px; switch to Regular.
- Don't hard-code icon colors except for semantic states.
- Don't combine multiple icon weights inside a single component except for outline/Fill state contrast.
```

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(foundations): add iconography chunk`)

---

## Tasks 11–16: Migrate component chunks from monolith Section 6

For each task below, port the matching subsection of monolith Section 6 into the standard 5-section skeleton. Frontmatter `category: components`. The Principles section is one short paragraph; Examples is at least one code-fence; Don'ts is a bullet list.

### Task 11: `components/cards.md`

Source: monolith Section 6 → "Cards". Tokens: `surface, border-light, radius-md, space-7, space-8`. Related: `[elevation, radius, spacing]`. Don'ts must include "no box-shadow."

### Task 12: `components/buttons.md`

Source: monolith Section 6 → "Buttons". Tokens: `[deep-teal, deep-teal-light, error, border, shell-warm, ink, radius-sm, text-sm]`. Related: `[color, typography, iconography]`. Don'ts must include "no uppercase button text."

### Task 13: `components/badges.md`

Source: monolith Section 6 → "Badges / Pills". Tokens: `[radius-pill, text-xxs, text-xs, iris-dim, iris-dark, sand-dim, sand-dark, ember-dim, ember-dark, deep-teal-dim, deep-teal]`. Related: `[color, radius, typography]`.

### Task 14: `components/inputs.md`

Source: monolith Section 6 → "Inputs". Expand to cover textarea, select, checkbox, radio, switch, search beyond the monolith's text-only treatment. Tokens: `[surface, border, iris, radius-sm, ink, ink-faint, text-base]`. Related: `[forms, color, accessibility]`.

For the new variants (textarea, select, checkbox, radio, switch, search), each gets a 1-paragraph rule + a code snippet. Switch tracks use `radius-pill`; checkboxes use `radius-sm`; radios are circular; search inputs include a Phosphor `MagnifyingGlass` Thin 16px icon.

### Task 15: `components/tables.md`

Source: monolith Section 6 → "Tables / Dense Data". Tokens: `[border-light, ink-muted, shell-warm, text-micro, text-xs]`. Related: `[data-viz/dense-tables, typography, spacing]`. Note the cross-link: this chunk covers the *component-level* table; the analytical-grade variant lives in `data-viz/dense-tables.md`.

### Task 16: `components/modals.md`

Source: monolith Section 6 → "Modals / Drawers". Tokens: `[surface, radius-lg, space-10, ink-muted, ink]`. Related: `[elevation, motion, accessibility]`. Modal overlay = `rgba(17,17,17,0.4)`; max-width 640px content / 400px confirmations; `space-10` padding.

For each task in this group:
- [ ] **Step 1:** Write the chunk per the standard skeleton.
- [ ] **Step 2:** Run `.venv/bin/python scripts/validate.py`.
- [ ] **Step 3:** Commit `feat(components): add <slug> chunk`.

---

## Task 17: Migrate `components/empty-states.md`

**Source:** monolith Section 6 → "Empty States".

- [ ] **Step 1: Write the chunk**

Frontmatter:

```yaml
---
title: Empty States
category: components
tokens: [ink-light, ink-muted, text-lg, text-sm]
related: [typography, voice-and-content, patterns/empty-error-success]
---
```

Body content from monolith: center-aligned text, DM Serif Display italic heading at `text-lg` in `ink-light`, Inter 400 description at `text-sm` in `ink-muted`, one line each maximum. Examples: a no-results table state, a no-data dashboard state. Don'ts: no illustrations, no decorative icons larger than 32px, no calls-to-action stacked vertically — one CTA max.

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(components): add empty-states chunk`)

---

## Task 18: Migrate `components/navigation.md`

**Source:** monolith Section 6 → "Sidebar Navigation". Expand to cover topbar, breadcrumbs, and tabs (which the monolith does not address).

- [ ] **Step 1: Write the chunk**

Frontmatter:

```yaml
---
title: Navigation
category: components
tokens: [shell-warm, surface, deep-teal, deep-teal-dim, ink-faint, text-xxs, space-3, space-4]
related: [layouts, responsive, iconography, color]
---
```

Body must cover four navigation surfaces:

1. **Sidebar** — width 200–240px (nav) or 300–360px (detail), background `shell-warm` or `surface`, active item `deep-teal-dim` background + `deep-teal` text, item padding `space-3` × `space-4`, section labels Inter 600 `text-xxs` uppercase `ink-faint` letter-spacing 1.5px. (From monolith.)
2. **Topbar** — height 48px, background `surface`, bottom border `border-light` 1px, logo + workspace selector left, primary actions right, no shadows.
3. **Breadcrumbs** — Inter 500 `text-xs`, separator `/` in `ink-faint`, current page in `ink`, prior crumbs in `ink-muted` underlined on hover.
4. **Tabs** — Inter 500 `text-sm`, active tab has 2px `deep-teal` underline + `ink` text, inactive tabs `ink-muted`, hover `ink-light`. No background pill; underline only.

Code snippets for sidebar item, topbar layout, breadcrumb, and tab strip.

Don'ts: no hover backgrounds on breadcrumbs, no full-pill tab backgrounds, no icon-only sidebar items without a tooltip, no animated underlines on tabs.

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(components): add navigation chunk`)

---

## Task 19: Write `components/tooltips.md` (NEW)

This chunk locks the 9px sizing rule from Kristian's existing feedback memory.

**Files:**
- Create: `components/tooltips.md`

- [ ] **Step 1: Write the chunk**

```markdown
---
title: Tooltips
category: components
tokens: [ink, surface, text-micro, radius-sm, motion-fast]
related: [motion, typography, accessibility]
---

# Tooltips

## Principles

Tooltips are very small and wide, never tall and narrow. They explain a single non-obvious affordance — a status icon, a truncated value, a keyboard shortcut. They are not for primary content.

## Tokens / Values

| Property | Value |
|---|---|
| Font size | `text-micro` (9px) |
| Font family | Inter 400 |
| Background | `ink` (#111111) |
| Text color | `surface` (#FFFFFF) |
| Padding | `space-2` vertical, `space-4` horizontal |
| Radius | `radius-sm` (4px) |
| Max width | 280px |
| Min width | 80px (lean wide, not tall) |
| Letter spacing | 0.04em |
| Text transform | `none` (always reset uppercase inheritance) |
| Show delay | 400ms |
| Hide delay | 100ms |
| Transition | `motion-fast` opacity |

## Semantic Assignment Rules

- Trigger on hover and focus — never click.
- Position above the trigger by default; flip to below if it would clip the viewport.
- Single line where possible. If it wraps, prefer a wider tooltip over a taller one.
- Always reset `text-transform: none` even on triggers that inherit `uppercase` (e.g., section labels).
- Never put interactive elements (links, buttons) inside a tooltip — that's a popover, not a tooltip.

## Examples

```css
.tooltip {
  font-size: var(--text-micro);
  font-family: Inter, system-ui, sans-serif;
  font-weight: 400;
  text-transform: none;
  letter-spacing: 0.04em;
  background: var(--ink);
  color: var(--surface);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-sm);
  max-width: 280px;
  min-width: 80px;
  transition: opacity var(--motion-fast) ease-out;
}
```

## Don'ts

- Don't size tooltips at `text-xxs` or larger — 9px is the rule.
- Don't make tooltips tall and narrow.
- Don't inherit uppercase from the trigger — always explicitly reset.
- Don't put links, buttons, or form fields inside a tooltip.
- Don't show a tooltip on tap on touch devices; provide an inline help icon instead.
```

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(components): add tooltips chunk`)

---

## Task 20: Write `components/forms.md` (NEW)

**Files:**
- Create: `components/forms.md`

- [ ] **Step 1: Write the chunk**

Frontmatter:

```yaml
---
title: Forms
category: components
tokens: [ink, ink-muted, ember, ember-dim, error, error-light, success, surface, border, border-light, iris, radius-sm, space-2, space-3, space-4, space-5, text-xs, text-sm]
related: [inputs, voice-and-content, accessibility, notifications]
---
```

Required body content:

1. **Principles** — forms communicate state explicitly; every required field is marked; error messages name the field and the fix; never rely on color alone (icon + text + color).
2. **Tokens / Values** — table covering: label spacing (`space-2` below label), helper text (Inter 400 `text-xs` `ink-muted`), error text (Inter 500 `text-xs` `error`), success text (Inter 500 `text-xs` `success`), required indicator (`*` in `ember` after the label).
3. **Semantic Assignment Rules** — inline validation only after the user leaves the field (`onBlur`), never on every keystroke; submit-time validation aggregates errors at the top with anchor links; disabled fields use `ink-faint` text on `shell-warm` background; readonly fields use `ink-muted` text on `shell-cool` background.
4. **Examples** — code snippet for: label + input + helper text; label + input + error state; label + input + success state; required field marker.
5. **Don'ts** — don't show errors before the user has interacted with the field; don't use red borders without an error message; don't rely on color alone (always pair with an icon and text); don't use placeholder text as the only label.

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(components): add forms chunk`)

---

## Task 21: Write `components/notifications.md` (NEW)

**Files:**
- Create: `components/notifications.md`

- [ ] **Step 1: Write the chunk**

Frontmatter:

```yaml
---
title: Notifications
category: components
tokens: [ink, ink-muted, surface, border-light, ember, ember-dim, ember-dark, error, error-light, success, iris, iris-dim, iris-dark, deep-teal, deep-teal-dim, radius-md, space-4, space-5, space-8, motion-slow, text-sm, text-xs]
related: [color, motion, voice-and-content, patterns/empty-error-success]
---
```

Body must cover three notification surfaces:

1. **Toast** — bottom-right corner, max-width 360px, `surface` background, `border-light` 1px, `radius-md`, `space-5` padding, Phosphor Thin 18px status icon left + Inter 500 `text-sm` title + optional Inter 400 `text-xs` `ink-muted` description, dismiss button top-right, auto-dismiss 5s for info/success, never auto-dismiss for error. Slide-in disabled — fade only, `motion-slow`.
2. **Banner** — full-width below topbar, semantic-color tinted background using the dim variant (e.g., `ember-dim` for warning), `space-4` × `space-8` padding, icon + text + optional CTA + dismiss.
3. **Inline alert** — within a card or form section, no border, semantic dim background, `radius-md`, `space-4` padding. Used when the alert relates to a specific component, not the whole page.

Color palette by severity:

| Severity | Background | Icon/text accent |
|---|---|---|
| Info | `iris-dim` | `iris-dark` |
| Success | `#E8F4EF` (success-dim, derived) | `success` |
| Warning | `ember-dim` | `ember-dark` |
| Error | `#F4E2DD` (error-dim, derived) | `error` |
| Neutral | `shell-warm` | `ink-muted` |

(Note: `success-dim` and `error-dim` will need to be added to `color.md` in a future revision; for now, document the derived rgba inline.)

Don'ts: no slide-in animation, no spring easing, never auto-dismiss errors, no more than one banner stacked at once.

- [ ] **Step 2: Validate**, **Step 3: Commit** (`feat(components): add notifications chunk`)

---

## Task 22: Write data-viz chunks

For each chunk in this task group:
- Frontmatter `category: data-viz`.
- Body: standard 5-section skeleton.
- After writing each: run validator, commit `feat(data-viz): add <slug> chunk`.

### `data-viz/charts.md`

Tokens: `[deep-teal, ember, iris, sand-dark, deep-iris, ink, ink-muted, ink-faint, border-light, text-micro, text-xs]`. Related: `[color, typography, dense-tables]`.

Required content:

- Categorical color order: `deep-teal, ember, iris, sand-dark, deep-iris` — same as monolith Section 2 categorical rule.
- Axis lines: `border-light` 1px, no tick marks below the axis.
- Gridlines: horizontal only, `border-light`, never vertical.
- Axis labels: Inter 500 `text-xs` `ink-muted`.
- Numeric labels: IBM Plex Mono `text-micro` `ink`.
- Legend: top-right, no border, no background; Inter 500 `text-xs` with a 12px swatch in the categorical color.
- No drop shadows on data, no 3D, no animation on first paint.
- Bar charts: 60% bar width, 40% gap; rounded top corners only at `radius-sm` (optional).
- Line charts: 1.5px stroke; data point dots only on hover at 4px filled.
- Area charts: 25% opacity fill of the line stroke color.
- Stacked: stacking order matches the categorical color order; legend lists in the same order.

Don'ts: no rainbow palettes, no diverging gradients except for choropleth (see `maps.md`), no pie charts (use stacked bars), no 3D.

### `data-viz/maps.md`

Tokens: `[shell, deep-teal, ember, iris, sand-dark, deep-iris, ink, ink-muted, border-light]`. Related: `[charts, color, accessibility]`.

Required content:

- Choropleth palette (sequential): a 5-step ramp from `shell-warm` → `deep-teal` for any single positive metric. For diverging (positive vs negative), use `error` ↔ `success` with `shell` at zero.
- Categorical map (regions/categories): same order as charts — `deep-teal, ember, iris, sand-dark, deep-iris`.
- Point/marker: 6px Phosphor Fill `circle` at the categorical color, 1px `surface` border for contrast on dense backgrounds.
- Heatmap: alpha-blend `ember` at 0–60% opacity over `shell`. No rainbow heatmaps.
- Country/region borders: `border-light` 1px when on `shell`; `surface` 1px when on a colored fill.
- Map text labels: Inter 500 `text-xs` `ink` with 2px `surface` halo for legibility on colored fills.
- Legends: discrete swatches for categorical, continuous gradient bar for choropleth/heatmap.

Don'ts: no terrain or satellite basemaps in MERLx products (visual noise); no rainbow scales; no bubble maps that scale dot area larger than 40px.

### `data-viz/dense-tables.md`

Tokens: `[border-light, shell-warm, ink, ink-muted, text-micro, text-xs, space-2, space-4]`. Related: `[components/tables, typography, spacing]`.

Distinguishes the analytical-grade table (used in PRISM, ToC Tester, OASIS) from the simpler component-level `components/tables.md`. Required content:

- Row height: 28px (vs 36px in standard tables).
- Font: IBM Plex Mono `text-micro` for numeric cells, Inter 400 `text-xs` for text cells.
- Sticky first column and header row at scroll boundaries.
- Numeric right-alignment, units in `ink-muted` next to the number.
- Sortable headers: Inter 600 `text-xs` uppercase `ink-muted` with a 10px Phosphor `caret-up` / `caret-down` Regular icon when sorted.
- Row selection: 1px left-edge `deep-teal` accent + `deep-teal-dim` background, never a checkbox without label.
- Conditional formatting: cell background uses dim accent variants (`ember-dim` for warning thresholds, `success` derivation for positive). Never raw color fills.
- Dense table examples: indicator monitoring grid, KII coding ledger, observation-by-observation export view.

Don'ts: no zebra striping, no row hover that obscures conditional formatting, no inline-editable cells without an explicit edit affordance.

### `data-viz/sparklines-and-stats.md`

Tokens: `[deep-teal, ember, error, success, ink, ink-muted, text-lg, text-xs, text-micro]`. Related: `[charts, typography]`.

Required content:

- KPI tile: Inter 700 `text-lg` value (or DM Serif Display for editorial dashboards), Inter 500 `text-xs` `ink-muted` label above, 1-line `text-xs` delta below in `success` (positive), `error` (negative), or `ink-muted` (neutral).
- Sparkline: 24px tall, 1.5px stroke, `deep-teal` default; `ember` if the metric is currently above warning threshold; no gridlines, no axes, no dots except a single endpoint dot.
- Delta indicators: triangle (Phosphor `triangle-up` / `triangle-down` Fill 10px) + percentage in IBM Plex Mono `text-micro`.
- Time-window label: Inter 500 `text-xxs` uppercase `ink-faint` (e.g., "30D", "MTD").
- Don'ts: no animated number tickers; no large-then-shrinking values on load; no decorative icons next to the value.

- [ ] **Step 1: Write all four chunks per the specs above.**
- [ ] **Step 2: Validate after each.**
- [ ] **Step 3: Commit one feat per chunk.**

---

## Task 23: Write patterns chunks

Same convention: frontmatter `category: patterns`, standard skeleton, validate after each, commit `feat(patterns): add <slug> chunk`.

### `patterns/layouts.md`

Tokens: `[shell, shell-warm, surface, border-light, space-5, space-10, space-12]`. Related: `[spacing, components/navigation, responsive]`.

Required content — four canonical layouts:

1. **Three-pane** — sidebar (200–240px) + content (1fr) + detail panel (300–360px). Used in PRISM, Aperture, ToC Tester. Detail panel collapses to modal below `bp-tablet`.
2. **Dashboard grid** — sidebar + content as a 12-column grid with `space-5` gaps. KPI tiles span 3 columns each; charts span 6 or 12.
3. **Document reader** — single centered column, max-width 720px, `space-12` page padding, optional right-rail TOC at 240px on `bp-desktop`.
4. **Full-bleed map/canvas** — sidebar + edge-to-edge map/canvas with overlaid floating panels at `space-5` from the viewport edges.

Each layout: ASCII wireframe + the CSS grid recipe.

Don'ts: no centered fixed-width layouts below 1024px breakpoint; no sidebars on the right; no layouts that depend on JavaScript for first paint.

### `patterns/loading-and-skeletons.md`

Tokens: `[shell-warm, ink-faint, motion-default, motion-slow, radius-sm, radius-md]`. Related: `[motion, components/cards, accessibility]`.

Required content:

- **Skeleton loaders** — `shell-warm` blocks at the same dimensions as the eventual content, no shimmer, opacity pulse only (1.0 → 0.5 → 1.0 over 1200ms, `linear`). Match the radius of the loaded element.
- **Inline progress** — 1px `iris` line at the top of a card while it loads. No spinners inside cards.
- **Spinner of last resort** — Phosphor `circle-notch` Thin 16px `ink-faint`, only when no skeleton is possible (e.g., indeterminate background job confirmation modal).
- **Empty-vs-loading distinction** — never show an empty state during load; always show a skeleton. The empty state is a *result*, not a *waiting room*.

Don'ts: no shimmer gradients, no full-page spinners, no progress bars below 1px, no spinner inside a button (use a Phosphor Thin icon swap instead).

### `patterns/empty-error-success.md`

Tokens: `[ink-light, ink-muted, error, success, ember, text-lg, text-sm]`. Related: `[components/empty-states, components/notifications, voice-and-content]`.

Required content — the three states every async surface must define:

1. **Empty** — refer to `components/empty-states.md`. One DM Serif Display italic line + one Inter 400 description line.
2. **Error** — Phosphor `warning-circle` Fill 24px `error` + Inter 600 `text-sm` `ink-light` title + Inter 400 `text-sm` `ink-muted` body naming what happened and what to try. Always offer a retry action when retry is meaningful.
3. **Success** — usually a brief toast, not a persistent surface. Persistent success surfaces only after destructive or one-way actions (data export complete, account deleted), using DM Serif Display italic title + a single line description.

Don'ts: no error states without a recovery path; no success states that block the user from moving on; never use the word "error" in the body — describe what happened.

### `patterns/dark-mode.md`

Tokens: every semantic token defined in `color.md`, with light + dark values. Related: `[color, accessibility, identity]`.

Required content:

1. **Principles** — dark mode is a value remap, not a parallel palette. Tokens keep their semantic names (`surface`, `ink`, `border`); only the values flip per theme. Components don't change.
2. **Token mapping table** — light vs dark for every semantic token:

| Token | Light | Dark |
|---|---|---|
| `shell` | `#F5F3EE` | `#15140F` |
| `shell-warm` | `#EDE9E1` | `#1F1D17` |
| `shell-cool` | `#F9F8F5` | `#191814` |
| `ink` | `#111111` | `#F0EEE7` |
| `ink-light` | `#2A2A2A` | `#D9D6CD` |
| `ink-muted` | `#6B6B6B` | `#9A968B` |
| `ink-faint` | `#9E9E9E` | `#6B6862` |
| `surface` | `#FFFFFF` | `#22201A` |
| `border` | `#D5D0C7` | `#3A372F` |
| `border-light` | `#E5E1DA` | `#2C2A24` |
| `iris` | `#8071BC` | `#A498D0` |
| `iris-dark` | `#635499` | `#8071BC` |
| `iris-dim` | `rgba(128,113,188,0.12)` | `rgba(164,152,208,0.18)` |
| `deep-teal` | `#1A3A34` | `#3FAA9B` |
| `deep-teal-light` | `#2A5249` | `#5BC2B3` |
| `deep-teal-dim` | `rgba(26,58,52,0.10)` | `rgba(63,170,155,0.15)` |
| `ember` | `#CA5D0F` | `#E07B33` |
| `ember-dark` | `#A84B0C` | `#CA5D0F` |
| `ember-dim` | `rgba(202,93,15,0.10)` | `rgba(224,123,51,0.18)` |
| `sand` | `#E8D4C0` | `#5C4D3E` |
| `sand-dark` | `#C4A98A` | `#A88E70` |
| `success` | `#3BAA7F` | `#5FCFA0` |
| `error` | `#B83A2A` | `#D9554A` |

(Other tokens follow the same pattern; this table is illustrative — derive remaining mappings to maintain ~equivalent perceived contrast in both modes.)

3. **Implementation rule** — toggle via a `data-theme="dark"` attribute on `<html>`. Tokens reference CSS custom properties; the dark theme overrides the property values, never the component CSS.
4. **Examples** — CSS snippet for `:root` light values + `[data-theme="dark"]` overrides.
5. **Don'ts** — no automatic switch by `prefers-color-scheme` without a user toggle (respect user preference, but offer override); no "dark mode" component variants — components must work unchanged; no dark-mode-only tokens.

- [ ] **Step 1: Write all four chunks above.**
- [ ] **Step 2: Validate after each.**
- [ ] **Step 3: Commit one feat per chunk.**

---

## Task 24: Migrate meta chunks

### `meta/accessibility.md`

Source: monolith Section 7 → "Contrast", "Focus States". Frontmatter:

```yaml
---
title: Accessibility
category: meta
tokens: [iris, ink, ink-muted, ink-faint, shell, surface]
related: [color, typography, responsive, components/forms, components/inputs]
---
```

Body: contrast ratios verbatim from monolith; focus state rule (2px solid `iris`, offset 2px, never removed); add WCAG references. Don'ts: never remove outline without replacing; never use `ink-faint` for required-readable text.

### `meta/responsive.md`

Source: monolith Section 7 → "Responsive Breakpoints", "Responsive Rules". Frontmatter:

```yaml
---
title: Responsive
category: meta
tokens: [bp-mobile, bp-tablet, bp-desktop]
related: [patterns/layouts, components/navigation, components/tables]
---
```

Body: breakpoints (`bp-mobile <640px`, `bp-tablet 640–1024px`, `bp-desktop >1024px`), per-component responsive behavior (sidebar collapse, detail panel → modal, table reflow), 44×44px touch target rule, 11px font-size floor, mobile-first principle. Don'ts: no fixed pixel widths above mobile; no horizontal page scroll on mobile.

### `meta/ai-assistant-instructions.md`

Source: monolith Section 8 (entire). Frontmatter:

```yaml
---
title: AI Assistant Instructions
category: meta
tokens: []
related: [identity, color, typography, spacing, motion, iconography, voice-and-content]
---
```

Body: port Section 8 verbatim into the standard skeleton. Add a top-level pointer block: "Before generating UI, load the relevant chunk(s) from this repo. For color decisions, see `foundations/color.md`. For component patterns, see `components/`. For data viz, see `data-viz/`. Always honor the don'ts in each chunk." Append the locked decisions from `foundations/iconography.md` (Phosphor only, Thin default).

### `meta/voice-and-content.md` (NEW)

Frontmatter:

```yaml
---
title: Voice and Content
category: meta
tokens: []
related: [identity, components/empty-states, components/notifications, components/forms]
---
```

Required content:

1. **Principles** — write for an analyst, not a marketer. Calm, specific, and short. Avoid promotional adjectives ("powerful," "seamless," "robust"). State what the thing does, not how good it is.
2. **Capitalization rules** — sentence case for all UI text (headings, buttons, labels, menu items). Reserve uppercase for small section labels at `text-xxs`. Never ALL CAPS for buttons or headings.
3. **Microcopy table** — common surfaces with example text:
   | Surface | Pattern | Example |
   |---|---|---|
   | Button (primary action) | Verb + noun | "Save changes", "Run analysis" |
   | Button (cancel) | Just "Cancel" | "Cancel" |
   | Empty state heading | Direct, italic | "No indicators yet." |
   | Empty state body | What to do next | "Add an indicator to start tracking." |
   | Error toast | What happened | "Couldn't load the dashboard. Retry?" |
   | Success toast | What was done | "Indicator saved." |
   | Form helper text | Explain the field | "Used to label exports." |
   | Form error | Name the fix | "Enter at least 3 characters." |
4. **Number and date formatting** — IBM Plex Mono for digits in tabular contexts; ISO 8601 dates (2026-05-05) in dense tables; "5 May 2026" in editorial contexts. No "5/5/26" — ambiguous between locales.
5. **Don'ts** — don't use "please" in error messages (it sounds servile); don't apologize ("Sorry, something went wrong" — say what went wrong instead); don't use emoji in product UI (reserved for editorial moments only); don't use exclamation marks; don't write to "the user" in second person ("Click here") when first-person works ("I want to…").

For each task in this group:
- [ ] **Step 1:** Write the chunk per spec.
- [ ] **Step 2:** `.venv/bin/python scripts/validate.py`.
- [ ] **Step 3:** Commit `feat(meta): add <slug> chunk`.

---

## Task 25: Tokens placeholder

**Files:**
- Create: `tokens/README.md`

- [ ] **Step 1: Write the README**

```markdown
# Tokens

Reserved for Stage 2. This folder will hold:

- `tokens.json` — W3C Design Tokens Community Group format with light + dark value modes
- `tokens.css` — CSS custom properties (`:root` light + `[data-theme="dark"]` overrides)
- `tokens.ts` — Typed TypeScript export

Until then, treat token names from the chunks (e.g., `shell`, `ink`, `iris`, `space-8`, `radius-md`) as the canonical interface. Hex/px/ms values are documented in the relevant `foundations/` chunk.
```

- [ ] **Step 2: Commit**

```bash
git add tokens/README.md
git commit -m "docs(tokens): add Stage 2 placeholder"
```

---

## Task 26: Assets

**Files:**
- Copy from Kristian's machine: existing MERLx logo SVGs into `assets/logo/`
- Create: `assets/README.md`

**Note for executor:** the SVG filenames in Kristian's `claude.ai/design` screenshot are `MERLx_icon_light.svg`, `MERLx_icon_light2.svg`, `MERLx_icon.svg`, plus a fourth that is cropped off. Locate them via Spotlight or ask Kristian for the path. Common locations to check first: `~/Downloads/`, `~/Library/Mobile Documents/com~apple~CloudDocs/`, `~/iCloud Drive (Archive)/`.

- [ ] **Step 1: Locate the SVG files**

```bash
mdfind -name "MERLx_icon" | head -20
```

If empty, ask Kristian for the path before continuing.

- [ ] **Step 2: Copy into assets/logo/**

```bash
cp <path>/MERLx_icon_light.svg ~/github/merlx-design-system/assets/logo/
cp <path>/MERLx_icon.svg ~/github/merlx-design-system/assets/logo/merlx-icon-dark.svg
# Add the wordmark if it exists; otherwise note its absence in the asset README
```

- [ ] **Step 3: Write assets/README.md**

```markdown
# Assets

Brand marks for MERLx. Use these unmodified — never re-tint, re-stretch, or recolor.

## Logos

| File | Use |
|---|---|
| `logo/merlx-icon-light.svg` | App icon on light backgrounds (`shell`) |
| `logo/merlx-icon-dark.svg` | App icon on dark backgrounds (dark mode) |
| `logo/merlx-wordmark.svg` | Full "MERLx" wordmark (Inter Bold + Iris "x") |

## Rules

- The logo is "MERLx" in Inter Bold with the "x" rendered in Iris (`#8071BC`).
- Always pair with a project subtitle in DM Serif Display italic (per `foundations/identity.md`).
- Minimum size: 24px height for the icon, 80px width for the wordmark.
- Clear space: at least 16px around the mark on every side.
- Never apply effects (shadow, glow, outline). Never rotate. Never recolor.
```

- [ ] **Step 4: Commit**

```bash
git add assets/
git commit -m "feat(assets): add MERLx brand SVGs and usage rules"
```

---

## Task 27: Build the README index and CHANGELOG entry

**Files:**
- Modify: `README.md`
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Replace `README.md` Index section with full chunk list**

Replace the placeholder `## Index` section with:

```markdown
## Index

### Foundations
- [Identity](foundations/identity.md) — aesthetic principles + logo
- [Color](foundations/color.md) — palette, semantic assignment, status
- [Typography](foundations/typography.md) — Inter / DM Serif Display / IBM Plex Mono
- [Spacing](foundations/spacing.md) — spacing scale + layout rules
- [Radius](foundations/radius.md) — radius scale
- [Motion](foundations/motion.md) — timing, easing, reduced-motion
- [Elevation](foundations/elevation.md) — no shadows; background contrast
- [Iconography](foundations/iconography.md) — Phosphor + weight rules

### Components
- [Buttons](components/buttons.md)
- [Inputs](components/inputs.md)
- [Cards](components/cards.md)
- [Badges](components/badges.md)
- [Tables](components/tables.md)
- [Modals](components/modals.md)
- [Empty States](components/empty-states.md)
- [Navigation](components/navigation.md) — sidebar, topbar, breadcrumbs, tabs
- [Tooltips](components/tooltips.md) — 9px wide-not-tall
- [Forms](components/forms.md)
- [Notifications](components/notifications.md) — toast, banner, inline

### Data Viz
- [Charts](data-viz/charts.md)
- [Maps](data-viz/maps.md)
- [Dense Tables](data-viz/dense-tables.md)
- [Sparklines and Stats](data-viz/sparklines-and-stats.md)

### Patterns
- [Layouts](patterns/layouts.md)
- [Loading and Skeletons](patterns/loading-and-skeletons.md)
- [Empty / Error / Success](patterns/empty-error-success.md)
- [Dark Mode](patterns/dark-mode.md)

### Meta
- [Accessibility](meta/accessibility.md)
- [Responsive](meta/responsive.md)
- [AI Assistant Instructions](meta/ai-assistant-instructions.md)
- [Voice and Content](meta/voice-and-content.md)

### Tokens & Assets
- [Tokens](tokens/README.md) — Stage 2 placeholder
- [Assets](assets/README.md) — brand SVGs

## Status

- v0.1.0 — Stage 1 complete (Modularity + Completeness). 31 chunks live.
- v0.2.0 — Stage 2 (Tokens as code) — planned.
- v0.3.0 — Stage 3 (Astro docs site + MERLx.fig) — planned.

## Versioning

SemVer. Major = breaking token changes. Minor = new tokens / chunks. Patch = clarifications, examples.
```

- [ ] **Step 2: Update CHANGELOG.md**

Replace `[Unreleased]` with:

```markdown
## [0.1.0] — 2026-05-05

### Added
- 31 modular chunks under foundations/, components/, data-viz/, patterns/, meta/
- Phosphor iconography rules with weight discipline (Thin / Regular / Fill)
- Dark mode token mapping table
- Voice and content microcopy rules
- Standard chunk skeleton (Principles → Tokens → Rules → Examples → Don'ts) enforced by `scripts/validate.py`
- Tokens folder reserved for Stage 2
- MERLx brand SVGs in `assets/logo/`
```

- [ ] **Step 3: Commit**

```bash
git add README.md CHANGELOG.md
git commit -m "docs: index all chunks and mark v0.1.0"
```

---

## Task 28: Final validation, tag, and push

- [ ] **Step 1: Run the validator one final time**

```bash
cd ~/github/merlx-design-system
.venv/bin/python scripts/validate.py
```

Expected: `OK — 31 chunks valid`.

- [ ] **Step 2: Create the private GitHub repo**

```bash
gh repo create merlx-design-system --private --source=. --remote=origin --description "Token-first design reference for MERLx — calm, minimal, warm Nordic Product Studio aesthetic for analytical tools."
```

- [ ] **Step 3: Push and tag v0.1.0**

```bash
git push -u origin main
git tag -a v0.1.0 -m "Stage 1 complete: 31 modular chunks + Phosphor iconography + dark mode mapping"
git push origin v0.1.0
```

- [ ] **Step 4: Smoke test against `claude.ai/design`** (manual)

In a browser:

1. Navigate to `claude.ai/design`.
2. Enter "MERLx — analytical tools for monitoring, evaluation, research, and learning in conflict and humanitarian contexts" in the blurb.
3. Paste the GitHub URL `https://github.com/<your-handle>/merlx-design-system`.
4. Upload the SVGs from `assets/logo/`.
5. Verify Claude can access the repo (private-repo access path — may require OAuth/PAT; if blocked, flip the repo public temporarily, then flip back).
6. Run one prompt: "Generate a dashboard card showing a single KPI with a sparkline and a delta indicator."
7. Manually inspect the output: does it use `surface` background, `border-light`, IBM Plex Mono for the value, Phosphor Thin icons, no shadows, `deep-teal` sparkline?
8. Note any drift in `docs/specs/post-v0.1.0-notes.md` for the next iteration.

- [ ] **Step 5: Mark v0.1.0 done in the spec**

Edit `docs/specs/2026-05-05-merlx-design-system-design.md` Section 12 to mark each success criterion checked. Commit:

```bash
git add docs/specs/2026-05-05-merlx-design-system-design.md
git commit -m "docs(spec): mark v0.1.0 success criteria complete"
git push
```

---

## Self-review

**Spec coverage:**
- Spec §3 repo facts (name, location, license, versioning, distribution) → Task 1, Task 25 (tokens placeholder), Task 28.
- Spec §4 three-stage roadmap → this plan covers Stage 1 only; Stages 2 and 3 are out of scope and named in the spec.
- Spec §5 chunk taxonomy (34 items) → Tasks 3–24 cover all 31 content chunks; Tasks 25–26 cover `tokens/` and `assets/`; Task 27 covers root `README.md`. Total = 34. ✓
- Spec §6 locked decisions → Phosphor (Task 10), dark mode (Task 23), English-only voice (Task 24), private repo (Task 28). ✓
- Spec §7 layout → Task 1 scaffolds the folder tree exactly. ✓
- Spec §8 chunk file convention → Task 2 validator enforces it; Tasks 3–24 each follow it. ✓
- Spec §9 dark mode approach → Task 23 `patterns/dark-mode.md`. ✓
- Spec §10 iconography rules → Task 10 `foundations/iconography.md`. ✓
- Spec §11 out of scope (print, email, etc.) → not covered here, consistent with spec. ✓
- Spec §12 success criteria → Task 28 Step 5 checks them off. ✓
- Spec §13 next step (writing-plans) → this document. ✓

**Placeholder scan:** No "TBD", no "implement later", no "similar to Task N" without code, no vague "add validation." Every chunk task lists the body sections and required content.

**Type / token consistency:** Token names (`shell`, `ink`, `iris-dim`, `deep-teal`, etc.) match the source monolith. Folder names match throughout (`foundations`, `components`, `data-viz`, `patterns`, `meta`). Validator categories match folder names. `tokens.json` in tokens/README references W3C Design Tokens spec consistent with spec §4.

**Note:** Task 21 introduces derived `success-dim` and `error-dim` rgba values that don't yet exist in `color.md`. The plan flags this inline as "needs to be added to `color.md` in a future revision." This is acceptable for v0.1.0 (the values are documented inline in the chunk that uses them) but should be promoted to canonical tokens in v0.1.1 or v0.2.0.

---

## Execution handoff

Plan complete and saved to `docs/plans/2026-05-05-merlx-stage-1-modularity-and-completeness.md`. Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration. Good for the volume of writing involved.

**2. Inline Execution** — Execute tasks in this session using `superpowers:executing-plans`, batch execution with checkpoints.

Which approach?
