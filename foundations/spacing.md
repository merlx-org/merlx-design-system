---
title: Spacing
category: foundations
tokens: [space-1, space-2, space-3, space-4, space-5, space-6, space-7, space-8, space-10, space-12]
related: [radius, layouts, responsive]
---

# Spacing

## Principles

Tighter is better than looser. Pick from the spacing scale; if a value feels between two tokens, take the smaller one. Custom px values are not allowed.

## Tokens / Values

| Token | Value | Use |
|-------|-------|-----|
| `space-1` | 2px | Inline gaps, icon-to-text |
| `space-2` | 4px | Tight padding (badges, pills) |
| `space-3` | 6px | Small element gaps |
| `space-4` | 8px | Default inner padding, compact gaps |
| `space-5` | 10px | Element-to-element spacing |
| `space-6` | 12px | Section inner padding |
| `space-7` | 14px | Comfortable card padding |
| `space-8` | 16px | Standard card / panel padding |
| `space-10` | 20px | Major layout gaps, section spacing |
| `space-12` | 24px | Page-level padding, large gaps |

## Semantic Assignment Rules

- **Card padding** — `space-7` (14px) to `space-8` (16px). Never less than `space-4`.
- **Page padding** — `space-10` (20px) to `space-12` (24px).
- **Dense grid gaps** — `space-5` (10px).
- **Comfortable grid gaps** — `space-10` (20px).
- **Sidebar widths** — 200–240px for navigation, 300–360px for detail panels.
- **Content area** — always fluid (`1fr` or `flex-grow`).
- **Scrollable regions** — set `max-height` with `overflow-y: auto`. Always pair with `space-4` or larger bottom-padding so content doesn't clip against the edge.

## Examples

A standard card:

```css
.card {
  padding: var(--space-8);
}
```

A dense data grid:

```css
.grid-dense {
  display: grid;
  gap: var(--space-5);
}
```

A page container:

```css
.page {
  padding: var(--space-12);
}
```

## Don'ts

- Don't pick custom px values — always use a token.
- Don't use `space-1` or `space-2` for component padding (reserved for inline gaps and badges).
- Don't go below `space-4` inside a card.
- Don't pad scrollable regions only at the top — the bottom needs equivalent padding.
