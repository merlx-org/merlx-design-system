---
title: Empty States
category: components
tokens: [ink-light, ink-muted, text-lg, text-sm]
related: [typography, voice-and-content, empty-error-success]
---

# Empty States

## Principles

An empty state is a result, not a waiting room. It tells the user — calmly — that there is nothing here yet, and ideally what to do next. One line of editorial heading, one line of plain description. No illustrations, no decorative icons.

## Tokens / Values

| Element | Token / Value |
|---|---|
| Heading font | DM Serif Display italic, `text-lg`, `ink-light` |
| Description font | Inter 400, `text-sm`, `ink-muted` |
| Alignment | center |
| Heading length | one line |
| Description length | one line |
| Optional CTA | one Secondary button below the description, never two |
| Vertical padding | `space-12` top and bottom |

## Semantic Assignment Rules

- **DM Serif Display italic only.** This is the design system's editorial signature voice. No Inter, no DM Serif regular.
- **Sentence case.** The heading is a calm sentence, not a marketing line.
- **Direct phrasing.** "No indicators yet." beats "There are no indicators to display." Cut the qualifiers.
- **Single CTA, optional.** "Add an indicator" — a Secondary button. Never two stacked actions; never a primary button without a clear next step.

## Examples

A no-results table state:

```html
<div class="empty-state">
  <h3>Nothing matches.</h3>
  <p>Try a broader query or clear the filters.</p>
</div>
```

```css
.empty-state {
  text-align: center;
  padding: var(--space-12) 0;
}
.empty-state h3 {
  font-family: "DM Serif Display", Georgia, serif;
  font-style: italic;
  font-size: var(--text-lg);
  color: var(--ink-light);
}
.empty-state p {
  font: 400 var(--text-sm) Inter, system-ui, sans-serif;
  color: var(--ink-muted);
}
```

A no-data dashboard state with CTA:

```html
<div class="empty-state">
  <h3>No indicators yet.</h3>
  <p>Add an indicator to start tracking.</p>
  <button class="btn-secondary">Add an indicator</button>
</div>
```

## Don'ts

- Don't use illustrations or large icons (more than 32px).
- Don't stack two calls-to-action.
- Don't use Inter for the heading — DM Serif Display italic is the rule.
- Don't write the heading in marketing voice ("Get started!", "Welcome aboard!").
- Don't use ALL CAPS or exclamation marks.
- Don't show an empty state during loading (use a skeleton from `loading-and-skeletons.md`).
