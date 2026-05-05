---
title: Modals
category: components
tokens: [surface, border, radius-lg, space-10, ink-muted, ink, motion-slow]
related: [elevation, motion, accessibility]
---

# Modals

## Principles

A modal is an interruption. It exists when the next action requires the user's full attention — confirming a destructive operation, capturing a focused input, presenting a single decision. Drawers (slide-in panels) and dialogs share the same patterns and live in this chunk.

## Tokens / Values

| Property | Value |
|---|---|
| Background | `surface` |
| Border | `border`, 1px solid |
| Radius | `radius-lg` (12px) |
| Overlay | `rgba(17, 17, 17, 0.4)` |
| Padding | `space-10` (20px) |
| Max width — content modal | 640px |
| Max width — confirmation modal | 400px |
| Max width — drawer | 480px (right-side) |
| Close button | top-right, Phosphor `x` Thin 18px, `ink-muted` (hover `ink`) |
| Enter / exit | `motion-slow` opacity fade |

## Semantic Assignment Rules

- **One modal at a time.** Never stack modals.
- **Always provide a close affordance.** A top-right close button plus `Esc` keyboard shortcut.
- **Confirmation modals** ask one question and offer two buttons (cancel + confirm). Confirm uses Primary or Danger; cancel is Secondary.
- **Content modals** carry richer content (forms, summaries, settings) and may use a footer with action buttons.
- **Drawers** slide in from the right at `motion-slow`; close on overlay click or `Esc`.
- **Focus trap.** Focus enters the modal on open and stays inside until the modal closes.
- **Initial focus** is the first interactive element, except in confirmation modals where it lands on the cancel button (so Enter-pressing doesn't auto-confirm a destructive action).

## Examples

A confirmation modal:

```html
<div class="modal-overlay">
  <div class="modal modal-confirm" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <h2 id="modal-title">Delete this indicator?</h2>
    <p>This removes all linked observations. This cannot be undone.</p>
    <div class="modal-actions">
      <button class="btn-secondary">Cancel</button>
      <button class="btn-danger">Delete</button>
    </div>
  </div>
</div>
```

```css
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(17, 17, 17, 0.4);
  display: grid;
  place-items: center;
  opacity: 0;
  transition: opacity var(--motion-slow) cubic-bezier(0.16, 1, 0.3, 1);
}
.modal-overlay[data-open="true"] { opacity: 1; }

.modal {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: var(--space-10);
  max-width: 640px;
}
.modal-confirm { max-width: 400px; }
```

## Don'ts

- Don't open a modal automatically on page load.
- Don't stack modals.
- Don't use `motion-default` slide-in for modals — fade only.
- Don't omit the close button or `Esc` handler.
- Don't auto-focus the destructive confirm button in a confirmation modal.
- Don't pad below `space-8` (16px) — confirmation copy needs breathing room.
