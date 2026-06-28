import feedparser
import json
from pathlib import Path

TICKERS = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA",
    "AMZN",
    "GOOGL",
    "META",
    "AMD",
    "NFLX",
    "JPM"
]

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for ticker in TICKERS:

    rss_url = (
        f"https://feeds.finance.yahoo.com/rss/2.0/headline?"
        f"s={ticker}&region=US&lang=en-US"
    )

    feed = feedparser.parse(rss_url)

    articles = []

    for article in feed.entries:

        articles.append(
            {
                "title": article.title,
                "link": article.link
            }
        )

    output_file = OUTPUT_DIR / f"{ticker.lower()}_news.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4)

    print(f"{ticker}: {len(articles)} articles saved")
