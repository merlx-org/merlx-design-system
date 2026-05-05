---
title: Dark Mode
category: patterns
tokens: [shell, shell-warm, shell-cool, ink, ink-light, ink-muted, ink-faint, surface, border, border-light, iris, iris-dark, iris-dim, deep-teal, deep-teal-light, deep-teal-dim, ember, ember-dark, ember-dim, sand, sand-dark, success, error]
related: [color, accessibility, identity]
---

# Dark Mode

## Principles

Dark mode is a value remap, not a parallel palette. Tokens keep their semantic names (`surface`, `ink`, `border`); only the values flip per theme. Components do not change between modes. Implementation is one CSS variable override on a `data-theme="dark"` attribute on `<html>`.

## Tokens / Values

| Token | Light value | Dark value |
|---|---|---|
| `shell` | `#F5F3EE` | `#15140F` |
| `shell-warm` | `#EDE9E1` | `#1F1D17` |
| `shell-cool` | `#F9F8F5` | `#191814` |
| `ink` | `#111111` | `#F0EEE7` |
| `ink-light` | `#2A2A2A` | `#D9D6CD` |
| `ink-muted` | `#6B6B6B` | `#9A968B` |
| `ink-faint` | `#9E9E9E` | `#6B6862` |
| `surface` | `#FFFFFF` | `#22201A` |
| `border` | `#D5D0C7` | `#3A372F` |
| `border-light` | `#E5E1DA` | `#2C2A24` |
| `iris` | `#8071BC` | `#A498D0` |
| `iris-dark` | `#635499` | `#8071BC` |
| `iris-dim` | `rgba(128, 113, 188, 0.12)` | `rgba(164, 152, 208, 0.18)` |
| `deep-teal` | `#1A3A34` | `#3FAA9B` |
| `deep-teal-light` | `#2A5249` | `#5BC2B3` |
| `deep-teal-dim` | `rgba(26, 58, 52, 0.10)` | `rgba(63, 170, 155, 0.15)` |
| `ember` | `#CA5D0F` | `#E07B33` |
| `ember-dark` | `#A84B0C` | `#CA5D0F` |
| `ember-dim` | `rgba(202, 93, 15, 0.10)` | `rgba(224, 123, 51, 0.18)` |
| `sand` | `#E8D4C0` | `#5C4D3E` |
| `sand-dark` | `#C4A98A` | `#A88E70` |
| `success` | `#3BAA7F` | `#5FCFA0` |
| `error` | `#B83A2A` | `#D9554A` |

(Other tokens — `iris-light`, `deep-iris`, `deep-iris-light`, `ember-light`, `sand-light`, `error-light`, `sand-dim`, `deep-iris-dim` — follow the same approach: shift values to maintain ~equivalent perceived contrast in both modes. Stage 2's `tokens.json` will codify all mappings.)

## Semantic Assignment Rules

- **Theme switch is a `data-theme="dark"` attribute on `<html>`.** Token values are CSS custom properties; the dark theme overrides their values, never the component CSS.
- **Components do not change between modes.** Only token values flip.
- **Respect `prefers-color-scheme` as a default**, but always offer a user toggle that overrides it.
- **Persist the user's choice** (localStorage). Sync across tabs.
- **Inverted tokens shift but keep semantics.** `surface` is still the card background — it just becomes `#22201A` instead of `#FFFFFF`.

## Examples

Token override with a theme attribute:

```css
:root {
  --shell: #F5F3EE;
  --ink: #111111;
  --surface: #FFFFFF;
  --iris: #8071BC;
  /* …all light tokens… */
}

[data-theme="dark"] {
  --shell: #15140F;
  --ink: #F0EEE7;
  --surface: #22201A;
  --iris: #A498D0;
  /* …all dark tokens… */
}
```

Theme toggle (with persistence):

```ts
const apply = (theme: "light" | "dark") => {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("merlx-theme", theme);
};

const initial = localStorage.getItem("merlx-theme") as "light" | "dark" | null;
if (initial) {
  apply(initial);
} else if (matchMedia("(prefers-color-scheme: dark)").matches) {
  apply("dark");
}
```

## Don'ts

- Don't switch by `prefers-color-scheme` without offering a manual toggle.
- Don't introduce dark-mode-only tokens (e.g., `dark-surface`). Tokens are semantic; values flip per theme.
- Don't write component CSS that branches on theme. Use the token; let it flip.
- Don't change radius, spacing, or motion tokens between themes — only color.
- Don't render a separate "dark theme" component variant.
- Don't omit dark-mode contrast verification — every text-on-background pair must still meet WCAG AA in dark mode.
