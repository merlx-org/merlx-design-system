---
title: Typography
category: foundations
tokens: [text-xl, text-lg, text-base, text-sm, text-xs, text-xxs, text-micro]
related: [identity, voice-and-content, accessibility]
---

# Typography

## Principles

Three families, three jobs. Inter for UI. DM Serif Display for editorial moments. IBM Plex Mono for data. Roles do not cross. A component uses Inter plus *at most one* of the other two — never all three.

## Tokens / Values

### Font stack

| Role | Family | Fallback | Weights | Use for |
|------|--------|----------|---------|---------|
| **UI** | Inter | system-ui, sans-serif | 300, 400, 500, 600, 700, 800 | All interface text — headings, body, labels, buttons |
| **Display** | DM Serif Display | Georgia, serif | 400, 400 italic | Editorial moments — subtitles, callouts, empty states, feature names |
| **Data** | IBM Plex Mono | JetBrains Mono, monospace | 400, 500, 600 | Numbers, timestamps, code, IDs, metrics |

### Sizing scale

| Token | Size | Use |
|-------|------|-----|
| `text-xl` | 16px | Page titles, logo |
| `text-lg` | 15px | Section headings, display subtitles |
| `text-base` | 13px | Body text, default UI |
| `text-sm` | 12px | Secondary text, descriptions |
| `text-xs` | 11px | Labels, captions, metadata |
| `text-xxs` | 10px | Badges, timestamps |
| `text-micro` | 9px | Mono data labels, dense tables, tooltips |

### Letter spacing

| Context | Value |
|---------|-------|
| Headings (Inter 600+) | `-0.2px` to `-0.3px` (tighten) |
| Body text | `0.04em` (default) |
| Uppercase labels | `0.5px` to `2px` (loosen) |
| Mono data | `0.5px` |

## Semantic Assignment Rules

- **Headings** — Inter 600–700, `text-xl` to `text-lg`, tightened letter-spacing.
- **Body** — Inter 400–500, `text-base`, default spacing.
- **Labels and metadata** — Inter 500–600, `text-xs` to `text-xxs`, `ink-muted`.
- **Display (editorial)** — DM Serif Display, regular or italic, only for an editorial moment (subtitle, callout, empty-state heading, feature name). Never body, never buttons, never labels. Italic preferred.
- **Mono (data)** — IBM Plex Mono, only for tabular alignment of numbers, dates, percentages, IDs. Never headings, never prose.

## Examples

A heading:

```html
<h2 class="heading">Indicator monitoring</h2>
```
```css
.heading {
  font-family: Inter, system-ui, sans-serif;
  font-weight: 600;
  font-size: var(--text-lg);
  letter-spacing: -0.2px;
}
```

A body paragraph:

```css
.body {
  font-family: Inter, system-ui, sans-serif;
  font-weight: 400;
  font-size: var(--text-base);
  letter-spacing: 0.04em;
  color: var(--ink);
}
```

A data cell in IBM Plex Mono:

```css
.cell-numeric {
  font-family: "IBM Plex Mono", monospace;
  font-weight: 400;
  font-size: var(--text-micro);
  color: var(--ink);
}
```

## Don'ts

- Don't combine all three families in one component. Inter + at most one of DM Serif Display or IBM Plex Mono.
- Don't use DM Serif Display for body, buttons, or labels.
- Don't use IBM Plex Mono for headings or running prose.
- Don't go below `text-micro` (9px) for any text.
- Don't go below `text-xs` (11px) for content that must be read.
- Don't use ALL CAPS for buttons or headings — uppercase is reserved for small section labels at `text-xxs`.
