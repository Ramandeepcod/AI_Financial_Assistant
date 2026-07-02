"""
LLM Module

Handles communication with the Gemini Large Language Model
to generate answers from retrieved financial news.
"""

import google.generativeai as genai

from src.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Gemini Model
MODEL_NAME = "gemini-2.5-flash"
model_gemini = genai.GenerativeModel(MODEL_NAME)


def generate_answer(question: str, context: str) -> str:
    """
    Generate an answer using the Gemini model.

    Args:
        question: User's question.
        context: Retrieved financial news.

    Returns:
        AI-generated response.
    """

    if not context.strip():
        return (
            "I couldn't find relevant financial news "
            "to answer your question."
        )

    prompt = f"""
You are an AI Financial Research Assistant.

Instructions:
- Answer ONLY using the provided financial news.
- Do not make up facts or assumptions.
- If the news does not contain enough information,
  clearly say so.
- Keep the response concise, professional, and easy to understand.

Question:
{question}

Relevant Financial News:
{context}

Answer:
"""

    try:
        response = model_gemini.generate_content(prompt)
        return response.text

    except Exception:
        return (
            "Sorry, I couldn't generate a response at the moment. "
            "Please try again later."
        )