def search_news(query, top_k=5):

    query_embedding = model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    top_indices = np.argsort(
        similarities
    )[::-1][:top_k]

    results = []

    for idx in top_indices:

        results.append(
            {
                "score": float(similarities[idx]),
                "text": texts[idx]
            }
        )

    return results


def rag_answer(question):

    query_embedding = model.encode([question])

    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    top_indices = np.argsort(
        similarities
    )[::-1][:3]

    context = "\n".join(
        [texts[idx] for idx in top_indices]
    )

    prompt = f"""
You are a financial research assistant.

Question:
{question}

Relevant News:
{context}

Provide a concise answer based only on the news above.
"""

    response = model_gemini.generate_content(
        prompt
    )

    return response.text
