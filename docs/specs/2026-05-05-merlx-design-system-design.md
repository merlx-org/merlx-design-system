# MERLx Design System Repo — Design

**Date:** 2026-05-05
**Author:** Kristian Svendsen (with Claude)
**Status:** Approved (pending user spec review)

---

## 1. Goal

Evolve the existing 343-line `~/.claude/design-systems/MERLx-design-system.md` into a public GitHub repository optimized for consumption by `claude.ai/design`, Claude Skills, human contributors, and (later) a rendered docs site and a Figma file.

The current file is solid as a token-first reference but is monolithic, has known content gaps (dark mode, data viz, forms, iconography, voice, etc.), and is not directly consumable by tools that expect topic-sized chunks or a structured repo.

## 2. Non-goals

- Not building per-product (Aperture, OASIS, PRISM, ToC Tester, GestoraX) sub-brand systems in this repo. Those are deferred.
- Not building print stylesheets, email templates, i18n/RTL, or data-density modes. Deferred.
- Not replacing RIKO or CMC design systems. MERLx-only.
- Not English-and-Danish. English-only voice guidance.

## 3. Repo

- **Name:** `merlx-design-system`
- **Location:** `~/github/merlx-design-system`, private on GitHub under Kristian's account
- **License:** MIT (still applied — license file is for if/when the repo is later flipped public)
- **Access for `claude.ai/design`:** Private repos may require granting Claude access via GitHub OAuth or a deploy-key/PAT mechanism. Verify access path before relying on it; fallback is to flip the repo public at submission time or attach a zipped snapshot.
- **Versioning:** SemVer. Major = breaking token changes. Minor = new tokens / chunks. Patch = clarifications, examples. Tagged releases so `claude.ai/design` can pin a version.
- **Distribution targets:**
  - `claude.ai/design` consumes: GitHub URL + (Stage 3) `MERLx.fig` + asset SVGs + one-line blurb
  - Claude Skills: same repo, frontmatter maps tasks → chunks
  - Human consumers: GitHub-rendered Markdown today, Astro site after Stage 3

## 4. Three-stage roadmap

### Stage 1 — Modularity + Completeness (parallel)

Split the existing monolith into 34 topic-sized chunks following the locked taxonomy (Section 5). Fill content gaps as the chunks are created. Stage 1 produces a usable v0.1.0.

### Stage 2 — Tokens as code

Export tokens to:

- `tokens/tokens.json` — W3C Design Tokens Community Group format
- `tokens/tokens.css` — CSS custom properties
- `tokens/tokens.ts` — Typed TypeScript export

Single source of truth: the Markdown chunks reference token names; the code consumes the exports. Projects can `import` tokens directly instead of re-typing hex values.

### Stage 3 — Showability

Two outputs:

- **Astro static docs site** — markdown-native, zero-JS by default, matches MERLx's "calm" aesthetic. Reads from the same `.md` chunks; renders swatches, type specimens, component demos.
- **`MERLx.fig`** — built from scratch using the rendered site as visual reference. Becomes the canonical visual companion for `claude.ai/design`.

Stage 3 is sequenced *after* Stage 1 so the docs site has chunks to render.

## 5. Chunk taxonomy (34 chunks, locked)

### Foundations (8)

1. `foundations/identity.md` — aesthetic principles, logo rules, voice/tone summary
2. `foundations/color.md` — full palette, semantic assignment, dim variants, status
3. `foundations/typography.md` — font stack, scale, letter-spacing, usage rules
4. `foundations/spacing.md` — spacing scale, layout rules, sidebar/page padding
5. `foundations/radius.md` — radius scale + when to use which
6. `foundations/motion.md` — timing scale, easing, reduced-motion rules
7. `foundations/elevation.md` *(new)* — explicit "no shadows; use background contrast" rules with examples
8. `foundations/iconography.md` *(new)* — Phosphor library, weight rules (Thin default, Regular sub-16px, Fill for emphasis)

### Components (11)

9. `components/buttons.md`
10. `components/inputs.md` — text, textarea, select, checkbox, radio, switch, search
11. `components/cards.md`
12. `components/badges.md`
13. `components/tables.md`
14. `components/modals.md` — merges drawers + dialogs
15. `components/empty-states.md`
16. `components/navigation.md` — sidebar + topbar + breadcrumbs + tabs
17. `components/tooltips.md` *(new)* — 9px sizing rule from existing feedback memory
18. `components/forms.md` *(new)* — validation, error display, helper text, fieldsets
19. `components/notifications.md` *(new)* — toasts, banners, inline alerts

### Data viz (4)

20. `data-viz/charts.md` *(new)* — bar, line, area, stacked; colors, axes, gridlines
21. `data-viz/maps.md` *(new)* — choropleth, point, heatmap palettes
22. `data-viz/dense-tables.md` *(split out)* — analytical-grade tables
23. `data-viz/sparklines-and-stats.md` *(new)* — KPI tiles, deltas, micro-charts

### Patterns (4)

24. `patterns/layouts.md` *(new)* — three-pane, full-bleed, dashboard grid, document reader
25. `patterns/loading-and-skeletons.md` *(new)*
26. `patterns/empty-error-success.md` *(new)* — three states every async surface needs
27. `patterns/dark-mode.md` *(new)* — semantic token re-mappings, not a parallel palette

### Meta (7, including folders)

28. `meta/accessibility.md` — contrast, focus, responsive
29. `meta/responsive.md` — breakpoints + per-component responsive behavior
30. `meta/ai-assistant-instructions.md` — how to use this system when generating UI
31. `meta/voice-and-content.md` *(new)* — microcopy, capitalization, error messages, empty-state phrasing
32. `tokens/` — `tokens.json`, `tokens.css`, `tokens.ts`, `README.md`
33. `assets/` — logo SVGs, favicon, brand marks, `README.md`
34. `README.md` (repo root) — index, how to consume, license, versioning

