---
title: Dense Tables
category: data-viz
tokens: [border-light, shell-warm, ink, ink-muted, deep-teal, deep-teal-dim, ember-dim, success, error, text-micro, text-xs, space-2, space-4]
related: [tables, typography, spacing]
---

# Dense Tables

## Principles

Dense tables — used in PRISM, ToC Tester, OASIS, and similar analytical surfaces — pack maximum information per row while remaining scannable. Row height is tighter, headers are sticky, conditional formatting is allowed (within the dim-accent palette), and IBM Plex Mono is the dominant font for cell values.

## Tokens / Values

| Property | Value |
|---|---|
| Row height | 28px |
| Numeric font | IBM Plex Mono `text-micro` |
| Text-cell font | Inter 400, `text-xs` |
| Header font | Inter 600, `text-xs`, uppercase, `ink-muted`, letter-spacing 1px |
| Cell padding | `space-2` vertical, `space-4` horizontal |
| Row separator | `border-light`, 1px solid (between rows only) |
| Sticky header | yes (top) |
| Sticky first column | optional (configurable per table) |
| Numeric alignment | right |
| Unit suffix color | `ink-muted`, separated by a hair-space |
| Sortable header indicator | Phosphor `caret-up` / `caret-down` Regular 10px in `ink-muted` (active sort: `ink`) |
| Row selection | 1px left-edge `deep-teal` accent + `deep-teal-dim` background |

### Conditional formatting (cell background)

| Meaning | Background |
|---|---|
| Above warning threshold | `ember-dim` |
| Critical / over hard threshold | `rgba(184, 58, 42, 0.12)` (error-dim, derived) |
| Positive milestone | `rgba(59, 170, 127, 0.12)` (success-dim, derived) |
| Selected row | `deep-teal-dim` |

(See note in `notifications.md` — `error-dim` and `success-dim` will be promoted to canonical tokens in a future patch.)

## Semantic Assignment Rules

- **Numeric cells use IBM Plex Mono.** Always. Including counts, percentages, currency, dates in ISO format.
- **Text cells use Inter.** Identifiers, names, labels.
- **Right-align numeric columns.** Including units. The unit suffix sits in `ink-muted`, separated from the value by a thin space.
- **Conditional formatting uses dim variants only.** Never use full accent colors as cell backgrounds — too aggressive at table density.
- **Row hover does not obscure conditional formatting.** Use a 1px left-edge `deep-teal` indicator instead of a full background tint.
- **Sticky the header at scroll boundaries.** Optionally sticky the first column for wide tables.
- **Sortable headers** display a Regular caret next to the label. The active sort caret is `ink`; inactive carets are `ink-muted`.

## Examples

A dense indicator monitoring grid:

```html
<table class="dense-table">
  <thead>
    <tr>
      <th>Indicator</th>
      <th class="numeric">Target</th>
      <th class="numeric">Current</th>
      <th class="numeric">Δ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HH food security</td>
      <td class="numeric mono">75 %</td>
      <td class="numeric mono">62 %</td>
      <td class="numeric mono cell-warning">−13 %</td>
    </tr>
  </tbody>
</table>
```

```css
.dense-table { width: 100%; border-collapse: collapse; }
.dense-table thead th {
  position: sticky; top: 0;
  background: var(--surface);
  font: 600 var(--text-xs) Inter, system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--ink-muted);
  text-align: left;
  padding: var(--space-2) var(--space-4);
  border-bottom: 1px solid var(--border-light);
}
.dense-table td {
  padding: var(--space-2) var(--space-4);
  border-bottom: 1px solid var(--border-light);
  height: 28px;
}
.dense-table td.numeric { text-align: right; }
.dense-table td.mono { font-family: "IBM Plex Mono", monospace; font-size: var(--text-micro); }
.dense-table td.cell-warning { background: var(--ember-dim); }
.dense-table tr[aria-selected="true"] td:first-child { box-shadow: inset 1px 0 0 var(--deep-teal); }
.dense-table tr[aria-selected="true"] td { background: var(--deep-teal-dim); }
```

## Don'ts

- Don't use zebra striping. `border-light` row separators are sufficient.
- Don't use full accent colors as cell backgrounds — dim variants only.
- Don't apply full-row hover backgrounds that obscure conditional formatting.
- Don't render inline-editable cells without an explicit edit affordance (icon button).
- Don't drop below 28px row height — it becomes unreadable.
- Don't use Inter for numeric columns.
