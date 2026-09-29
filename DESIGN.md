---
name: Il mio portafoglio
description: Private portfolio tracker in the style of a broker app, light or dark following the phone.
colors:
  bg: "#ffffff"
  raise: "#f2f3f5"
  ink: "#0d0f14"
  ink-2: "#5b616e"
  ink-3: "#8c929e"
  rule: "#e7e9ed"
  up: "#0a7c43"
  down: "#c8303b"
  bg-dark: "#000000"
  raise-dark: "#15171c"
  ink-dark: "#f2f3f5"
  ink-2-dark: "#999fac"
  ink-3-dark: "#626873"
  rule-dark: "#1f2228"
  up-dark: "#3ccb82"
  down-dark: "#ff6b70"
  compare: "#2f63f0"
  compare-dark: "#7c9cff"
typography:
  figure:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "clamp(38px, 9vw, 54px)"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.035em"
  title:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "clamp(26px, 5vw, 34px)"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  section:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "21px"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.5
  caption:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  row: "10px"
  pill: "999px"
spacing:
  gutter: "16px"
  row: "14px"
  section: "44px"
components:
  range-button:
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "9px 14px"
  range-button-active:
    backgroundColor: "{colors.raise}"
    textColor: "{colors.ink}"
  position-row:
    rounded: "{rounded.row}"
    padding: "14px 12px"
  position-row-hover:
    backgroundColor: "{colors.raise}"
---

# Design System: Il mio portafoglio

## Overview

**Creative North Star: "The broker's own screen"**

The site looks like the owner's broker app (Trade Republic), with the column discipline of a bank statement. One big number at the top, a clean line chart under it, and positions as ruled rows. Nothing decorates the data: no cards, no shadows, no illustration. Color exists only to say gain or loss. The theme follows the phone: light is the default because dark text on a light ground reads better ([NN/g](https://www.nngroup.com/articles/dark-mode/)), and dark matches the broker app at night.

**Key Characteristics:**
- A big figure whose decimals are set smaller, and which follows the finger on the chart.
- Monochrome ink line charts with no tooltip box: the header is the readout.
- Ruled rows, right-aligned tabular figures, a true minus sign.
- Light and dark from the same tokens, switched by `prefers-color-scheme`.

## Colors

### Primary
- **Ink** (`#0d0f14` / dark `#f2f3f5`): text, the price and value lines, the scrub dot, the active range pill.

### Neutral
- **Ground** (`#ffffff` / dark `#000000`): the whole page. There are no panels on top of it.
- **Raise** (`#f2f3f5` / dark `#15171c`): row hover and the active range pill only.
- **Ink 2** (`#5b616e` / dark `#999fac`): labels, captions, axis ticks, dates in the delta line.
- **Ink 3** (`#8c929e` / dark `#626873`): graphics only: the invested line, the average-price line, the price line outside the holding period, the crosshair.
- **Rule** (`#e7e9ed` / dark `#1f2228`): hairlines between rows and around the stats band, chart grid.

### Semantic
- **Up** (`#0a7c43` / dark `#3ccb82`) and **Down** (`#c8303b` / dark `#ff6b70`), with 14–20% fills of the same hue fading to transparent under the chart line.
- **Compare** (`#2f63f0` / dark `#7c9cff`): only the second line of a comparison, its swatch and the compare pill when active.

### Named Rules
**The Sign Rule.** Gain and loss always carry a `+` or a true minus `−` as well as their color; color is never the only signal.
**The Money-Only Color Rule.** Green and red are reserved for gain and loss. The only other hue is the comparison blue.

## Typography

**Font:** Hanken Grotesk (400, 500, 600, 700) from Google Fonts, system-ui as fallback. Its figures are tabular by default, and its punctuation stays proportional, so `1.991,24 €` stays tight while columns still line up.

### Hierarchy
- **Figure** (600, 38–54px, -0.035em): the portfolio value or the security price. The decimals and currency are set in a `<small>` at 0.55em.
- **Title** (600, 26–34px): the security name on its page.
- **Section** (600, 21px): Posizioni, Vendute, La tua posizione, Movimenti.
- **Body** (400, 15px): row names at 600, values.
- **Caption** (400, 13px, ink 2): column heads, sublines, legend, stamp, footnote.

### Named Rules
**The Tabular Rule.** `font-variant-numeric: tabular-nums` on the whole body; every number column is right-aligned.

## Layout

Single column, max 1040px, 16px gutter. The header block (label or title, figure, delta line), then the chart at 320px (250px on phone), then the range pills and the legend on one line, then a stats band between two hairlines (3 columns, 2 on phone), then the sections. Sections sit 44px apart; a heading directly followed by a stats band tightens to 12px.

Below 720px, the position rows drop to name plus value, with the percentage under the value; the quantity column of the movements table is hidden because it is an estimate.

## Elevation & Depth

Flat. No shadows anywhere. Separation comes from hairlines and from the raise tint on hover.

## Shapes

Rows hover with a 10px radius; range buttons are pills. Everything else is square to the page.

## Components

### Range pills
Text buttons (`1M 3M 6M 1A Max`) with `aria-pressed`. Only ranges shorter than the available data are shown, plus Max. The active one sits on the raise tint.

### Position row
A whole-row link on a CSS grid set by `--cols`: name (600) with `type · symbol` under it; price; value (600); weight as a percentage over a 2px bar (ink on rule); return in € with % under it, colored. Hairlines between rows are inset 12px and disappear around the hovered row.

### Stats band
A `<dl>` grid between two hairlines: caption label, 17px/600 value.

### Charts (signature)
Chart.js line, no animation, no tooltip box, no grid, no y axis. Dragging a finger or the mouse moves a crosshair and dots, and the header figure and delta line show that moment; the delta line is fixed at one line height (nowrap, ellipsis) so nothing below it moves. `touch-action: none` on the canvas.
- **Periods:** 1G 1S (15-minute prices) and 1M 3M 6M 1A Max (daily closes); only periods the data covers are shown. X labels sit at the start of each hour, day or month.
- **Line color:** green or red by the change over the period, with a gradient of the same hue underneath. The y range hugs the data; the period high and low are written on the chart, and dashed reference lines carry their label at the right end. Canvas labels have a 4px halo in the ground color.
- **Portfolio:** value line plus invested as a dashed ink 3 step line (daily periods only). Sold positions leave both on the day of sale.
- **Security:** price line in color inside the holding period with the gradient only there, ink 3 outside; dashed average price (daily periods only); a dot on each buy and sale, and while the finger is on it the event is written above the plot, not in the header.
- **Compare:** a native select ("Confronta con…": own securities, then indices and other stocks from `confronti.json`). Both lines switch to % from the start of the period, main in ink, comparison in blue, dotted 0% baseline. The portfolio uses a time-weighted return so deposits never count as gains.

### Name transition
A View Transition moves the tapped row's name into the security title and back.

## Do's and Don'ts

### Do:
- **Do** let the header figure be the chart readout, and keep the header the same height while scrubbing.
- **Do** show the invested line on any portfolio value chart, so deposits never read as gains.
- **Do** keep estimates labeled as estimates (Quote (stima), the footnote).

### Don't:
- **Don't** add cards, shadows, gradients or icons beside the data.
- **Don't** use green or red for anything other than gain and loss.
- **Don't** set punctuation tabular: a font whose `tnum` widens `.` and `,` makes figures look typed.
