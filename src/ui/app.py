"""
Streamlit Frontend

User interface for the AI Financial Assistant.
"""

import streamlit as st

from api_client import ask_ai
from components import render_sources
from sidebar import render_sidebar
from styles import load_css
from suggestions import render_suggestions

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Financial Assistant",
    page_icon="🤖",
    layout="wide"
)

load_css()

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

render_sidebar()

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 AI Financial Assistant")

st.caption(
    "Ask intelligent financial questions using "
    "Retrieval-Augmented Generation (RAG), "
    "FAISS Vector Search and Google Gemini."
)

st.divider()

# --------------------------------------------------
# Suggested Questions
# --------------------------------------------------

if len(st.session_state.messages) == 0:
    render_suggestions()

# --------------------------------------------------
# Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and message.get("sources")
        ):
            render_sources(
                message["sources"]
            )

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask anything about financial markets..."
)

if question:

    # -----------------------------
    # User Message
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # -----------------------------
    # AI Response
    # -----------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "🔍 Searching financial news..."
        ):

            result = ask_ai(question)

            answer = result["answer"]
            sources = result["sources"]

        st.markdown(answer)

        render_sources(sources)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources
        }
    )
