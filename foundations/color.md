---
title: Color
category: foundations
tokens: [shell, shell-warm, shell-cool, ink, ink-light, ink-muted, ink-faint, surface, border, border-light, sand, sand-light, sand-dark, iris, iris-light, iris-dark, deep-teal, deep-teal-light, deep-iris, deep-iris-light, ember, ember-light, ember-dark, sand-dim, iris-dim, deep-teal-dim, deep-iris-dim, ember-dim, success, error, error-light]
related: [identity, dark-mode, accessibility, charts, maps]
---

# Color

## Principles

Color encodes meaning, never decoration. Backgrounds are warm neutrals (Shell scale), text is Ink, and accents are reserved for semantic roles — status, category, severity. Every accent token earns its place by carrying a meaning. If a color is not encoding something, it should not be there.

## Tokens / Values

### Core Palette

| Token | Name | Hex | Usage |
|-------|------|-----|-------|
| `shell` | Shell | `#F5F3EE` | Primary background |
| `shell-warm` | Shell Warm | `#EDE9E1` | Surface offset, hover states |
| `shell-cool` | Shell Cool | `#F9F8F5` | Secondary surfaces |
| `ink` | Ink | `#111111` | Primary text |
| `ink-light` | Ink Light | `#2A2A2A` | Secondary text |
| `ink-muted` | Ink Muted | `#6B6B6B` | Supporting text, labels |
| `ink-faint` | Ink Faint | `#9E9E9E` | Placeholder, disabled text |
| `surface` | Surface | `#FFFFFF` | Cards, panels, modals |
| `border` | Border | `#D5D0C7` | Default borders |
| `border-light` | Border Light | `#E5E1DA` | Subtle dividers |

### Accent Palette

| Token | Name | Hex | Role |
|-------|------|-----|------|
| `sand` | Sand | `#E8D4C0` | Warm accent, highlights |
| `sand-light` | Sand Light | `#F0E2D4` | Hover/active on sand elements |
| `sand-dark` | Sand Dark | `#C4A98A` | Sand text on light backgrounds |
| `iris` | Iris | `#8071BC` | Brand accent, interactive elements |
| `iris-light` | Iris Light | `#A498D0` | Hover/active on iris elements |
| `iris-dark` | Iris Dark | `#635499` | Iris text, emphasis |
| `deep-teal` | Deep Teal | `#1A3A34` | Primary action, strong emphasis |
| `deep-teal-light` | Deep Teal Light | `#2A5249` | Hover on deep-teal |
| `deep-iris` | Deep Iris | `#4A3F6B` | Secondary action |
| `deep-iris-light` | Deep Iris Light | `#5E5280` | Hover on deep-iris |
| `ember` | Ember | `#CA5D0F` | Alerts, warnings, attention |
| `ember-light` | Ember Light | `#E07B33` | Hover on ember |
| `ember-dark` | Ember Dark | `#A84B0C` | Ember emphasis |

### Dim Variants

Use for subtle backgrounds behind accent-colored elements:

| Token | Value |
|-------|-------|
| `sand-dim` | `rgba(232, 212, 192, 0.25)` |
| `iris-dim` | `rgba(128, 113, 188, 0.12)` |
| `deep-teal-dim` | `rgba(26, 58, 52, 0.10)` |
| `deep-iris-dim` | `rgba(74, 63, 107, 0.10)` |
| `ember-dim` | `rgba(202, 93, 15, 0.10)` |

### Status Colors

| Token | Hex | Use |
|-------|-----|-----|
| `success` | `#3BAA7F` | Confirmed-positive states only |
| `error` | `#B83A2A` | Errors, critical states |
| `error-light` | `#D05454` | Lighter error variant |

## Semantic Assignment Rules

Don't pick colors for aesthetics — assign them by meaning:

- **Backgrounds**: Always `shell` or `surface`. Never a raw accent color.
- **Primary actions** (buttons, links): `deep-teal` with `deep-teal-light` on hover.
- **Brand / interactive highlights**: `iris`.
- **Warnings / urgency**: `ember`. Reserve red-range colors strictly for error or critical states.
- **Success / positive**: `success` (#3BAA7F). Use sparingly, only for confirmed-positive states.
- **Error / critical**: `error` (#B83A2A) or `error-light` (#D05454).
- **Categorical data**: When color-coding categories, draw from the accent palette in this order: `deep-teal`, `ember`, `iris`, `sand-dark`, `deep-iris`. Never invent new colors.

## Examples

Primary button:

```css
.btn-primary {
  background: var(--deep-teal);
  color: var(--surface);
}
.btn-primary:hover { background: var(--deep-teal-light); }
```

Iris badge using a dim background + dark accent text:

```css
.badge-iris {
  background: var(--iris-dim);
  color: var(--iris-dark);
}
```

## Don'ts

- Don't use colors not in this palette. No `#333`, no `gray-500`, no `blue-600`.
- Don't reference raw hex values in component code — always reference token names.
- Don't use red outside `error` / `error-light`.
- Don't invent additional categorical colors when more than 5 are needed; use lighter/darker variants of existing accents instead.
- Don't apply accent colors directly to large background surfaces — use `surface` or a dim variant.
