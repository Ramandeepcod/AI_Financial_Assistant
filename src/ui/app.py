"""
Streamlit Frontend

User interface for the AI Financial Assistant.
"""

import streamlit as st

from api_client import ask_ai

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Financial Assistant",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 AI Financial Assistant")

st.markdown(
    """
Ask questions about financial markets using our
Retrieval-Augmented Generation (RAG) system powered by
Google Gemini.
"""
)

st.divider()

# --------------------------------------------------
# User Input
# --------------------------------------------------

question = st.text_input(
    "Enter your financial question:",
    placeholder="Example: Should I invest in Alphabet?"
)

# --------------------------------------------------
# Ask Button
# --------------------------------------------------

if st.button("Ask AI", use_container_width=True):

    if question.strip():

        with st.spinner("Generating response..."):

            answer = ask_ai(question)

        st.subheader("🤖 AI Response")

        st.success(answer)

    else:

        st.warning("Please enter a question.")