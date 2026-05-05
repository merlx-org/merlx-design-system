---
title: Notifications
category: components
tokens: [ink, ink-muted, surface, border-light, ember, ember-dim, ember-dark, error, error-light, success, iris, iris-dim, iris-dark, deep-teal, deep-teal-dim, shell-warm, radius-md, space-4, space-5, space-8, motion-slow, text-sm, text-xs]
related: [color, motion, voice-and-content, empty-error-success]
---

# Notifications

## Principles

Three notification surfaces — toast, banner, inline — for three scopes: ephemeral system feedback, page-wide context, and component-local context. All fade in (no slide), pair color with a Phosphor Thin status icon, and never carry decorative elements.

## Tokens / Values

### Toast

| Property | Value |
|---|---|
| Position | bottom-right, `space-8` from viewport edges |
| Max width | 360px |
| Background | `surface` |
| Border | `border-light`, 1px solid |
| Radius | `radius-md` |
| Padding | `space-5` |
| Status icon | Phosphor Thin 18px in the semantic color, left of text |
| Title | Inter 500, `text-sm`, `ink` |
| Description (optional) | Inter 400, `text-xs`, `ink-muted` |
| Dismiss button | top-right, Phosphor `x` Thin 14px, `ink-muted` (hover `ink`) |
| Auto-dismiss (info, success) | 5s |
| Auto-dismiss (warning) | 8s |
| Auto-dismiss (error) | never — manual dismiss only |
| Enter / exit | fade `motion-slow`, no slide |

### Banner

| Property | Value |
|---|---|
| Position | full-width below topbar |
| Background | semantic dim variant (`iris-dim` info, `ember-dim` warning, etc.) |
| Border | none |
| Radius | none (full-bleed) |
| Padding | `space-4` vertical, `space-8` horizontal |
| Status icon | Phosphor Thin 18px in the semantic accent color |
| Body | Inter 400, `text-sm`, semantic accent text color |
| Optional CTA | Secondary button, right-aligned |
| Dismiss | optional Phosphor `x` Thin 14px on the far right |

### Inline alert

| Property | Value |
|---|---|
| Position | within a card or form section |
| Background | semantic dim variant |
| Border | none |
| Radius | `radius-md` |
| Padding | `space-4` |
| Status icon | Phosphor Thin 16px in the semantic accent color |
| Body | Inter 400, `text-xs`, semantic accent text color |
| No dismiss button | inline alerts are scoped, not interruptions |

### Severity → color

| Severity | Background | Icon / text accent |
|---|---|---|
| Info | `iris-dim` | `iris-dark` |
| Success | `rgba(59, 170, 127, 0.12)` (success-dim, derived) | `success` |
| Warning | `ember-dim` | `ember-dark` |
| Error | `rgba(184, 58, 42, 0.12)` (error-dim, derived) | `error` |
| Neutral | `shell-warm` | `ink-muted` |

> Note: `success-dim` and `error-dim` are documented as inline rgba values in v0.1.0. They will be promoted to canonical tokens in `color.md` in a future patch release.

## Semantic Assignment Rules

- **Toasts are for ephemeral system feedback.** Saved, deleted, copied, exported — short-lived confirmations.
- **Banners are for page-wide context.** Maintenance windows, account-level warnings, version-upgrade prompts.
- **Inline alerts are for component-local context.** A specific form field, a single dashboard tile, a per-row warning in a table.
- **Never auto-dismiss errors.** The user must dismiss explicitly.
- **One banner at a time.** If multiple banner-level events fire, queue them — never stack.
- **No slide-in animation.** Fade only, `motion-slow`.

## Examples

A success toast:

```html
<div class="toast toast-success" role="status">
  <CheckCircle size={18} weight="thin" />
  <div class="toast-body">
    <p class="toast-title">Indicator saved.</p>
  </div>
  <button class="toast-dismiss"><X size={14} weight="thin" /></button>
</div>
```

```css
.toast {
  position: fixed;
  bottom: var(--space-8);
  right: var(--space-8);
  background: var(--surface);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--space-5);
  max-width: 360px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: var(--space-4);
  align-items: start;
  opacity: 0;
  transition: opacity var(--motion-slow) cubic-bezier(0.16, 1, 0.3, 1);
}
.toast[data-open="true"] { opacity: 1; }
```

A warning banner:

```html
<div class="banner banner-warning" role="status">
  <WarningCircle size={18} weight="thin" />
  <p>The Aperture data feed is delayed by 12 hours.</p>
  <button class="btn-secondary">View status</button>
</div>
```

An inline error alert in a form section:

```html
<div class="inline-alert inline-alert-error" role="alert">
  <WarningCircle size={16} weight="thin" />
  <p>This export failed because the dataset is currently being rebuilt.</p>
</div>
```

## Don'ts

- Don't slide-in toasts or banners — fade only.
- Don't stack banners; queue them.
- Don't auto-dismiss errors.
- Don't put more than a single Secondary CTA in a banner.
- Don't use a destructive (red) toast for a non-error event.
- Don't use exclamation marks in notification copy.
- Don't render multiple inline alerts of the same severity in one card — consolidate into one.
