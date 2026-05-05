---
title: Inputs
category: components
tokens: [surface, border, iris, ink, ink-faint, ink-muted, shell-warm, shell-cool, deep-teal, deep-teal-dim, error, error-light, radius-sm, radius-pill, space-2, space-3, space-4, text-base, text-sm]
related: [forms, color, accessibility, iconography]
---

# Inputs

## Principles

All input controls share one base — `surface` background, `border` 1px, `radius-sm`, Inter 400 `text-base`, `iris` focus ring. Variants (textarea, select, checkbox, radio, switch, search) extend the base; they do not introduce new visual languages.

## Tokens / Values

### Base text input

| Property | Value |
|---|---|
| Background | `surface` |
| Border | `border`, 1px solid |
| Focus border | `iris` |
| Radius | `radius-sm` |
| Padding | `space-2` vertical, `space-4` horizontal |
| Font | Inter 400, `text-base` |
| Placeholder color | `ink-faint` |
| Disabled background | `shell-warm` |
| Disabled text | `ink-faint` |
| Readonly background | `shell-cool` |
| Readonly text | `ink-muted` |

## Semantic Assignment Rules

- **Focus is `iris`, never `deep-teal`.** Action and focus are distinct semantics — `deep-teal` belongs to primary actions.
- **Error state**: 1px `error` border, `error` helper text below. See `forms.md` for the full error pattern.
- **Disabled vs readonly**: disabled means the field is inactive in the current state; readonly means the value is informational. Different backgrounds make this distinguishable at a glance.
- **All inputs share the same height** as buttons (32px) so they line up in a form row.

## Variants

### Textarea

Same base styling. Vertical resize only (`resize: vertical`). Minimum 3 visible rows. Padding identical to text input.

```css
.textarea {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: var(--space-2) var(--space-4);
  font: 400 var(--text-base) Inter, system-ui, sans-serif;
  resize: vertical;
  min-height: calc(3 * 1.5em + var(--space-4));
}
.textarea:focus { border-color: var(--iris); outline: none; }
```

### Select

Native `<select>` styled to match the text input base. Trailing Phosphor `caret-down` Thin 16px in `ink-muted`, positioned in the right padding zone. Opens the OS-native dropdown — no custom popover unless multi-select is required (out of scope for v0.1.0).

```css
.select {
  background: var(--surface) url('/assets/caret-down.svg') no-repeat right var(--space-3) center;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: var(--space-2) var(--space-7) var(--space-2) var(--space-4);
  font: 400 var(--text-base) Inter, system-ui, sans-serif;
  appearance: none;
}
```

### Checkbox

Square 16×16px box, `radius-sm`, 1px `border`. Checked: `deep-teal` background + Phosphor `check` Fill 12px in `surface`. Label sits to the right at `space-3` gap.

```css
.checkbox {
  width: 16px;
  height: 16px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--surface);
}
.checkbox:checked {
  background: var(--deep-teal);
  border-color: var(--deep-teal);
}
```

### Radio

Circular 16×16px, otherwise identical to checkbox. Checked indicator is a 6px filled `deep-teal` dot centered inside.

```css
.radio {
  width: 16px;
  height: 16px;
  border: 1px solid var(--border);
  border-radius: 50%;
  background: var(--surface);
}
.radio:checked::after {
  content: '';
  display: block;
  width: 6px;
  height: 6px;
  margin: 4px;
  border-radius: 50%;
  background: var(--deep-teal);
}
```

### Switch

Pill track 28×16px, `radius-pill`. Off: `shell-warm` track + `border` 1px + `ink-faint` thumb. On: `deep-teal-dim` track + `deep-teal` thumb. Thumb is a 12×12 circle that translates 12px on toggle. Transition uses `motion-default`.

```css
.switch-track {
  width: 28px;
  height: 16px;
  background: var(--shell-warm);
  border: 1px solid var(--border);
  border-radius: var(--radius-pill);
  position: relative;
  transition: background var(--motion-default) cubic-bezier(0.16, 1, 0.3, 1);
}
.switch-track[data-checked="true"] {
  background: var(--deep-teal-dim);
  border-color: var(--deep-teal);
}
.switch-thumb {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--ink-faint);
  position: absolute;
  top: 1px;
  left: 1px;
  transition: transform var(--motion-default) cubic-bezier(0.16, 1, 0.3, 1), background var(--motion-default);
}
.switch-track[data-checked="true"] .switch-thumb {
  background: var(--deep-teal);
  transform: translateX(12px);
}
```

### Search

Text input with a leading Phosphor `magnifying-glass` Thin 16px in `ink-muted`, positioned in the left padding zone. Optional trailing Phosphor `x` Thin 14px to clear when there is content.

```css
.search {
  background: var(--surface) url('/assets/magnifying-glass.svg') no-repeat left var(--space-3) center;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: var(--space-2) var(--space-4) var(--space-2) var(--space-7);
  font: 400 var(--text-base) Inter, system-ui, sans-serif;
}
```

## Examples

A labelled text input with helper text:

```html
<label class="field">
  <span class="field-label">Project name</span>
  <input class="input" type="text" placeholder="e.g. Aperture" />
  <span class="field-helper">Used to label exports.</span>
</label>
```

(See `forms.md` for the full label / helper / error layout.)

## Don'ts

- Don't use `deep-teal` for focus — focus is `iris`.
- Don't remove the focus ring without a replacement (see `accessibility.md`).
- Don't size inputs taller than 36px or shorter than 30px in dense forms.
- Don't make placeholder text the only label — labels must be visible.
- Don't replace the native `<select>` dropdown with a custom popover unless multi-select is required.
- Don't use a switch for a destructive or one-way action — use a button with confirmation.
