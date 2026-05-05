---
title: Responsive
category: meta
tokens: [bp-mobile, bp-tablet, bp-desktop]
related: [layouts, navigation, tables]
---

# Responsive

## Principles

Mobile-first: start with a single column and add complexity at wider breakpoints. Tokens for breakpoints carry semantic names (`bp-mobile`, `bp-tablet`, `bp-desktop`) so component CSS does not hard-code pixel values.

## Tokens / Values

| Token | Width | Behavior |
|---|---|---|
| `bp-mobile` | < 640px | Single column. Sidebars collapse to drawers. |
| `bp-tablet` | 640–1024px | Two columns. Detail panel becomes modal or bottom sheet. |
| `bp-desktop` | > 1024px | Full layout — sidebar + content + detail panel. |

## Semantic Assignment Rules

- **Mobile-first** — base styles target mobile; media queries add complexity at wider breakpoints.
- **Sidebars** collapse to a hamburger or drawer below `bp-tablet`.
- **Detail panes** convert to a full-screen modal or bottom sheet below `bp-tablet`.
- **Tables** scroll horizontally on mobile, or reflow into stacked card rows. Pick reflow when the data is < 5 columns; pick scroll when columns are integral (e.g., dense-tables).
- **Font sizes** never scale below `text-xs` (11px) on any breakpoint.
- **Touch targets** are 44 × 44px minimum on mobile.
- **Page padding** scales: `space-8` (16px) at mobile, `space-10` (20px) at tablet, `space-12` (24px) at desktop.

## Examples

Layout breakpoint behavior (using `clamp` for fluid padding):

```css
.page {
  padding: clamp(var(--space-8), 4vw, var(--space-12));
}

@media (max-width: 1024px) {
  .layout-three-pane {
    grid-template-columns: 1fr;
  }
  .detail-pane { display: none; }
  .detail-pane[data-open="true"] { display: block; position: fixed; inset: 0; }
}

@media (max-width: 640px) {
  .sidebar { display: none; }
  .sidebar[data-open="true"] { position: fixed; inset: 0; }
}
```

A reflowing table:

```css
@media (max-width: 640px) {
  .table-reflow thead { display: none; }
  .table-reflow tr {
    display: block;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: var(--space-4);
    margin-bottom: var(--space-4);
  }
  .table-reflow td {
    display: flex;
    justify-content: space-between;
    border: none;
    padding: var(--space-1) 0;
  }
  .table-reflow td::before {
    content: attr(data-label);
    color: var(--ink-muted);
    font-weight: 500;
  }
}
```

## Don'ts

- Don't hard-code breakpoint pixel values in component CSS — reference the breakpoint tokens via media queries.
- Don't use fixed widths above mobile (use `1fr`, `clamp()`, or `max-width`).
- Don't shrink font sizes below `text-xs` on any breakpoint.
- Don't introduce a fourth breakpoint — three is the rule.
- Don't allow horizontal page scroll on mobile.
- Don't show desktop-only navigation chrome (large sidebars, multi-column dashboards) on mobile.
