"""Create deterministic synthetic data for CI-only notebook execution.

This file is not real NIFTY 50 data. It is ignored local test input and must never
be used for financial analysis or committed as a replacement for source data.
"""
import csv
import math
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
output = Path(__file__).resolve().parents[1] / "data" / "NIFTY50_data.csv"
output.parent.mkdir(parents=True, exist_ok=True)

rows = [
    ["Price", "Close", "High", "Low", "Open", "Volume"],
    ["Ticker", "^NSEI", "^NSEI", "^NSEI", "^NSEI", "^NSEI"],
    ["Date", "Close", "High", "Low", "Open", "Volume"],
]
day = date(2020, 1, 1)
price = 10000.0
while len(rows) < 603:
    if day.weekday() < 5:
        price *= 1 + random.gauss(0.0002, 0.01)
        close = max(price, 100.0)
        open_price = close * (1 + random.gauss(0, 0.002))
        high = max(close, open_price) * (1 + abs(random.gauss(0, 0.003)))
        low = min(close, open_price) * (1 - abs(random.gauss(0, 0.003)))
        volume = int(random.uniform(1_000_000, 8_000_000))
        rows.append([
            day.isoformat(),
            f"{close:.4f}",
            f"{high:.4f}",
            f"{low:.4f}",
            f"{open_price:.4f}",
            str(volume),
        ])
    day += timedelta(days=1)

with output.open("w", newline="", encoding="utf-8") as stream:
    csv.writer(stream).writerows(rows)
print(f"Created {len(rows)-3} synthetic rows at {output}; NOT real market data.")
