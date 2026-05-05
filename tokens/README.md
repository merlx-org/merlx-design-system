# Tokens

Reserved for Stage 2. This folder will hold:

- `tokens.json` — W3C Design Tokens Community Group format with light + dark value modes
- `tokens.css` — CSS custom properties (`:root` light + `[data-theme="dark"]` overrides)
- `tokens.ts` — Typed TypeScript export

Until then, treat token names from the chunks (e.g., `shell`, `ink`, `iris`, `space-8`, `radius-md`) as the canonical interface. Hex / px / ms values are documented in the relevant `foundations/` chunk. The full dark-mode value mapping is in `patterns/dark-mode.md`.
