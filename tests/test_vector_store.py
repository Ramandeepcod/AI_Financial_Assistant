from src.rag.vector_store import search_news

print("=" * 60)
print("Testing FAISS Vector Store")
print("=" * 60)

results = search_news(
    "What is happening in the stock market?",
    top_k=3
)

print(f"\nRetrieved {len(results)} documents.\n")

for i, result in enumerate(results, start=1):

    print(f"Result {i}")
    print("-" * 40)
    print(f"Distance : {result['distance']}")
    print(result["text"][:300])
    print()