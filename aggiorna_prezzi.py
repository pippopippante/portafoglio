"""Scarica da Yahoo Finance i prezzi dei titoli in portfolio.json e scrive dati.js (portafoglio + prezzi).
È uno script e non un .json così index.html funziona anche aperto col doppio clic, senza server.
Lo lancia GitHub Actions: se un titolo fallisce, la pubblicazione si ferma e resta online la versione precedente."""
import datetime as dt
import json
import time
import urllib.request
from urllib.parse import quote


def chart(symbol, since):
    start = int(dt.datetime.combine(since, dt.time(), dt.timezone.utc).timestamp())
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{quote(symbol)}"
           f"?period1={start}&period2={int(time.time())}&interval=1d")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    r = json.load(urllib.request.urlopen(req, timeout=30))["chart"]["result"][0]
    meta, off = r["meta"], r["meta"]["gmtoffset"]
    day = lambda t: dt.datetime.fromtimestamp(t + off, dt.timezone.utc).date().isoformat()
    return {
        "name": meta.get("longName") or meta.get("shortName") or symbol,
        "currency": meta["currency"],
        "price": meta["regularMarketPrice"],
        "points": [[day(t), round(c, 4)]
                   for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c is not None],
    }


with open("portfolio.json", encoding="utf-8") as f:
    portfolio = json.load(f)

prices = {}
for pos in portfolio:
    first = min(dt.date.fromisoformat(b["date"]) for b in pos["buys"])
    try:
        prices[pos["symbol"]] = chart(pos["symbol"], first - dt.timedelta(days=365))  # un anno di contesto prima
    except Exception as e:
        raise SystemExit(f"{pos['symbol']}: {e}")

dati = {"updated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "portfolio": portfolio, "prices": prices}
with open("dati.js", "w", encoding="utf-8") as f:
    f.write("window.DATI = " + json.dumps(dati, ensure_ascii=False) + ";\n")
print("Aggiornati:", ", ".join(prices))
