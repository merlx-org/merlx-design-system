---
title: Radius
category: foundations
tokens: [radius-sm, radius-md, radius-lg, radius-xl, radius-pill]
related: [identity, cards, buttons, badges]
---

# Radius

## Principles

Radius signals scale: smaller surfaces get tighter corners. Pills are reserved for badges, tags, and toggle tracks.

## Tokens / Values

| Token | Value | Use |
|-------|-------|-----|
| `radius-sm` | 4px | Buttons, inputs, small cards |
| `radius-md` | 8px | Cards, panels, modals |
| `radius-lg` | 12px | Large containers, feature cards |
| `radius-xl` | 16px | Hero elements, prominent surfaces |
| `radius-pill` | 100px | Badges, tags, pills, toggle tracks |

## Semantic Assignment Rules

- **Buttons / inputs / small cards** — `radius-sm`.
- **Cards / panels / modals** — `radius-md`.
- **Large containers / feature cards** — `radius-lg`.
- **Hero or prominent surfaces** — `radius-xl`.
- **Badges, tags, pills, toggle tracks** — `radius-pill`.

## Examples

A button:

```css
.btn { border-radius: var(--radius-sm); }
```

A card:

```css
.card { border-radius: var(--radius-md); }
```

A badge:

```css
.badge { border-radius: var(--radius-pill); }
```

## Don'ts

- Don't use `radius-pill` on rectangular elements (text fields, cards).
- Don't invent intermediate values like 6px or 10px.
- Don't apply `radius-xl` to anything smaller than a hero element.
- Don't mix multiple radius tokens within one nested component.
