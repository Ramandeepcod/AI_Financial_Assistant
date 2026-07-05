"""
API Client

Handles communication with the FastAPI backend.
"""

import requests

API_URL = "http://127.0.0.1:8000/ask"
STATS_URL = "http://127.0.0.1:8000/stats"


def ask_ai(question: str) -> dict:
    """
    Send a question to the FastAPI backend.

    Args:
        question: User's financial question.

    Returns:
        Dictionary containing the AI answer and sources.
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

        return response.json()

    except Exception as e:

        return {
            "answer": f"Error: {e}",
            "sources": []
        }


def get_statistics():
    """
    Fetch dashboard statistics from the backend.
    """

    try:
        response = requests.get(
            STATS_URL,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except Exception:

        return None
