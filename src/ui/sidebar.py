"""
Sidebar Components
"""

import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.title("🤖 AI Financial Assistant")

        st.divider()

        st.success("🟢 Backend Online")

        st.markdown("### 🧠 Model")
        st.info("Gemini 2.5 Flash")

        st.markdown("### 📚 Vector Store")
        st.info("FAISS")

        st.markdown("### 💬 Messages")

        message_count = len(
            st.session_state.get("messages", [])
        )

        st.info(message_count)

        st.divider()

        if st.button(
            "🗑️ Clear Conversation",
            use_container_width=True
        ):

            st.session_state.messages = []

            st.rerun()
