"""
Suggested Questions Component
"""

import streamlit as st


SUGGESTED_QUESTIONS = [
    "Should I invest in Alphabet?",
    "Latest Tesla news",
    "Compare Apple and Microsoft",
    "What are the best banking stocks?",
    "Is Nvidia a good long-term investment?"
]


def render_suggestions():
    """
    Display suggested questions.
    """

    st.markdown("## 💡 Suggested Questions")

    for question in SUGGESTED_QUESTIONS:

        st.markdown(f"• {question}")

    st.divider()
