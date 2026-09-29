# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS/JS in a single index.html (Chart.js from a CDN), hosted on GitHub Pages. A GitHub Action (aggiorna_prezzi.py) fetches prices from Yahoo Finance and writes dati.js at every publish, hourly Monday to Friday. The user explicitly does not want a program running locally.

## Users

One person: the owner of a small Trade Republic account (about €2,000 in ETFs, one Italian stock and a little Bitcoin). They look at it from their phone and their PC, in Italian.

## Product Purpose

Trade Republic shows a performance chart only for the whole portfolio. This site shows each position on its own: how that security has moved since the day it was bought, with the holding period highlighted on the chart. Success = at a glance, the owner sees how each thing they bought is doing since they bought it.

## Positioning

The chart for a single security, centered on the owner's own purchase history (buy dates, average price, holding period, and sales) instead of the market's.

## Operating Context

The owner opens the site now and then to check how things are going, mostly on the phone. The data comes from Trade Republic transaction screenshots, which Claude transcribes into portfolio.json.

## Capabilities and Constraints

- Home page: current value with the total gain, a chart of portfolio value against money invested (range 1M/3M/Max), a table of current holdings with weight and return, a table of sold securities.
- Dragging on any chart shows that day's figures in the header.
- Detail page per security: chart from one year before the first buy to today, holding period highlighted, a dot on each buy and sale, a line at the average price, the list of buys.
- Prices are daily closes plus the last price at update time; the page shows when they were last updated.
- Quantities are estimated from the amount paid and that day's closing price (€1 fee included in the amount invested).
- Totals are summed in EUR, with no currency conversion.

## Evidence on Hand

Real holdings in portfolio.json (VWCE, iShares Physical Gold, Amundi Stoxx Europe 600, Bitcoin, iShares S&P 500, Poste Italiane; NVIDIA sold). There are no logos or brand assets.

## Product Principles

- The truth of the numbers comes before anything else: never figures that look more precise than they are.
- Gain or loss must be readable instantly, and never by color alone.
- It is a private tool: no marketing, no onboarding, no decoration getting in the way of the data.

## Brand Commitments

- The look is a broker app's (reference: Trade Republic), played straight. The owner rejected the sticker-album concept as amateurish.
- Light or dark follows the phone's setting.
