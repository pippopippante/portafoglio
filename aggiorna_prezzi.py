"""Scarica da Yahoo Finance i prezzi dei titoli in portfolio.json e di quelli in confronti.json e scrive dati.js.
È uno script e non un .json così index.html funziona anche aperto col doppio clic, senza server.
Lo lancia GitHub Actions: se un titolo del portafoglio fallisce, la pubblicazione si ferma e resta online
la versione precedente; se fallisce un titolo da confrontare, sparisce solo lui dal menu."""
import datetime as dt
import json
import time
import urllib.request
from urllib.parse import quote


def fetch(symbol, start, interval):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{quote(symbol)}"
           f"?period1={start}&period2={int(time.time())}&interval={interval}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.load(urllib.request.urlopen(req, timeout=30))["chart"]["result"][0]


def pairs(r, key):
    return [[key(t), round(c, 4)]
            for t, c in zip(r.get("timestamp", []), r["indicators"]["quote"][0]["close"]) if c is not None]


def chart(symbol, since):
    start = int(dt.datetime.combine(since, dt.time(), dt.timezone.utc).timestamp())
    r = fetch(symbol, start, "1d")
    meta, off = r["meta"], r["meta"]["gmtoffset"]
    day = lambda t: dt.datetime.fromtimestamp(t + off, dt.timezone.utc).date().isoformat()
    out = {
        "name": meta.get("longName") or meta.get("shortName") or symbol,
        "currency": meta["currency"],
        "price": meta["regularMarketPrice"],
        "points": pairs(r, day),
    }
    # ultimi 8 giorni ogni 15 minuti, per i grafici "1G" e "1S"; ora UTC, es. 2026-09-29T12:45Z
    try:
        ri = fetch(symbol, int(time.time()) - 8 * 86400, "15m")
        out["intraday"] = pairs(ri, lambda t: dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"))
    except Exception as e:
        print(f"{symbol}: niente prezzi ogni 15 minuti ({e})")
    return out


with open("portfolio.json", encoding="utf-8") as f:
    portfolio = json.load(f)
with open("confronti.json", encoding="utf-8") as f:
    confronti = json.load(f)

prices = {}
for pos in portfolio:
    first = min(dt.date.fromisoformat(b["date"]) for b in pos["buys"])
    try:
        prices[pos["symbol"]] = chart(pos["symbol"], first - dt.timedelta(days=365))  # un anno di contesto prima
    except Exception as e:
        raise SystemExit(f"{pos['symbol']}: {e}")

# i titoli da confrontare coprono tutto il periodo dei grafici del portafoglio
since = min(dt.date.fromisoformat(b["date"]) for pos in portfolio for b in pos["buys"]) - dt.timedelta(days=365)
compare = []
for c in confronti:
    if c["symbol"] in prices:
        continue
    try:
        prices[c["symbol"]] = chart(c["symbol"], since)
        compare.append(c)
    except Exception as e:
        print(f"{c['symbol']}: saltato ({e})")

dati = {"updated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "portfolio": portfolio, "prices": prices, "compare": compare}
with open("dati.js", "w", encoding="utf-8") as f:
    f.write("window.DATI = " + json.dumps(dati, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("Aggiornati:", ", ".join(prices))
