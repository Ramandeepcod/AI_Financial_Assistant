"""
Custom CSS Styles
"""

import streamlit as st


def load_css():
    """
    Load custom CSS.
    """

    st.markdown(
        """
<style>

/* Main page */
.main {
    padding-top: 1rem;
}

/* Chat input */
.stChatInput {
    margin-top: 20px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    border-right: 1px solid #d9d9d9;
}

/* Source Cards */
div[data-testid="stVerticalBlock"] {
    border-radius: 12px;
}

</style>
""",
        unsafe_allow_html=True
    )
