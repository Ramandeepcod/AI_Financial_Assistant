"""
Statistics Service

Provides statistics about the financial news dataset.
"""

import json

from src.config import (
    DATASET_PATH,
    LLM_MODEL,
    EMBEDDING_MODEL,
    VECTOR_STORE
)


class StatsService:
    """
    Provides statistics about the financial news dataset.
    """

    def __init__(self):
        """
        Initialize the statistics service.
        """

        with open(DATASET_PATH, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def total_articles(self):
        """
        Return the total number of articles.
        """

        return len(self.data)

    def total_companies(self):
        """
        Return the total number of unique companies.
        """

        tickers = {
            article["ticker"]
            for article in self.data
        }

        return len(tickers)

    def total_sources(self):
        """
        Return the total number of unique news sources.
        """

        sources = {
            article["source"]
            for article in self.data
        }

        return len(sources)

    def get_statistics(self):
        """
        Return all application statistics.
        """

        return {
            "total_articles": self.total_articles(),
            "total_companies": self.total_companies(),
            "total_sources": self.total_sources(),
            "llm_model": LLM_MODEL,
            "embedding_model": EMBEDDING_MODEL,
            "vector_store": VECTOR_STORE
        }
