---
title: Motion
category: foundations
tokens: [motion-fast, motion-default, motion-slow]
related: [identity, accessibility, loading-and-skeletons]
---

# Motion

## Principles

Calm motion. No bouncing, no spring physics, no overshoot. Transitions communicate state change, not personality. Animation never plays on page load — content should be there, not arrive.

## Tokens / Values

### Default transition

```
200ms cubic-bezier(0.16, 1, 0.3, 1)
```

Slightly snappy with a soft landing. Used for all interactive state changes — hover, focus, active.

### Timing scale

| Token | Duration | Use |
|-------|----------|-----|
| `motion-fast` | 100ms | Tooltips, opacity micro-feedback |
| `motion-default` | 200ms | Hover states, color transitions, most interactions |
| `motion-slow` | 300ms | Panel open / close, element enter / exit |

## Semantic Assignment Rules

- **Hover states** — color shift + optional `scale(1.05)` on small interactive elements (icons, dots). Never scale cards or panels.
- **Appearing elements** — fade in (`opacity 0 → 1`) over `motion-slow`. No slide-in, no fly-in.
- **Progress and bar charts** — animate width with `motion-fast` and `linear` easing (not the default curve).
- **Loading states** — prefer subtle opacity pulse over spinners. If a spinner is necessary, keep it small (Phosphor `circle-notch` Thin 16px) in `ink-faint`.
- **Reduced motion** — always respect `prefers-reduced-motion`. Disable all transitions and animations when set.

## Examples

A standard hover transition:

```css
.btn {
  transition: background var(--motion-default) cubic-bezier(0.16, 1, 0.3, 1);
}
```

A progress bar:

```css
.progress-fill {
  transition: width var(--motion-fast) linear;
}
```

Reduced-motion fallback:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0ms !important;
    transition-duration: 0ms !important;
  }
}
```

## Don'ts

- Don't use spring physics, bouncing, or overshoot.
- Don't slide elements in or out — fade only.
- Don't animate on initial page load.
- Don't scale cards or panels on hover (only small interactive elements).
- Don't omit the `prefers-reduced-motion` fallback.
