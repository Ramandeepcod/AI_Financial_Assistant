"""
Retriever Module

Retrieves the most relevant financial news
from the vector store.
"""

from .vector_store import search_news


def retrieve_documents(query: str, top_k: int = 3) -> list:
    """
    Retrieve the most relevant financial news articles.

    Args:
        query: User's search query.
        top_k: Number of documents to retrieve.

    Returns:
        List of retrieved financial news articles.
    """

    return search_news(
        query=query,
        top_k=top_k
    )