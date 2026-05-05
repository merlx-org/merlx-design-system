---
title: Elevation
category: foundations
tokens: [shell, shell-warm, shell-cool, surface, border, border-light]
related: [identity, color, cards, modals]
---

# Elevation

## Principles

MERLx does not use shadows. Elevation is communicated through background contrast — a `surface` card on a `shell` page reads as "above" without a single pixel of blur. This is a hard rule from the identity layer: data clarity over decoration.

## Tokens / Values

| Layer | Background | Border | Use |
|---|---|---|---|
| Page | `shell` | — | Default page background |
| Section offset | `shell-warm` | — | Sidebars, secondary surfaces, hover backgrounds |
| Card | `surface` (#FFFFFF) | `border-light`, 1px | Standard card on a `shell` page |
| Modal | `surface` | `border`, 1px | Modal / drawer over a `rgba(17, 17, 17, 0.4)` overlay |
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

A modal overlay:

```css
.modal-overlay { background: rgba(17, 17, 17, 0.4); }
.modal-panel {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
}
```

## Don'ts

- Don't use `box-shadow` for any elevation cue, ever.
- Don't use `filter: drop-shadow()` as a workaround.
- Don't stack three or more contrast layers; two is enough (page + surface, or page + sidebar).
- Don't add a border AND a darker background to communicate elevation — pick one.
