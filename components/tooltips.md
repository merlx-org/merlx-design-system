---
title: Tooltips
category: components
tokens: [ink, surface, text-micro, radius-sm, motion-fast, space-2, space-4]
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

- **Trigger on hover and focus** — never click.
- **Position above the trigger by default**; flip to below if it would clip the viewport.
- **Single line where possible.** If it wraps, prefer a wider tooltip over a taller one.
- **Always reset `text-transform: none`** even on triggers that inherit `uppercase` (e.g., section labels in the sidebar).
- **Never put interactive elements** (links, buttons, form fields) inside a tooltip — that is a popover, not a tooltip.

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
  opacity: 0;
  transition: opacity var(--motion-fast) ease-out;
}
.tooltip[data-open="true"] { opacity: 1; }
```

A tooltip explaining a truncated cell value:

```html
<span class="cell" data-tooltip="Operationalised under indicator IND-204">
  IND-204…
</span>
```

## Don'ts

- Don't size tooltips at `text-xxs` or larger — 9px is the rule.
- Don't make tooltips tall and narrow.
- Don't inherit uppercase from the trigger — always explicitly reset.
- Don't put links, buttons, or form fields inside a tooltip.
- Don't show a tooltip on tap on touch devices; provide an inline help icon instead.
