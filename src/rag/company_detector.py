"""
Company Detector

Detects company names and ticker symbols
mentioned in a user's question.
"""

import re

# Company aliases
COMPANY_MAP = {
    "apple": "AAPL",
    "aapl": "AAPL",

    "microsoft": "MSFT",
    "msft": "MSFT",

    "tesla": "TSLA",
    "tsla": "TSLA",

    "nvidia": "NVDA",
    "nvda": "NVDA",

    "alphabet": "GOOGL",
    "google": "GOOGL",
    "googl": "GOOGL",

    "amazon": "AMZN",
    "amzn": "AMZN",

    "meta": "META",
    "facebook": "META",

    "netflix": "NFLX",
    "nflx": "NFLX",

    "amd": "AMD",

    "intel": "INTC",
    "intc": "INTC"
}


def detect_companies(question: str) -> list[str]:
    """
    Detect company ticker symbols from a user question.

    Args:
        question: User question.

    Returns:
        List of detected ticker symbols.
    """

    question = question.lower()

    detected = []

    for keyword, ticker in COMPANY_MAP.items():

        if re.search(rf"\b{re.escape(keyword)}\b", question):

            if ticker not in detected:
                detected.append(ticker)

    return detected
