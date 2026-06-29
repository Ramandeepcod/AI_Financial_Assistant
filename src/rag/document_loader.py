import json
from pathlib import Path

DATASET_PATH = Path("data/master/master_news_dataset.json")


def load_documents():

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        documents = json.load(f)

    print(f"Loaded {len(documents)} documents")

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print("\nFirst document:\n")
    print(docs[0])
