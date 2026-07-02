import json
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer

# Paths
INDEX_PATH = Path("data/embeddings/faiss_index.bin")
TEXTS_PATH = Path("data/embeddings/texts.json")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index(str(INDEX_PATH))

# Load searchable texts
with open(TEXTS_PATH, "r", encoding="utf-8") as f:
    texts = json.load(f)


def search_news(query: str, top_k: int = 5) -> list:
    """
    Search the FAISS index and return the most relevant news.
    """

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in range(top_k):
        results.append(
            {
                "text": texts[indices[0][i]],
                "distance": float(distances[0][i])
            }
        )

    return results