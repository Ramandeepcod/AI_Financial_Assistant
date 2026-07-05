"""
Reusable UI Components
"""

import streamlit as st


def render_sources(sources):
    """
    Display retrieved source documents.
    """

    if not sources:
        return

    st.divider()

    st.markdown("## 📚 Retrieved Sources")

    for i, source in enumerate(
        sources,
        start=1
    ):

        with st.container(border=True):

            st.markdown(
                f"**📄 Source {i}**"
            )

            st.write(source)
