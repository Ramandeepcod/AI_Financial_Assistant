"""
RAG Pipeline Module

Coordinates document retrieval and answer generation
using the retrieval-augmented generation (RAG) workflow.
"""

from .retriever import retrieve_documents
from .llm import generate_answer


def rag_answer(question: str, model_gemini) -> str:
    """
    Generate an answer for a user's question using RAG.

    Args:
        question: User's question.
        model_gemini: Initialized Gemini model.

    Returns:
        AI-generated answer.
    """

    documents = retrieve_documents(question, top_k=3)

    context = "\n".join(
        [doc["text"] for doc in documents]
    )

    answer = generate_answer(
        question,
        context,
        model_gemini
    )

    return answer