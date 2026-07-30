import streamlit as st
from config.settings import APP_NAME

def show_sidebar():
    with st.sidebar:
        st.title(f"🤖 {APP_NAME}")

        st.markdown("---")

        st.success("AI Vision Platform")

        st.info(
            "Select a page from the navigation menu."
        )

        st.markdown("---")

        st.caption("Version 1.0")