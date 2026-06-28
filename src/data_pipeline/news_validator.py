import json
from pathlib import Path

INPUT_DIR = Path("data/cleaned")
OUTPUT_DIR = Path("data/validated")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for file in INPUT_DIR.glob("*_news.json"):


    with open(file, "r", encoding="utf-8") as f:
        articles = json.load(f)

    valid_articles = []

    for article in articles:

        title = article.get("title", "").strip()
        link = article.get("link", "").strip()

        if not title:
            continue

        if not link.startswith("http"):
            continue

        valid_articles.append(article)

    output_file = OUTPUT_DIR / file.name

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(valid_articles, f, indent=4)

    print(
        f"{file.name}: "
        f"{len(valid_articles)} validated articles"
    )
