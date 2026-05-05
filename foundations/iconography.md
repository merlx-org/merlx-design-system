---
title: Iconography
category: foundations
tokens: []
related: [identity, color, buttons, navigation]
---

# Iconography

## Principles

One icon family across all MERLx products: **Phosphor Icons** (MIT). Phosphor's multi-weight design lets MERLx use Thin as its visual signature while keeping Regular and Fill available for legibility and state contrast. No other icon library may be introduced.

## Tokens / Values

| Context | Weight | Size |
|---|---|---|
| Default UI (buttons, navigation, cards) | Thin (1px) | 16–20px |
| Editorial / hero / empty states | Thin | 24–32px |
| Dense tables, badges, sub-16px contexts | Regular (1.5px) | 12–14px |
| Active / selected / emphasis state | Fill | match outline size |
| Forbidden | Light, Bold, Duotone | — |

Color: icons inherit `currentColor` from their parent text element. Hard-code an icon color only when it carries semantic meaning (e.g., a Fill `warning-circle` taking the `ember` token).

## Semantic Assignment Rules

- **Default = Thin.** Any new icon use starts at Thin, 16–20px.
- **Drop to Regular only when Thin breaks.** Phosphor Thin renders fragile at sub-16px — anti-aliasing dulls the strokes on standard-DPR displays. Switch to Regular for table-row icons, badges, and 12–14px contexts.
- **Fill is for state contrast.** A filled icon paired with an outline icon of the same name reads as "active vs inactive." Never use Fill for decoration alone.
- **Pick semantic icon names.** Use `warning-circle` for warnings, `check-circle` for success, `arrow-up-right` for external links — match Phosphor's name to its meaning.

## Examples

Default UI icon (button):

```tsx
import { ArrowRight } from "phosphor-react";

<button>
  <ArrowRight size={18} weight="thin" />
  Next
</button>
```

Active / inactive contrast:

```tsx
{isActive
  ? <Circle size={16} weight="fill" color="var(--deep-teal)" />
  : <Circle size={16} weight="thin" color="var(--ink-muted)" />}
```

Dense table row:

```tsx
<TrashSimple size={14} weight="regular" />
```

## Don'ts

- Don't introduce a second icon library (Lucide, Heroicons, custom SVG sets).
- Don't use Phosphor Light, Bold, or Duotone weights — they break the visual signature.
- Don't render Thin icons below 16px; switch to Regular.
- Don't hard-code icon colors except for semantic states.
- Don't combine multiple icon weights inside a single component except for outline / Fill state contrast.
