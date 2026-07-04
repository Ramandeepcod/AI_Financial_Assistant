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
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

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
# Display Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and "sources" in message
            and message["sources"]
        ):

            st.divider()

            st.markdown("### 📚 Retrieved Sources")

            for i, source in enumerate(
                message["sources"],
                start=1
            ):

                st.markdown(
                    f"**{i}.** {source}"
                )

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask a financial question..."
)

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = ask_ai(question)

            answer = result["answer"]
            sources = result["sources"]

            st.markdown(answer)
            if sources:

                st.divider()

                st.markdown("### 📚 Retrieved Sources")

                for i, source in enumerate(sources, start=1):

                    st.markdown(
                        f"**{i}.** {source}"
                    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources
        }
    )
