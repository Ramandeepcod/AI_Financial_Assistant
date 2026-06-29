"""
LLM Module

Handles communication with the Gemini Large Language Model
to generate answers from retrieved financial news.
"""
import google.generativeai as genai


def generate_answer(
    question: str,
    context: str,
    model_gemini
) -> str:
    """
    Generate an answer using the Gemini model.

    Args:
        question: User's question.
        context: Retrieved financial news context.
        model_gemini: Initialized Gemini model.

    Returns:
        Generated response as text.
    """

    prompt = f"""
You are a financial research assistant.

Question:
{question}

Relevant News:
{context}

Provide a concise answer based only on the news above.
"""

    try:
        response = model_gemini.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"