"""Scarica da Yahoo Finance i prezzi dei titoli in portfolio.json e li salva in prices.json.
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


prices = {}
with open("portfolio.json", encoding="utf-8") as f:
    for pos in json.load(f):
        first = min(dt.date.fromisoformat(b["date"]) for b in pos["buys"])
        try:
            prices[pos["symbol"]] = chart(pos["symbol"], first - dt.timedelta(days=365))  # un anno di contesto prima
        except Exception as e:
            raise SystemExit(f"{pos['symbol']}: {e}")

with open("prices.json", "w", encoding="utf-8") as f:
    json.dump({"updated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "prices": prices}, f)
print("Aggiornati:", ", ".join(prices))
