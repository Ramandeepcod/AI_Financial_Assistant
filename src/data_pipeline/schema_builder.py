import json
from pathlib import Path

INPUT_DIR = Path("data/validated")
OUTPUT_DIR = Path("data/structured")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for file in INPUT_DIR.glob("*_news.json"):

    ticker = file.stem.split("_")[0].upper()

    with open(file, "r", encoding="utf-8") as f:
        articles = json.load(f)

    structured_articles = []

    for article in articles:

        structured_articles.append(
            {
                "ticker": ticker,
                "title": article["title"],
                "link": article["link"],
                "source": "Yahoo Finance"
            }
        )

    output_file = OUTPUT_DIR / file.name

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(structured_articles, f, indent=4)

    print(
        f"{ticker}: "
        f"{len(structured_articles)} structured articles"
    )
