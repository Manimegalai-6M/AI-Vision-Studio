import os
import streamlit as st
from groq import Groq


@st.cache_resource
def load_story_model():

    api_key = (
        st.secrets.get("GROQ_API_KEY")
        or os.getenv("GROQ_API_KEY")
    )

    if not api_key:
        raise ValueError("GROQ_API_KEY not found.")

    return Groq(api_key=api_key)