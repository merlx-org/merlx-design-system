---
title: Forms
category: components
tokens: [ink, ink-muted, ember, ember-dim, error, error-light, success, surface, border, border-light, iris, radius-sm, space-2, space-3, space-4, space-5, text-xs, text-sm]
related: [inputs, voice-and-content, accessibility, notifications]
---

# Forms

## Principles

Forms communicate state explicitly. Every required field is marked. Every error names the field and the fix. Color is never the only signal — error states pair color with an icon and text. Validation runs only after the user leaves a field, never on every keystroke.

## Tokens / Values

| Element | Token / Value |
|---|---|
| Label | Inter 500, `text-xs`, `ink`, `space-2` margin below |
| Helper text | Inter 400, `text-xs`, `ink-muted`, `space-2` margin above |
| Error text | Inter 500, `text-xs`, `error`, paired with Phosphor `warning-circle` Fill 12px |
| Success text | Inter 500, `text-xs`, `success`, paired with Phosphor `check-circle` Fill 12px |
| Required marker | `*` in `ember`, `space-2` margin left of the label text |
| Field gap (vertical) | `space-5` between fields |
| Fieldset gap | `space-8` between fieldsets |
| Submit button row | `space-5` margin above, right-aligned |

## Semantic Assignment Rules

- **Inline validation runs on `onBlur`**, not on every keystroke. Errors show only after the user leaves the field for the first time.
- **Submit-time validation** aggregates errors at the top of the form with anchor links to each affected field.
- **Disabled fields** use `ink-faint` text on `shell-warm` background.
- **Readonly fields** use `ink-muted` text on `shell-cool` background.
- **Required fields** are marked with a `*` in `ember` after the label text. Optional fields carry no marker — never the word "(optional)".
- **Pair color with an icon and text.** A red border alone is not enough; pair with `warning-circle` and a written error message.

## Examples

A labelled input with helper text:

```html
<label class="field">
  <span class="field-label">Project name<span class="required">*</span></span>
  <input class="input" type="text" />
  <span class="field-helper">Used to label exports.</span>
</label>
```

A field in error state:

```html
<label class="field">
  <span class="field-label">Project name<span class="required">*</span></span>
  <input class="input input-error" type="text" value="" />
  <span class="field-error">
    <WarningCircle size={12} weight="fill" />
    Enter at least 3 characters.
  </span>
</label>
```

A field in success state (after async validation):

```html
<span class="field-success">
  <CheckCircle size={12} weight="fill" />
  Slug is available.
</span>
```

```css
.field { display: flex; flex-direction: column; gap: var(--space-2); }
.field + .field { margin-top: var(--space-5); }
.field-label { font: 500 var(--text-xs) Inter, system-ui, sans-serif; color: var(--ink); }
.required { color: var(--ember); margin-left: var(--space-2); }
.field-helper { font: 400 var(--text-xs) Inter, system-ui, sans-serif; color: var(--ink-muted); }
.field-error {
  font: 500 var(--text-xs) Inter, system-ui, sans-serif;
  color: var(--error);
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
}
.input-error { border-color: var(--error); }
```

## Don'ts

- Don't show errors before the user has interacted with the field.
- Don't use a red border without an accompanying error message + icon.
- Don't rely on color alone — always pair color with an icon and text.
- Don't use placeholder text as the only label.
- Don't add the word "(optional)" — mark required fields, leave optional unmarked.
- Don't auto-submit on blur — submission is always an explicit action.
- Don't use exclamation marks or "please" in error copy.
