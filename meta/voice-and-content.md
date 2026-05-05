---
title: Voice and Content
category: meta
tokens: []
related: [identity, empty-states, notifications, forms]
---

# Voice and Content

## Principles

Write for an analyst, not a marketer. Calm, specific, short. Avoid promotional adjectives ("powerful," "seamless," "robust"). State what the thing does, not how good it is. The product is for people who care about the data — they do not need to be hyped.

## Tokens / Values

No tokens — this chunk is content guidance.

### Capitalization

- **Sentence case** for all UI text — headings, buttons, labels, menu items, tooltips, empty states.
- **Uppercase reserved for small section labels** at `text-xxs` only (sidebar section headers, table column headers).
- **Never ALL CAPS** for buttons, page titles, modal titles, or marketing copy.

### Microcopy reference

| Surface | Pattern | Example |
|---|---|---|
| Button (primary action) | Verb + noun | "Save changes", "Run analysis" |
| Button (cancel) | Just "Cancel" | "Cancel" |
| Button (destructive) | Specific verb | "Delete indicator", not "Yes" |
| Empty state heading | Direct, italic | "No indicators yet." |
| Empty state body | What to do next | "Add an indicator to start tracking." |
| Error toast title | What happened | "Couldn't load the dashboard." |
| Error body | Naming the fix | "The Aperture data feed timed out. Try again." |
| Success toast | What was done | "Indicator saved." |
| Form label | Noun | "Project name" |
| Form helper text | Explain the field | "Used to label exports." |
| Form error | Name the fix | "Enter at least 3 characters." |
| Tooltip | One short fragment | "Operationalised under indicator IND-204" |

### Numbers and dates

- **Tabular contexts** (tables, dense data, stat tiles) — IBM Plex Mono.
- **Dense tables** — ISO 8601 dates (`2026-05-05`).
- **Editorial / report contexts** — long-form dates (`5 May 2026`).
- **Never use ambiguous formats** like `5/5/26` (US vs ISO collision).
- **Currency** — symbol-prefixed, mono font in tabular contexts.
- **Percentages** — IBM Plex Mono with a hair-space before `%`.
- **Negative numbers** — leading minus, no parentheses.

## Semantic Assignment Rules

- **Sentence case for everything** that is not a small section label.
- **No exclamation marks.** Calm voice across success, empty, error.
- **No "please" in errors.** It sounds servile and adds no information.
- **No apologies** — say what happened, not "Sorry, something went wrong."
- **No "the user" copy in second person.** "Click here" → "Save changes" / "Run analysis."
- **No emoji in product UI.** Reserve emoji for editorial moments (e.g., a published RIKO essay), never inside MERLx tools.
- **Pair every state with a clear next action** when one exists. Empty → CTA. Error → retry. Success → close.
- **Direct phrasing.** Cut hedges and qualifiers. "There are no indicators to display." → "No indicators yet."

## Examples

**Empty state:**

> No indicators yet.
>
> Add an indicator to start tracking.

**Error toast:**

> Couldn't load this chart.
>
> The Aperture data feed timed out. Retry?

**Success toast:**

> Indicator saved.

**Form helper:**

> Used to label exports.

**Form error:**

> Enter at least 3 characters.

**Confirmation modal:**

> Delete this indicator?
>
> This removes all linked observations. This cannot be undone.
>
> [ Cancel ] [ Delete indicator ]

## Don'ts

- Don't write in marketing voice. "Powerful new dashboard!" has no place here.
- Don't use exclamation marks.
- Don't use "please" in errors or warnings.
- Don't apologize on the user's behalf or your own ("Sorry, something went wrong").
- Don't use emoji in MERLx product UI.
- Don't write to "the user" — write to the actual user, second person sparingly.
- Don't use ambiguous date formats (`5/5/26`).
- Don't capitalize button labels (sentence case always).
