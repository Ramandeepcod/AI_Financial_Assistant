"""
API Client

Handles communication with the FastAPI backend.
"""

import os

import requests

# Backend URL
BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://your-backend-url.onrender.com"
)

API_URL = f"{BASE_URL}/ask"
STATS_URL = f"{BASE_URL}/stats"


def ask_ai(question: str) -> dict:
    """
    Send a question to the FastAPI backend.
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
    Fetch dashboard statistics.
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
