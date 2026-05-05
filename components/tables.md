---
title: Tables
category: components
tokens: [border-light, ink-muted, shell-warm, text-micro, text-xs, space-2, space-4]
related: [dense-tables, typography, spacing]
---

# Tables

## Principles

A table renders structured data row-by-row. Component-level tables (this chunk) cover everyday use — settings lists, simple data grids, comparison views. Analytical-grade tables (KII coding ledgers, indicator monitoring grids) live in `data-viz/dense-tables.md`.

## Tokens / Values

| Property | Value |
|---|---|
| Cell font | IBM Plex Mono `text-micro` to `text-xs` for numeric, Inter 400 `text-xs` for text |
| Header font | Inter 600, `text-xs`, uppercase, `ink-muted`, letter-spacing 1px |
| Row border | `border-light`, 1px solid (between rows only) |
| Row hover | `shell-warm` background |
| Cell padding | `space-2` vertical, `space-4` horizontal |
| Numeric alignment | right |

## Semantic Assignment Rules

- **Headers are uppercase, body cells are not.** Headers are the only uppercase text in this design system; body cells stay sentence case.
- **Right-align numeric columns.** Always. Including currency, percentages, and counts.
- **Left-align text columns.** Including identifiers and short codes.
- **No vertical borders.** Horizontal `border-light` only — vertical separators add noise.
- **Single header row.** No grouped headers in component-level tables (use `dense-tables.md` if you need them).

## Examples

A standard component-level table:

```html
<table class="table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Created</th>
      <th class="numeric">Records</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Aperture</td>
      <td class="mono">2026-04-12</td>
      <td class="numeric mono">1,204</td>
    </tr>
  </tbody>
</table>
```

```css
.table { width: 100%; border-collapse: collapse; }
.table th {
  font: 600 var(--text-xs) Inter, system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--ink-muted);
  text-align: left;
  padding: var(--space-2) var(--space-4);
  border-bottom: 1px solid var(--border-light);
}
.table td {
  font: 400 var(--text-xs) Inter, system-ui, sans-serif;
  padding: var(--space-2) var(--space-4);
  border-bottom: 1px solid var(--border-light);
}
.table td.numeric { text-align: right; }
.table td.mono { font-family: "IBM Plex Mono", monospace; }
.table tbody tr:hover { background: var(--shell-warm); }
```

## Don'ts

- Don't use zebra striping. `border-light` row separators are sufficient.
- Don't add vertical borders.
- Don't uppercase body cells — only headers.
- Don't use Inter for numeric columns — IBM Plex Mono is the rule.
- Don't render component-level tables denser than `space-2` vertical padding (28px row height); switch to `dense-tables.md` patterns instead.