## 6. Locked decisions

| Decision | Value |
|---|---|
| Stage order | Modularity + Completeness in parallel, then Tokens-as-code, then Showability |
| Repo shape | Public Markdown + `tokens/` + `assets/` |
| Dark mode | In scope (Stage 1, `patterns/dark-mode.md`) |
| Iconography library | Phosphor (MIT, multi-weight) |
| Iconography weights | Thin (default 16–20px), Regular (sub-16px), Fill (state emphasis); Light/Bold/Duotone forbidden |
| Voice | English-only |
| Sub-brand systems | Out of scope |
| Print / email / i18n / data-density | Out of scope |

## 7. Repo layout

```
merlx-design-system/
├── README.md                    # Index, how to consume, license
├── CHANGELOG.md                 # SemVer-tracked design changes
├── LICENSE                      # MIT
├── foundations/
│   ├── identity.md
│   ├── color.md
│   ├── typography.md
│   ├── spacing.md
│   ├── radius.md
│   ├── motion.md
│   ├── elevation.md
│   └── iconography.md
├── components/
│   ├── buttons.md
│   ├── inputs.md
│   ├── cards.md
│   ├── badges.md
│   ├── tables.md
│   ├── modals.md
│   ├── empty-states.md
│   ├── navigation.md
│   ├── tooltips.md
│   ├── forms.md
│   └── notifications.md
├── data-viz/
│   ├── charts.md
│   ├── maps.md
│   ├── dense-tables.md
│   └── sparklines-and-stats.md
├── patterns/
│   ├── layouts.md
│   ├── loading-and-skeletons.md
│   ├── empty-error-success.md
│   └── dark-mode.md
├── meta/
│   ├── accessibility.md
│   ├── responsive.md
│   ├── ai-assistant-instructions.md
│   └── voice-and-content.md
├── tokens/
│   ├── tokens.json              # W3C Design Tokens spec
│   ├── tokens.css               # CSS custom properties
│   ├── tokens.ts                # Typed TS export
│   └── README.md
└── assets/
    ├── logo/
    │   ├── merlx-icon-light.svg
    │   ├── merlx-icon-dark.svg
    │   └── merlx-wordmark.svg
    └── README.md
```

## 8. Chunk file convention

Every Markdown chunk opens with frontmatter for AI consumption:

```yaml
---
title: Color
category: foundations
tokens: [shell, ink, iris, ember, deep-teal, ...]
related: [identity, dark-mode, accessibility]
---
```

Body skeleton, applied to every chunk for predictability:

1. **Principles** — one short paragraph on the philosophy of this surface
2. **Tokens / values** — table of tokens with hex/px/ms values and one-line usage notes
3. **Semantic assignment rules** — when to use which token (the "why")
4. **Examples** — code-fence snippets and short visual references
5. **Don'ts** — the negative space (what not to do)

## 9. Dark mode approach

Single canonical palette in `foundations/color.md`. Dark mode defined in `patterns/dark-mode.md` as semantic-token re-mappings (e.g., `surface` becomes `#1A1A1A`), not a parallel palette. Tokens carry semantic names (`surface`, `ink`, `border`) so components don't change between modes — only the token values flip per theme.

This means Stage 2's `tokens.json` carries `light` and `dark` value sets per token, not duplicated tokens. The W3C Design Tokens format supports this natively via `$value` modes.

## 10. Iconography rules (canonical for `foundations/iconography.md`)

| Context | Weight | Size |
|---|---|---|
| Default UI (buttons, navigation, cards) | Thin | 16–20px |
| Editorial / hero / empty states | Thin | 24–32px |
| Dense tables, badges, sub-16px contexts | Regular (1.5px) | 12–14px |
| Active / selected / emphasis state | Fill | match outline size |
| Forbidden | Light, Bold, Duotone | — |

Color: icons take their parent's text color via `currentColor`. Never hard-code icon colors except in semantic contexts (e.g., a Fill icon for "error" gets `error` token).

## 11. Out of scope (deferred, not deleted)

Each of these may become a future minor release:

- Print stylesheets / PDF export rules
- Transactional email templates
- Data-density modes (comfortable / dense / compact)
- i18n / RTL / partner-language handling (Arabic for Sudan, Somali, etc.)
- Sub-brand systems for Aperture, OASIS, PRISM, ToC Tester, GestoraX

## 12. Success criteria for v0.1.0 (end of Stage 1)

- [x] All 34 items in the taxonomy exist (31 content chunks + `tokens/README.md` + `assets/README.md` + repo `README.md`) with frontmatter and the standard body skeleton on the 31 chunks
- [x] Every chunk references tokens by name, never raw hex
- [x] Dark-mode token mappings drafted in `patterns/dark-mode.md`
- [x] Iconography rules locked in `foundations/iconography.md`
- [x] `README.md` indexes all chunks with one-line descriptions
- [x] Repo is private on GitHub at `https://github.com/KSvend/merlx-design-system`, tagged `v0.1.0`
- [ ] `claude.ai/design` accepts the repo URL and produces UI that matches MERLx visual language in a smoke test — **deferred to manual verification by Kristian**; private-repo access path may require granting Claude OAuth access or a fallback to flipping the repo public at submission time

## 13. Next step

After spec review and approval, invoke `superpowers:writing-plans` to break Stage 1 into a sequenced, reviewable implementation plan. Stages 2 and 3 each get their own spec + plan cycle when their turn comes.
