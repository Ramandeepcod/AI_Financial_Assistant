"""
Application Configuration
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from project root
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

    # --------------------------------------------------
# Application Configuration
# --------------------------------------------------

LLM_MODEL = "gemini-2.5-flash"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

VECTOR_STORE = "FAISS"

DATASET_PATH = Path(
    "data/master/master_news_dataset.json"
)
