import json
from pathlib import Path

INPUT_DIR = Path("data/raw")
OUTPUT_DIR = Path("data/cleaned")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for file in INPUT_DIR.glob("*_news.json"):


    with open(file, "r", encoding="utf-8") as f:
        articles = json.load(f)

    cleaned_articles = []

    seen_titles = set()

    for article in articles:

        title = article["title"].strip()

        if len(title) < 10:
            continue

        if title in seen_titles:
            continue

        seen_titles.add(title)

        cleaned_articles.append(
            {
                "title": title,
                "link": article["link"]
            }
        )

    output_file = OUTPUT_DIR / file.name

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(cleaned_articles, f, indent=4)

    print(
        f"{file.name}: "
        f"{len(cleaned_articles)} cleaned articles"
    )
