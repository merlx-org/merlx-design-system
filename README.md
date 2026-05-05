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

## License

MIT — see `LICENSE`.
