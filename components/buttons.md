---
title: Buttons
category: components
tokens: [deep-teal, deep-teal-light, error, border, shell-warm, ink, surface, radius-sm, text-sm]
related: [color, typography, iconography]
---

# Buttons

## Principles

Three button kinds for three jobs: primary (`deep-teal`), secondary (transparent), danger (`error`). Sentence case always — no uppercase. Buttons live within the `radius-sm` family.

## Tokens / Values

| Variant | Background | Text | Border | Hover background |
|---|---|---|---|---|
| Primary | `deep-teal` | `surface` | none | `deep-teal-light` |
| Secondary | transparent | `ink` | `border`, 1px | `shell-warm` |
| Danger | `error` | `surface` | none | `error-light` (use sparingly) |

| Property | Value |
|---|---|
| Height | 30–36px |
| Padding | `space-2` vertical, `space-4` horizontal |
| Radius | `radius-sm` (4px) |
| Font | Inter 500, `text-sm` (12px) |
| Letter spacing | default body (`0.04em`) |
| Text transform | none (sentence case) |

## Semantic Assignment Rules

- **One primary per surface.** Never stack two `deep-teal` buttons next to each other.
- **Secondary is the workhorse.** Default to secondary unless a clear primary action exists.
- **Danger is reserved.** Use only for destructive actions (delete, discard, irreversibly change). Pair with a confirmation step.
- **Icon buttons** carry a Phosphor Thin icon at 16–18px; if icon-only, always provide an accessible label and a tooltip.
- **Loading state**: replace the icon with a Phosphor `circle-notch` Thin 16px in `ink-faint`, keep the label visible. Disable interaction.

## Examples

Primary button:

```css
.btn-primary {
  background: var(--deep-teal);
  color: var(--surface);
  border: none;
  border-radius: var(--radius-sm);
  padding: var(--space-2) var(--space-4);
  font-family: Inter, system-ui, sans-serif;
  font-weight: 500;
  font-size: var(--text-sm);
  height: 32px;
}
.btn-primary:hover { background: var(--deep-teal-light); }
```

Secondary button:

```css
.btn-secondary {
  background: transparent;
  color: var(--ink);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: var(--space-2) var(--space-4);
  font: 500 var(--text-sm) Inter, system-ui, sans-serif;
  height: 32px;
}
.btn-secondary:hover { background: var(--shell-warm); }
```

## Don'ts

- Don't use ALL CAPS or `text-transform: uppercase` on button labels.
- Don't add box-shadows or gradients.
- Don't stack two primary buttons side by side.
- Don't use `error` or `error-light` outside the Danger button.
- Don't size buttons below 30px tall — touch target floor.
- Don't put icons on the right unless the icon represents direction (`arrow-right`, `caret-right`).
