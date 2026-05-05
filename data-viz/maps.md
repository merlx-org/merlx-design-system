---
title: Maps
category: data-viz
tokens: [shell, shell-warm, surface, deep-teal, ember, iris, sand-dark, deep-iris, ink, ink-muted, border-light, success, error]
related: [charts, color, accessibility]
---

# Maps

## Principles

Maps in MERLx contexts (Sudan, Somalia, East Africa) carry analytical weight, not decorative weight. Basemaps are flat — no terrain, no satellite imagery. Color encodes the data layer; the basemap stays calm and unobtrusive.

## Tokens / Values

### Basemap

| Element | Token / Value |
|---|---|
| Land background | `shell` |
| Water | `shell-warm` |
| Country / region borders (default) | `border-light`, 1px |
| Country / region borders (over colored fill) | `surface`, 1px |
| Country labels | Inter 500, `text-xs`, `ink`, with 2px `surface` halo |
| Place labels | Inter 400, `text-xs`, `ink-muted` |

### Choropleth (sequential)

5-step ramp from `shell-warm` → `deep-teal` for any single positive metric. Each step is a manual interpolation rather than a continuous gradient.

| Step | Color |
|---|---|
| 0 (lowest) | `shell-warm` (#EDE9E1) |
| 1 | `#B5C2BD` |
| 2 | `#7E9991` |
| 3 | `#487268` |
| 4 (highest) | `deep-teal` (#1A3A34) |

### Choropleth (diverging)

For metrics that span negative-to-positive (e.g., year-over-year change), interpolate from `error` through `shell` to `success`.

| Step | Color |
|---|---|
| -2 (most negative) | `error` (#B83A2A) |
| -1 | `#D58A82` |
| 0 (zero / neutral) | `shell` (#F5F3EE) |
| +1 | `#90D2B4` |
| +2 (most positive) | `success` (#3BAA7F) |

### Categorical map

Same 5-color order as charts: `deep-teal`, `ember`, `iris`, `sand-dark`, `deep-iris`.

### Heatmap

Alpha-blend `ember` over `shell` at 0–60% opacity. Never use rainbow heatmaps.

### Point markers

| Property | Value |
|---|---|
| Default | 6px circle, Phosphor `circle` Fill in the categorical color |
| Border | 1px `surface` for contrast on dense backgrounds |
| Hover | 8px circle |
| Maximum | 12px (cluster instead of growing markers) |

## Semantic Assignment Rules

- **Pick the ramp by what the data is**: single-positive → sequential; spans negative-to-positive → diverging; categorical regions → categorical.
- **Borders flip color based on the underlying fill.** On `shell`/`shell-warm`, use `border-light`. On any colored fill, use `surface` for legibility.
- **Country labels carry a `surface` halo.** This keeps them readable on colored fills.
- **Don't oversize point markers** — clustering beats scaling. A 40px dot reads as "important" even when the underlying number doesn't justify it.

## Examples

A choropleth in pseudocode (using a map library — e.g., MapLibre, Leaflet):

```tsx
<Choropleth
  data={regions}
  valueAccessor={(r) => r.indicator_score}
  colorScale={[
    'var(--shell-warm)',
    '#B5C2BD',
    '#7E9991',
    '#487268',
    'var(--deep-teal)'
  ]}
  borderColor="var(--surface)"
  borderWidth={1}
/>
```

A categorical regions overlay:

```tsx
<RegionLayer
  data={regions}
  colorAccessor={(r, i) => [
    'var(--deep-teal)',
    'var(--ember)',
    'var(--iris)',
    'var(--sand-dark)',
    'var(--deep-iris)'
  ][i % 5]}
/>
```

## Don'ts

- Don't use terrain or satellite basemaps in MERLx products.
- Don't use rainbow scales (HSL hue ramps).
- Don't render bubble maps that scale dot area larger than 40px.
- Don't omit the `surface` halo on country labels over colored fills.
- Don't pair categorical and choropleth on the same layer — pick one analytical claim per map.
- Don't display political boundaries as the only data — borders are basemap chrome, not data.
