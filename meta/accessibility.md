---
title: Accessibility
category: meta
tokens: [iris, ink, ink-muted, ink-faint, shell, surface]
related: [color, typography, responsive, forms, inputs]
---

# Accessibility

## Principles

Accessibility is not a checklist applied at the end — it is a property of the tokens themselves. Contrast ratios, focus indicators, and reduced-motion behavior are enforced at the design-system level so any component built from MERLx tokens inherits them.

## Tokens / Values

### Contrast ratios (WCAG)

| Pair | Ratio | Level |
|---|---|---|
| `ink` on `shell` | 14.5:1 | AAA |
| `ink-light` on `shell` | ~10.7:1 | AAA |
| `ink-muted` on `shell` | ~5.2:1 | AA |
| `ink-faint` on `shell` | ~2.9:1 | not for body text |
| `ink` on `surface` | 19.0:1 | AAA |
| Interactive elements | minimum 4.5:1 | required |

### Focus indicator

| Property | Value |
|---|---|
| Style | 2px solid `iris` |
| Offset | 2px from element |
| Visibility | always visible on keyboard focus |
| Override | never remove without an equivalent visible replacement |

## Semantic Assignment Rules

- **Body text uses `ink` or `ink-light`.** `ink-muted` is the floor for readable text on `shell`.
- **Never use `ink-faint` for content that must be readable.** Reserve it for placeholder, disabled, and decorative supporting text.
- **Verify accent text on dim backgrounds per combination.** `iris-dark` on `iris-dim` is verified; new pairings must be checked. When in doubt, use the full accent on `surface` instead.
- **Focus indicator is `iris` on every interactive element.** No exceptions.
- **Touch targets** are 44 × 44px minimum on mobile.
- **Reduced motion** disables all transitions and animations when `prefers-reduced-motion: reduce` is set.
- **Color is never the only signal.** Status, errors, and successes pair color with an icon and text.

## Examples

A focus ring:

```css
.btn:focus-visible {
  outline: 2px solid var(--iris);
  outline-offset: 2px;
}
```

Reduced-motion fallback (mirrored from `motion.md`):

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

A status pair (icon + color + text):

```html
<span class="status-warning">
  <WarningCircle size={16} weight="thin" />
  <span>Above threshold</span>
</span>
```

## Don'ts

- Don't remove the focus outline without replacing it with an equivalent visible indicator.
- Don't use `ink-faint` for text that must be read.
- Don't communicate state through color alone — pair with an icon and text.
- Don't size touch targets below 44 × 44px on mobile.
- Don't disable `prefers-reduced-motion` handling.
- Don't ship a new accent / dim pairing without verifying contrast.
