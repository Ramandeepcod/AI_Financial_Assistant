"""
API request and response models.
"""

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    """
    Request model for asking a financial question.
    """

    question: str


class QuestionResponse(BaseModel):
    """
    Response model returned by the API.
    """

    question: str
    answer: str
    sources: list[str]
