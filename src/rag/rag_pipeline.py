"""
RAG Pipeline Module

Coordinates document retrieval and answer generation
using the Retrieval-Augmented Generation (RAG) workflow.
"""

from .retriever import retrieve_documents
from .llm import generate_answer


def rag_answer(question: str) -> dict:
    """
    Generate an answer for a user's question using RAG.

    Args:
        question: User's question.

    Returns:
        Dictionary containing the AI-generated answer
        and retrieved source documents.
    """

    # Retrieve relevant documents
    documents = retrieve_documents(
        query=question,
        top_k=3
    )

    # Handle empty retrieval
    if not documents:

        return {
            "answer": (
                "I couldn't find any relevant financial news "
                "to answer your question."
            ),
            "sources": []
        }

    # Build context
    context = "\n".join(
        doc["text"] for doc in documents
    )

    # Generate answer
    answer = generate_answer(
        question=question,
        context=context
    )

    # Extract source texts
    sources = [
        doc["text"]
        for doc in documents
    ]

    return {
        "answer": answer,
        "sources": sources
    }
