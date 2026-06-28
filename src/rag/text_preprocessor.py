import json
from pathlib import Path

DATASET_PATH = Path("data/news/master_news_dataset.json")


def prepare_documents():

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        docs = json.load(f)

    processed_docs = []

    for doc in docs:

        text = f"{doc['ticker']} {doc['title']}"

        processed_docs.append(text)

    print(f"Prepared {len(processed_docs)} texts")

    print("\nSample:\n")
    print(processed_docs[0])

    return processed_docs


if __name__ == "__main__":
    prepare_documents()
