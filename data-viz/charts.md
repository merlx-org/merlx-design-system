---
title: Charts
category: data-viz
tokens: [deep-teal, ember, iris, sand-dark, deep-iris, ink, ink-muted, ink-faint, border-light, surface, text-micro, text-xs, radius-sm]
related: [color, typography, dense-tables]
---

# Charts

## Principles

Charts encode quantitative data with the minimum amount of visual ink. No 3D, no shadows, no decorative gradients, no rainbow palettes. Categorical color order is fixed across all MERLx products so a "Category 1" series is always `deep-teal` regardless of which chart it appears in.

## Tokens / Values

### Categorical color order

When color-coding categories or series, draw from this list in this order. Never invent new categorical colors.

| Index | Token | Hex |
|---|---|---|
| 1 | `deep-teal` | `#1A3A34` |
| 2 | `ember` | `#CA5D0F` |
| 3 | `iris` | `#8071BC` |
| 4 | `sand-dark` | `#C4A98A` |
| 5 | `deep-iris` | `#4A3F6B` |

If more than 5 categories are required, derive lighter / darker variants of the existing tokens via opacity or HSL — do not introduce new base colors.

### Chart chrome

| Element | Value |
|---|---|
| Axis line | `border-light`, 1px |
| Axis tick marks | none |
| Gridlines | horizontal only, `border-light`, 1px |
| Vertical gridlines | none |
| Axis labels | Inter 500, `text-xs`, `ink-muted` |
| Numeric labels | IBM Plex Mono `text-micro`, `ink` |
| Legend swatch | 12px square, `radius-sm` |
| Legend font | Inter 500, `text-xs`, `ink` |
| Legend position | top-right |
| Background | `surface` (charts sit inside cards) |

### Chart-specific rules

| Chart type | Rule |
|---|---|
| Bar | 60% bar width, 40% gap. Optional `radius-sm` on top corners only. |
| Line | 1.5px stroke. No data dots except on hover (4px filled at the cursor x). |
| Area | Line stroke + 25% opacity fill of the same color. |
| Stacked (bar / area) | Stacking order matches categorical color order; legend lists in the same order. |
| Scatter | 4px filled dots in the categorical color, 1px `surface` border for contrast on dense backgrounds. |

## Semantic Assignment Rules

- **The first series uses `deep-teal`. Always.** Even if a chart has only one series.
- **Highlight a single series** by leaving it at full color and reducing all others to `ink-faint` at 40% opacity.
- **Reference lines (target, threshold)** use `ember` 1.5px dashed.
- **No 3D, no isometric, no perspective.**
- **No bubble charts.** They distort area perception. Use scatter with sized dots no larger than 12px.
- **No pie charts.** Use stacked bars instead.
- **No diverging gradients in regular charts** — those are reserved for choropleth maps (see `maps.md`).
- **Right-align numeric axis labels.**

## Examples

A bar chart in pseudocode (using a chart library — e.g., Recharts, Visx):

```tsx
<BarChart>
  <CartesianGrid horizontal vertical={false} stroke="var(--border-light)" />
  <XAxis stroke="var(--border-light)" tickLine={false}
         tick={{ fontFamily: 'Inter', fontSize: 11, fill: 'var(--ink-muted)' }} />
  <YAxis stroke="var(--border-light)" tickLine={false}
         tick={{ fontFamily: 'IBM Plex Mono', fontSize: 9, fill: 'var(--ink)' }} />
  <Bar dataKey="series1" fill="var(--deep-teal)" />
  <Bar dataKey="series2" fill="var(--ember)" />
  <Legend iconType="square" iconSize={12} />
</BarChart>
```

A line chart with a target reference:

```tsx
<LineChart>
  <Line stroke="var(--deep-teal)" strokeWidth={1.5} dot={false} />
  <ReferenceLine y={75} stroke="var(--ember)" strokeWidth={1.5} strokeDasharray="3 3" />
</LineChart>
```

## Don'ts

- Don't use rainbow palettes or HSL ramps for categorical data.
- Don't use 3D effects, shadows, or perspective.
- Don't use pie or donut charts.
- Don't use bubble charts where dot area encodes a value.
- Don't add vertical gridlines.
- Don't animate on first paint — animate only on data updates, with `motion-fast` and `linear` easing.
- Don't use Inter for numeric axis labels — IBM Plex Mono.
