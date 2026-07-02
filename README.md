# 🤖 AI Financial Assistant

A Retrieval-Augmented Generation (RAG) based AI Financial Assistant that answers financial questions using the latest financial news. The application combines semantic search with Google Gemini to generate accurate, context-aware responses.

---

## 🚀 Features

- 📈 Financial news collection pipeline
- 🧹 Automated data cleaning and validation
- 🔍 Semantic search using Sentence Transformers
- 🗂️ FAISS vector database for fast retrieval
- 🤖 Google Gemini 2.5 Flash for answer generation
- 🌐 FastAPI backend with Swagger documentation
- 💬 Ready for Streamlit chat interface

---

## 🏗️ Architecture

```
                Financial News
                       │
                       ▼
             Data Collection Pipeline
                       │
                       ▼
                Data Cleaning
                       │
                       ▼
            SentenceTransformer
                       │
                       ▼
                 FAISS Index
                       │
      User Question     │
            │           │
            ▼           │
        Retriever ◄─────┘
            │
            ▼
      Relevant Documents
            │
            ▼
      Google Gemini 2.5 Flash
            │
            ▼
        AI Generated Answer
```

---

## 📂 Project Structure

```
AI_Financial_Assistant
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── validated/
│   ├── structured/
│   ├── master/
│   └── embeddings/
│
├── src/
│   ├── api/
│   ├── rag/
│   ├── data_pipeline/
│   ├── agents/
│   ├── ui/
│   └── utils/
│
├── tests/
├── configs/
├── deployment/
├── notebooks/
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI / Machine Learning
- Google Gemini 2.5 Flash
- Sentence Transformers
- FAISS
- NumPy
- Scikit-learn

### Data Processing
- Pandas
- Feedparser
- Requests

### Version Control
- Git
- GitHub

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Ramandeepcod/AI_Financial_Assistant.git
cd AI_Financial_Assistant
```

Create a virtual environment:

```bash
python -m venv venv_api
```

Activate it:

### Linux

```bash
source venv_api/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the API:

```bash
python -m uvicorn src.api.main:app --reload
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome endpoint |
| GET | `/health` | Health check |
| POST | `/ask` | Ask a financial question |

---

## 📌 Example Request

```json
{
    "question": "Should I invest in Alphabet?"
}
```

---

## 📌 Future Improvements

- Streamlit chat interface
- Docker support
- Authentication
- Conversation history
- Source citation display
- Deployment on Render/Railway
- Unit testing
- CI/CD pipeline

---

## 👨‍💻 Author

**Ramandeep**

GitHub: https://github.com/Ramandeepcod