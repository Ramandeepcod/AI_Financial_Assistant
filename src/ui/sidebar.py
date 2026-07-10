"""
Sidebar Components
"""

import streamlit as st

from src.ui.api_client import get_statistics


def render_sidebar():
    """
    Render the application sidebar.
    """

    stats = get_statistics()

    with st.sidebar:

        # -----------------------------
        # Title
        # -----------------------------
        st.title("🤖 AI Financial Assistant")

        st.caption("Financial News powered by RAG")

        st.divider()

        # -----------------------------
        # Backend Status
        # -----------------------------
        if stats:
            st.success("🟢 Backend Online")
        else:
            st.error("🔴 Backend Offline")
            return

        # -----------------------------
        # Dataset Statistics
        # -----------------------------
        st.subheader("📊 Statistics")

        st.write(f"**📄 Articles:** {stats['total_articles']}")
        st.write(f"**🏢 Companies:** {stats['total_companies']}")
        st.write(f"**📰 Sources:** {stats['total_sources']}")

        st.divider()

        # -----------------------------
        # Technology
        # -----------------------------
        st.subheader("⚙️ Technology")

        st.write(f"**🤖 LLM:** {stats['llm_model']}")
        st.write(f"**🧠 Embedding:** {stats['embedding_model']}")
        st.write(f"**📚 Vector DB:** {stats['vector_store']}")

        st.divider()

        # -----------------------------
        # Chat Statistics
        # -----------------------------
        st.subheader("💬 Chat")

        message_count = len(
            st.session_state.get("messages", [])
        )

        st.write(f"**Messages:** {message_count}")

        st.divider()

        # -----------------------------
        # Clear Chat
        # -----------------------------
        if st.button(
            "🗑️ Clear Conversation",
            use_container_width=True
        ):
            st.session_state.messages = []
            st.rerun()
