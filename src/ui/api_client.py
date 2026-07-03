"""
API Client

Handles communication with the FastAPI backend.
"""

import requests

API_URL = "http://127.0.0.1:8000/ask"


def ask_ai(question: str) -> str:
    """
    Send a question to the FastAPI backend.

    Args:
        question: User's financial question.

    Returns:
        AI-generated answer.
    """

    payload = {
        "question": question
    }

    try:
        response = requests.post(
            API_URL,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        return response.json()["answer"]

    except Exception as e:
        return f"Error: {e}"