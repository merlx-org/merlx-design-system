---
title: Layouts
category: patterns
tokens: [shell, shell-warm, surface, border-light, space-5, space-10, space-12]
related: [spacing, navigation, responsive]
---

# Layouts

## Principles

Four canonical layouts handle every MERLx product surface — three-pane, dashboard grid, document reader, full-bleed map / canvas. Layouts are CSS Grid by default; flex is reserved for one-dimensional rows.

## Tokens / Values

### Three-pane

```
┌──────────┬───────────────┬──────────┐
│          │               │          │
│ Sidebar  │  Content      │  Detail  │
│ 200–240  │  1fr          │  300–360 │
│          │               │          │
└──────────┴───────────────┴──────────┘
```

| Pane | Width | Background |
|---|---|---|
| Sidebar | 200–240px | `shell-warm` |
| Content | 1fr | `shell` |
| Detail | 300–360px | `surface` |

```css
.layout-three-pane {
  display: grid;
  grid-template-columns: 220px 1fr 320px;
  min-height: 100vh;
}
```

Below `bp-tablet`, the detail pane becomes a modal or bottom sheet.

### Dashboard grid

12-column grid inside the content area. KPI tiles span 3 columns; charts span 6 or 12.

```
┌─────┬─────┬─────┬─────┐
│ KPI │ KPI │ KPI │ KPI │
└─────┴─────┴─────┴─────┘
┌─────────────┬───────────┐
│ Chart 6col  │ Chart 6col│
└─────────────┴───────────┘
┌─────────────────────────┐
│ Chart 12col             │
└─────────────────────────┘
```

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-5);
  padding: var(--space-10);
}
.kpi { grid-column: span 3; }
.chart-half { grid-column: span 6; }
.chart-full { grid-column: span 12; }
```

### Document reader

Single centered column, max-width 720px, generous page padding. Optional right-rail TOC at 240px on `bp-desktop`.

```
              ┌───────────────────────┐
              │                       │
              │   720px content       │   240
              │                       │   TOC
              │                       │
              └───────────────────────┘
```

```css
.layout-doc {
  max-width: 720px;
  margin: 0 auto;
  padding: var(--space-12);
}
@media (min-width: 1280px) {
  .layout-doc-with-toc {
    display: grid;
    grid-template-columns: 720px 240px;
    gap: var(--space-10);
    margin: 0 auto;
    width: max-content;
    padding: var(--space-12);
  }
}
```

### Full-bleed map / canvas

Sidebar + edge-to-edge map / canvas with floating panels at `space-5` from the viewport edges.

```
┌──────┬──────────────────────────┐
│      │  ┌────┐               ┌──┐│
│ Side │  │Pnl │   Map / canvas│Pnl│
│      │  └────┘               └──┘│
│      │                           │
└──────┴──────────────────────────┘
```

```css
.layout-canvas {
  display: grid;
  grid-template-columns: 220px 1fr;
  height: 100vh;
}
.layout-canvas-floating-panel {
  position: absolute;
  background: var(--surface);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--space-5);
}
```

## Semantic Assignment Rules

- **Pick the layout by what's primary on screen.** A list with a selected detail → three-pane. A grid of metrics → dashboard. A long-form report → document reader. A spatial visualization → full-bleed canvas.
- **Sidebars on the left, never on the right.**
- **Detail panes on the right, always.**
- **Page padding** uses `space-10` to `space-12`; grid gaps use `space-5` (dense) or `space-10` (comfortable).
- **First-paint requirement:** layouts must not depend on JavaScript. The grid renders in CSS; data hydrates afterwards.

## Examples

(See above — code blocks accompany each layout.)

## Don'ts

- Don't put sidebars on the right.
- Don't use centered fixed-width content layouts below 1024px viewport.
- Don't depend on JS for first paint of a layout.
- Don't mix four-pane layouts — three is the maximum (sidebar / content / detail).
- Don't pad less than `space-10` at the page level.
- Don't nest a dashboard grid inside another grid — pick one grid per page.
