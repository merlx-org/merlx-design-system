---
title: Loading and Skeletons
category: patterns
tokens: [shell-warm, ink-faint, iris, motion-default, motion-slow, radius-sm, radius-md]
related: [motion, cards, accessibility]
---

# Loading and Skeletons

## Principles

Skeletons are the default loading state. They hold the shape of the eventual content so the layout doesn't shift on hydration. Spinners are a last resort, used only when no skeleton is possible.

## Tokens / Values

### Skeleton block

| Property | Value |
|---|---|
| Background | `shell-warm` |
| Radius | match the loaded element's radius (`radius-sm` for inputs, `radius-md` for cards, `100%` for avatars) |
| Animation | opacity pulse 1.0 → 0.5 → 1.0 over 1200ms, `linear` |
| No shimmer | gradient sweeps are forbidden |

### Inline progress bar

| Property | Value |
|---|---|
| Position | top of card, full-width, 1px tall |
| Color | `iris` |
| Animation | indeterminate width oscillation 200ms `linear`, or determinate width `motion-fast` `linear` |

### Spinner (last resort)

| Property | Value |
|---|---|
| Icon | Phosphor `circle-notch` Thin 16px |
| Color | `ink-faint` |
| Animation | rotate 360° over 800ms, `linear`, infinite |
| Use only when | no skeleton possible (indeterminate background job confirmation modal, etc.) |

## Semantic Assignment Rules

- **Skeleton, not empty state, during load.** An empty state is a *result*, not a *waiting room*.
- **Skeleton blocks match dimensions of the eventual element.** A loading card = a card-shaped skeleton; a loading row = a row-shaped skeleton.
- **No shimmer gradients.** The opacity pulse is the only sanctioned animation.
- **Inline progress at the top of a card** when content is loading inside an existing card. 1px tall, `iris`.
- **Avoid spinners inside buttons.** Replace the icon with a Phosphor `circle-notch` Thin 16px and keep the label visible; do not show a spinner overlay.

## Examples

A skeleton card:

```html
<div class="card skeleton-card">
  <div class="skeleton skeleton-line w-half"></div>
  <div class="skeleton skeleton-line w-full"></div>
  <div class="skeleton skeleton-line w-3-quarter"></div>
</div>
```

```css
.skeleton {
  background: var(--shell-warm);
  border-radius: var(--radius-sm);
  animation: skeleton-pulse 1200ms linear infinite;
}
.skeleton-line { height: 12px; margin: 6px 0; }
.w-half { width: 50%; }
.w-full { width: 100%; }
.w-3-quarter { width: 75%; }

@keyframes skeleton-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

@media (prefers-reduced-motion: reduce) {
  .skeleton { animation: none; opacity: 0.7; }
}
```

A card with an inline progress indicator:

```html
<div class="card">
  <div class="progress" data-determinate="true" style="--progress: 60%"></div>
  <h3>Aperture</h3>
  <p>Loading indicators…</p>
</div>
```

```css
.progress {
  height: 1px;
  background: var(--shell-warm);
  position: relative;
  overflow: hidden;
}
.progress::after {
  content: '';
  position: absolute;
  inset: 0 auto 0 0;
  width: var(--progress);
  background: var(--iris);
  transition: width var(--motion-fast) linear;
}
```

## Don'ts

- Don't show a generic spinner where a skeleton would fit.
- Don't use shimmer gradient sweeps.
- Don't show an empty state during load.
- Don't fade content in over a skeleton — replace the skeleton with content directly (no double-render).
- Don't render a full-page spinner.
- Don't let progress bars exceed 1px tall — use a 2px `iris` underline only for tab indicators (see `navigation.md`).
