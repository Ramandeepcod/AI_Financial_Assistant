"""
FastAPI Backend

Entry point for the AI Financial Assistant API.
"""

from fastapi import FastAPI

from src.api.models import QuestionRequest, QuestionResponse
from src.rag.rag_pipeline import rag_answer
from src.services.stats_service import StatsService

stats_service = StatsService()

app = FastAPI(
    title="AI Financial Assistant",
    description="RAG-based Financial News Assistant",
    version="1.0.0",
)


@app.get("/")
def root():
    """
    Root endpoint.
    """
    return {
        "message": "Welcome to AI Financial Assistant API!"
    }


@app.get("/health")
def health():
    """
    Health check endpoint.
    """
    return {
        "status": "healthy"
    }


@app.get("/stats")
def get_statistics():
    """
    Return application statistics.
    """

    return stats_service.get_statistics()


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    """
    Generate an AI answer for a financial question.
    """

    result = rag_answer(
        question=request.question
    )

    return QuestionResponse(
        question=request.question,
        answer=result["answer"],
        sources=result["sources"]
    )
