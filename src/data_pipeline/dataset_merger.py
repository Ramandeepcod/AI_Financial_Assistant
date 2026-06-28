import json
from pathlib import Path

INPUT_DIR = Path("data/structured")
OUTPUT_DIR = Path("data/master")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

master_dataset = []

for file in INPUT_DIR.glob("*_news.json"):

    with open(file, "r", encoding="utf-8") as f:
        articles = json.load(f)

    master_dataset.extend(articles)

with open(
    OUTPUT_DIR / "master_news_dataset.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(master_dataset, f, indent=4)

print(
    f"Master dataset created with "
    f"{len(master_dataset)} articles"
)
