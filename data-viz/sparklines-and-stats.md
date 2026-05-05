---
title: Sparklines and Stats
category: data-viz
tokens: [deep-teal, ember, error, success, ink, ink-muted, ink-faint, surface, border-light, text-lg, text-xs, text-xxs, text-micro]
related: [charts, typography]
---

# Sparklines and Stats

## Principles

KPI tiles communicate a single number at a glance. The value is large, the label is small, the delta tells the story. Sparklines visualize the trend in 24px without labels, axes, or gridlines.

## Tokens / Values

### KPI tile

| Element | Token / Value |
|---|---|
| Label (above value) | Inter 500, `text-xs`, `ink-muted`, sentence case |
| Value | Inter 700, `text-lg` (or DM Serif Display for editorial dashboards), `ink` |
| Delta | IBM Plex Mono, `text-micro`, paired with a triangle icon |
| Time-window label | Inter 500, `text-xxs`, uppercase, `ink-faint`, letter-spacing 1.5px |
| Tile background | `surface` |
| Tile border | `border-light`, 1px |
| Tile padding | `space-7` |

### Sparkline

| Element | Value |
|---|---|
| Height | 24px |
| Stroke | 1.5px |
| Default color | `deep-teal` |
| Above warning threshold | `ember` |
| Critical | `error` |
| Endpoint dot | 3px Phosphor `circle` Fill, same color as stroke |
| Axes / gridlines | none |
| Animation | none on first paint; on data update, fade-in `motion-fast` |

### Delta indicator

| Direction | Icon | Color |
|---|---|---|
| Positive | Phosphor `triangle-up` Fill 10px | `success` |
| Negative | Phosphor `triangle-down` Fill 10px | `error` |
| Neutral | Phosphor `minus` Regular 10px | `ink-muted` |

The delta value (e.g., `+12 %` or `-3 pts`) follows the icon in IBM Plex Mono `text-micro`.

## Semantic Assignment Rules

- **One KPI per tile.** Don't pack two values into one tile.
- **Pick the value typography by context.** Inter 700 for analytical dashboards; DM Serif Display for editorial / executive summaries.
- **Sparklines stay calm.** No axes, no labels, no animation on first paint, no fancy gradients.
- **Sparkline color encodes status.** `deep-teal` = normal; `ember` = above warning threshold; `error` = critical.
- **Delta goes below the value, not beside it** — it's commentary, not part of the number.
- **Time-window label sits above the main label** at `text-xxs` uppercase. It scopes the value (e.g., "30D", "MTD", "YTD").

## Examples

A KPI tile:

```html
<div class="kpi-tile">
  <span class="kpi-window">30D</span>
  <span class="kpi-label">Active indicators</span>
  <span class="kpi-value">128</span>
  <span class="kpi-delta kpi-delta-up">
    <TriangleUp size={10} weight="fill" />
    +12
  </span>
  <Sparkline data={trend} color="var(--deep-teal)" />
</div>
```

```css
.kpi-tile {
  background: var(--surface);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--space-7);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}
.kpi-window {
  font: 500 var(--text-xxs) Inter, system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: var(--ink-faint);
}
.kpi-label { font: 500 var(--text-xs) Inter, system-ui, sans-serif; color: var(--ink-muted); }
.kpi-value { font: 700 var(--text-lg) Inter, system-ui, sans-serif; color: var(--ink); }
.kpi-delta {
  font: 500 var(--text-micro) "IBM Plex Mono", monospace;
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
}
.kpi-delta-up { color: var(--success); }
.kpi-delta-down { color: var(--error); }
```

A warning-state sparkline:

```tsx
<Sparkline
  data={trend}
  color="var(--ember)"
  height={24}
  strokeWidth={1.5}
  endpoint
/>
```

## Don'ts

- Don't animate a number ticker — values appear at their final value.
- Don't use a "hero" oversized number that grows on load — render at final size immediately.
- Don't add decorative icons next to the value (e.g., a "📈" or a chart-line symbol).
- Don't pair two sparklines in one tile.
- Don't render axes, labels, or gridlines on a sparkline.
- Don't use `success` or `error` as the sparkline color — those are reserved for the delta. Sparkline status uses `deep-teal` / `ember` / `error`.
