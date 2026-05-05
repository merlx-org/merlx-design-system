---
title: Empty / Error / Success
category: patterns
tokens: [ink-light, ink-muted, error, success, ember, deep-teal, surface, text-lg, text-sm]
related: [empty-states, notifications, voice-and-content]
---

# Empty / Error / Success

## Principles

Every async surface — a list, a chart, a saved record — has at least three states beyond loading: empty, error, success. These three are not optional. Designing only the happy path produces brittle UIs that surprise the user the first time something goes wrong.

## Tokens / Values

### Empty

Defer to `components/empty-states.md`. One DM Serif Display italic line + one Inter 400 description line, optional Secondary CTA.

### Error

| Element | Token / Value |
|---|---|
| Status icon | Phosphor `warning-circle` Fill 24px in `error` |
| Title | Inter 600, `text-sm`, `ink-light` |
| Body | Inter 400, `text-sm`, `ink-muted` |
| Body length | one to two lines naming what happened and what to try |
| Retry action | Secondary button if retry is meaningful |
| Layout | center-aligned within the failed surface |

### Success (persistent)

| Element | Token / Value |
|---|---|
| Status icon | Phosphor `check-circle` Fill 24px in `success` |
| Title | DM Serif Display italic, `text-lg`, `ink-light` |
| Body | Inter 400, `text-sm`, `ink-muted` — one line |
| Layout | center-aligned within the relevant surface |
| Use when | after destructive or one-way actions only (export complete, account deleted) |

For ephemeral success (saved, copied, exported), use a toast — see `components/notifications.md`.

## Semantic Assignment Rules

- **Every async surface ships all three states.** Skipping is not a choice.
- **Empty is a result, never a waiting room.** During load, show a skeleton (see `loading-and-skeletons.md`).
- **Errors offer a retry path.** If retry is meaningful, include a Secondary button. If retry will not help (e.g., permission denied), explain the actual fix.
- **Errors describe what happened, not "an error occurred."** Name the surface and the cause.
- **Success surfaces are rare.** Most successes are toasts. A persistent success surface is appropriate only for destructive or one-way actions.
- **Never use the word "error"** in user-facing copy; describe what happened.
- **No exclamation marks.** Calm voice across all three states.

## Examples

An error state inside a chart card:

```html
<div class="state-error">
  <WarningCircle size={24} weight="fill" color="var(--error)" />
  <h3 class="state-title">Couldn't load this chart.</h3>
  <p class="state-body">The Aperture data feed timed out. Try again in a moment.</p>
  <button class="btn-secondary">Retry</button>
</div>
```

A persistent success state after an export:

```html
<div class="state-success">
  <CheckCircle size={24} weight="fill" color="var(--success)" />
  <h3 class="state-title-editorial">Export complete.</h3>
  <p class="state-body">Your CSV has been delivered to the download tray.</p>
</div>
```

```css
.state-error, .state-success {
  text-align: center;
  padding: var(--space-12) var(--space-8);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3);
}
.state-title { font: 600 var(--text-sm) Inter, system-ui, sans-serif; color: var(--ink-light); }
.state-title-editorial {
  font-family: "DM Serif Display", Georgia, serif;
  font-style: italic;
  font-size: var(--text-lg);
  color: var(--ink-light);
}
.state-body { font: 400 var(--text-sm) Inter, system-ui, sans-serif; color: var(--ink-muted); }
```

## Don'ts

- Don't ship a feature without designing all three states.
- Don't use the word "error" in copy.
- Don't use exclamation marks.
- Don't render an error without a recovery path (retry or explanation of the fix).
- Don't render a persistent success state for routine saves — toast it.
- Don't block the user from leaving a success surface.
