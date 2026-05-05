---
title: AI Assistant Instructions
category: meta
tokens: []
related: [identity, color, typography, spacing, motion, iconography, voice-and-content]
---

# AI Assistant Instructions

## Principles

This chunk is the entry point for AI coding assistants generating MERLx UI. Before writing any UI code, load the relevant chunks from this repo. Never improvise tokens, fonts, or motion values.

## Tokens / Values

No tokens — this chunk is procedural guidance.

## Semantic Assignment Rules

### Setup

- Load fonts: Inter (variable or 300–800), DM Serif Display (regular + italic), IBM Plex Mono (400–600).
- Set `<body>` background to `shell` (`#F5F3EE`), color to `ink` (`#111111`), font to Inter 400 at `text-base` (13px).
- Define all color, spacing, radius, and motion tokens as CSS custom properties in `:root`. Reference tokens by name in component code; never raw hex / px / ms values.

### Decision-making

- **Color** — check `foundations/color.md` semantic assignment rules first. Use `ink` variants for text and `shell` variants for backgrounds. Reach for accent colors only when encoding meaning.
- **Typography** — `foundations/typography.md`. Inter is the default. Use DM Serif Display only for editorial moments; IBM Plex Mono only for tabular / data text.
- **Spacing** — `foundations/spacing.md`. Pick from the scale; if a value feels between two tokens, use the smaller one.
- **Motion** — `foundations/motion.md`. Use the default transition. When uncertain, no animation is better than wrong animation.
- **Icons** — `foundations/iconography.md`. Phosphor Thin at 16–20px is the default. Drop to Regular only sub-16px. Use Fill only for state contrast.
- **New component** — check `components/` for a similar pattern first. Match its tokens. If nothing fits, follow the same principles: `surface` background, `border-light` edges, `radius-md`, Inter font.
- **Data viz** — `data-viz/` chunks define chart, map, dense-table, and stat-tile rules. Categorical color order is fixed: `deep-teal`, `ember`, `iris`, `sand-dark`, `deep-iris`.
- **Voice** — `meta/voice-and-content.md`. Sentence case, no exclamation marks, no "please" in errors.

### Don'ts

- Don't use colors not in this palette. No `#333`, no `gray-500`, no `blue-600`.
- Don't use `box-shadow` for elevation. Use background contrast (see `foundations/elevation.md`).
- Don't combine more than two font families in one component.
- Don't introduce a second icon library — Phosphor only.
- Don't add decorative elements: gradients, background patterns, ornamental dividers.
- Don't use ALL CAPS for buttons or headings. Reserve uppercase for small section labels at `text-xxs`.
- Don't animate on page load.
- Don't go below 9px font size for any text, or 11px for readable content.

### Project customization

Each project built on MERLx may need project-specific tokens (country colors, classification categories). Define these as extensions:

- Add a `project-specific tokens` section in the project's own CSS or config.
- Draw from the accent palette when assigning project-specific meaning. Don't invent new hues.
- If more than 5 categorical colors are needed, derive lighter / darker variants of existing accents using opacity or HSL — don't add new base colors.

## Examples

A pre-flight checklist before generating UI:

1. Read `foundations/identity.md` to anchor the aesthetic.
2. Read the most relevant component or pattern chunk for the surface you're building.
3. Pull the token list from that chunk's frontmatter and load only those tokens.
4. Pull cross-references from the `related:` field for any adjacent chunks.
5. Generate UI using only tokens, never raw values.

## Don'ts

(Captured in the Semantic Assignment Rules section above.)
