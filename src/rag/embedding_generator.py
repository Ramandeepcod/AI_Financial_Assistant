import json
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

# Paths
DATASET_PATH = Path("data/master/master_news_dataset.json")
EMBEDDING_PATH = Path("data/embeddings/embeddings.npy")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents():
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def create_texts(documents):
    texts = []

    for doc in documents:
        text = (
            f"{doc['ticker']} "
            f"{doc['title']}"
        )
        texts.append(text)

    return texts


def generate_embeddings(texts):

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    np.save(EMBEDDING_PATH, embeddings)

    print(f"\nSaved embeddings to: {EMBEDDING_PATH}")


def main():

    documents = load_documents()

    texts = create_texts(documents)

    generate_embeddings(texts)


if __name__ == "__main__":
    main()