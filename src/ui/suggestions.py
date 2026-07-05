"""
Suggested Questions Component
"""

import streamlit as st

SUGGESTED_QUESTIONS = [
    "📈 Should I invest in Alphabet?",
    "🚗 Latest Tesla news",
    "🍎 Compare Apple and Microsoft",
    "🏦 What are the best banking stocks?",
    "💻 Is Nvidia a good long-term investment?"
]


def render_suggestions():
    """
    Display suggested questions.
    """

    st.subheader("💡 Try Asking")

    col1, col2 = st.columns(2)

    for index, question in enumerate(SUGGESTED_QUESTIONS):

        if index % 2 == 0:
            col1.info(question)

        else:
            col2.info(question)

    st.divider()
