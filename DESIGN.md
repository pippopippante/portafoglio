# Design: Panini sticker album

The portfolio is a sticker album. Every holding is a sticker; its "photo" is the price trace since the purchase. Everything lives in `index.html`: tokens on `:root`, a single page.

## Palette (`:root`)

| Token | Value | Role |
|---|---|---|
| `--page` | `#1d3cb8` | album page (ultramarine blue + 7px white halftone at 7%) |
| `--on-page` / `--on-page-2` | `#fff` / `#c9d3ff` | text on the blue page |
| `--paper` | `#fff` | stickers and printed panels |
| `--ink` / `--ink-2` / `--ink-3` | `#0c1541` / `#4b5479` / `#a3aac6` | text, secondary labels, chart line outside the holding period |
| `--rule` | `#d9dcea` | table rules, dotted leaders, chart grid |
| `--etf` `--azioni` `--crypto` `--venduti` | `#ffc81e` `#ff7a45` `#b89cff` `#cdd1de` | team colors: sticker field, team band, holding-period band on the chart |
| `--up` / `--down` | `#0b7a35` / `#c42b2b` | gain and loss, always with a +/− sign as well |

Only light theme: it's paper. Color lives in fields and bands; text is always ink or white.

## Type

- **Barlow Condensed 800**, uppercase: titles, sticker numbers, name plates, team bands, band label on the chart.
- **Barlow 400–700**: everything else. Numbers always `tabular-nums`.

## Components

- **Sticker** (`.sticker`): white card, 8px radius, 7px margin, tilted by hand (`--tilt` from `TILTS`, by number). Team-colored field with the two-digit number at 38px and the SVG portrait (holding period only, dashed line at the average price). Navy plate with the name in caps and the symbol. Value and % gain at the bottom. When sold: gray field and a navy "VENDUTA" stamp.
- **Team band** (`.band`): team-color strip with the name in caps and the sticker count. Teams sit side by side: each spans as many columns as it has stickers (4 max, 2 on phone).
- **Printed panel** (`.card`) with **dotted leaders** (`.facts`): the portfolio card and the security card.
- **Chart**: navy line inside the holding period, `--ink-3` outside; team-colored band at 40% with an uppercase label above the plot area; navy dots with a white ring on buys and sales; dashed average price.

## Motion

- On first open the stickers "stick" (`@keyframes stick`, staggered by 50 ms, exponential ease-out; content stays visible).
- On hover a sticker straightens and lifts.
- Signature: a View Transition, where the tapped sticker becomes the big one on the security card and flies back when you close it.
- Everything turns off with `prefers-reduced-motion`.
