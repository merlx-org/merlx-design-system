---
title: Cards
category: components
tokens: [surface, border-light, radius-md, space-7, space-8]
related: [elevation, radius, spacing]
---

# Cards

## Principles

A card is the standard surface for grouping related content. It sits on the page background with subtle border-light separation and no shadow. Elevation is communicated through background contrast, not blur.

## Tokens / Values

| Property | Token / Value |
|---|---|
| Background | `surface` (#FFFFFF) |
| Border | `border-light`, 1px solid |
| Radius | `radius-md` (8px) |
| Padding | `space-7` (14px) to `space-8` (16px) |
| Box-shadow | none |

## Semantic Assignment Rules

- A card always sits on a `shell` or `shell-warm` background — never on another `surface`.
- Use `space-7` for compact dashboard cards, `space-8` for content-heavy cards.
- Cards do not raise on hover. Hover may swap the border to `border` (slightly darker) or tint the background `shell-cool`, but never adds a shadow.
- A card may contain a header, a body, and an optional footer — separated by 1px `border-light` dividers, not whitespace alone.

## Examples

A standard card:

```css
.card {
  background: var(--surface);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--space-8);
}
```

A compact dashboard tile:

```css
.tile {
  background: var(--surface);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--space-7);
}
```

## Don'ts

- Don't use `box-shadow` on cards.
- Don't nest a card inside another card.
- Don't use `radius-pill` or `radius-xl` for cards — `radius-md` is the rule.
- Don't pad below `space-4`.
- Don't communicate hover with a shadow or scale; use background or border tint.
