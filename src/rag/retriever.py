"""
Retriever Module

Retrieves the most relevant financial news
from the vector store.
"""

from .company_detector import detect_companies
from .vector_store import search_news


def retrieve_documents(query: str, top_k: int = 5) -> list:
    """
    Retrieve the most relevant financial news articles.

    Args:
        query: User's search query.
        top_k: Number of documents to retrieve.

    Returns:
        List of retrieved financial news articles.
    """

    companies = detect_companies(query)

    # Normal semantic search
    if len(companies) <= 1:

        return search_news(
            query=query,
            top_k=top_k
        )

    # -------------------------------------
    # Comparison query
    # -------------------------------------

    # Retrieve more documents
    candidates = search_news(
        query=query,
        top_k=20
    )

    filtered = []

    for company in companies:

        for article in candidates:

            if company.lower() in article["text"].lower():

                filtered.append(article)

    # Remove duplicates
    unique = []

    seen = set()

    for article in filtered:

        if article["text"] not in seen:

            seen.add(article["text"])

            unique.append(article)

    # Fallback
    if not unique:

        return candidates[:top_k]

    return unique[:top_k]
