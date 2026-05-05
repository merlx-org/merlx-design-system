---
title: Badges
category: components
tokens: [radius-pill, text-xxs, text-xs, iris-dim, iris-dark, sand-dim, sand-dark, ember-dim, ember-dark, deep-teal-dim, deep-teal, deep-iris-dim, deep-iris]
related: [color, radius, typography]
---

# Badges

## Principles

A badge is a small, semantic label — a category, a status, a count. It uses the dim accent variant as its background with the full accent as text color, producing low-contrast pills that read as labels rather than buttons.

## Tokens / Values

| Property | Value |
|---|---|
| Radius | `radius-pill` (100px) |
| Padding | `space-2` vertical, `space-3` horizontal (tight) |
| Font | Inter 500–600, `text-xxs` (10px) to `text-xs` (11px) |
| Letter spacing | `0.04em` (default) — never uppercase |
| Border | none |

### Background / text pairings

| Meaning | Background | Text |
|---|---|---|
| Brand / interactive | `iris-dim` | `iris-dark` |
| Warm / highlight | `sand-dim` | `sand-dark` |
| Warning / attention | `ember-dim` | `ember-dark` |
| Primary / strong | `deep-teal-dim` | `deep-teal` |
| Secondary | `deep-iris-dim` | `deep-iris` |

## Semantic Assignment Rules

- **Pick the pairing by meaning, not by visual appeal.** A "warning" badge uses `ember-dim` + `ember-dark`, never `iris-dim`.
- **Stay sentence case.** Never uppercase a badge label.
- **Keep labels short** — 1–2 words. If a badge needs more, it's not a badge; it's a chip or a tag with content.
- **Pair badges with a leading icon** only when the icon carries semantic meaning (e.g., a Phosphor `warning-circle` Fill 12px on warning badges). Otherwise text-only.

## Examples

A brand badge:

```css
.badge-brand {
  background: var(--iris-dim);
  color: var(--iris-dark);
  border-radius: var(--radius-pill);
  padding: var(--space-2) var(--space-3);
  font: 500 var(--text-xxs) Inter, system-ui, sans-serif;
}
```

A warning badge with icon:

```html
<span class="badge-warn">
  <WarningCircle size={12} weight="fill" />
  Late
</span>
```

## Don'ts

- Don't use full accent colors as the badge background — always use the dim variant.
- Don't use ALL CAPS.
- Don't make badges interactive (use a button or chip).
- Don't fit more than 2 words inside a badge.
- Don't introduce a badge color outside the listed pairings.
