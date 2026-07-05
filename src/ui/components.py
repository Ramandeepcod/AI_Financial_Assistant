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

    st.subheader("📰 Retrieved News")

    for source in sources:

        with st.container(border=True):

            st.markdown("**📰 Financial News**")

            st.caption("Retrieved from the vector database")

            st.write(source)
