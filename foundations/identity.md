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
