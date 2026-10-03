---
title: Editorial layer
applies_to: marketing and editorial pages (merlx.org and sub-sites). Not dashboards or product UIs.
---

# Editorial layer

The core MERLx rules were written for analytical tools, where motion and large type compete with data. Marketing pages have a different job: to be read and remembered. This layer extends the core system for those pages only. Product UIs keep every core rule unchanged.

## Type

| Token | Size | Face | Use |
|---|---|---|---|
| display-xl | 56→96px | DM Serif Display | One per page: the opening headline |
| display-l | 40→64px | DM Serif Display | Section headlines |
| display-m | 32→44px | DM Serif Display | Sub-section headlines |
| title | 20→24px | Inter 600 | Card and layer titles |
| body-l | 17–18px | Inter 400 | Ledes |
| body | 15–16px | Inter 400 | Running text |
| eyebrow | 11px | IBM Plex Mono, uppercase | Section labels |

DM Serif Display is allowed at display sizes and for editorial accents; never for body text, buttons or labels. Italic accents inside display headlines use `iris` on paper and `teal-pale` on night. Measure: 60–70 characters.

## Layout

12-column grid, 1280px max width, side padding 16→48px. Section rhythm 72→120px (`space-section`) and 96→160px (`space-section-lg`).

## Colour

No new hues. `teal-pale` (#B8D9D3) is a named token. Three section surfaces:

- **paper**: shell background; the default.
- **line**: shell with a 48px survey grid; for analytical or "the model sees the plan" moments.
- **night**: deep-teal background, shell and teal-pale text; for network and closing moments.

## Motion

- A load animation is allowed (up to about 1.2 s) for illustrative scenes, never for headline or CTA text, which are visible on the first frame.
- No overshoot: no bounce or elastic easing. Critically damped smoothing is allowed.
- Reveal on scroll: fade plus a rise of 8–16px. No fly-ins from off-screen; no horizontal slides (they break right-to-left layouts).
- Scroll-linked motion is allowed when tied 1:1 to scroll position, with no autoplay. At most one pinned sequence per page.
- Hover and focus keep the core 200 ms default.
- `prefers-reduced-motion: reduce` turns every reveal off and every scroll-linked sequence into static panels.
- Still no box-shadow elevation. Shading inside a 3D or illustrated scene is rendering, not interface elevation.
- No emoji.

## Classes (merlx-website)

`mx-ed-display-xl|l|m`, `mx-ed-title`, `mx-ed-lede`, `mx-ed-body`, `mx-ed-eyebrow`, `mx-ed-section`, `mx-ed-wrap`, `mx-surface--paper|line|night`, `mx-chip--iris|teal|ember`, `mx-reveal`.
