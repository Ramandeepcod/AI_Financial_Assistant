"""
RAG Pipeline Module

Coordinates document retrieval and answer generation
using the Retrieval-Augmented Generation (RAG) workflow.
"""

from .retriever import retrieve_documents
from .llm import generate_answer


def rag_answer(question: str) -> str:
    """
    Generate an answer for a user's question using RAG.

    Args:
        question: User's question.

    Returns:
        AI-generated answer.
    """

    # Retrieve relevant documents
    documents = retrieve_documents(question, top_k=3)

    # Handle empty retrieval
    if not documents:
        return (
            "I couldn't find any relevant financial news "
            "to answer your question."
        )

    # Build context from retrieved documents
    context = "\n".join(
        doc["text"] for doc in documents
    )

    # Generate answer using Gemini
    answer = generate_answer(
        question=question,
        context=context
    )

    return answer