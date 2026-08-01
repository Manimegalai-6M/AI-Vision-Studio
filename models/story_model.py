import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

# Load .env file
load_dotenv()


@st.cache_resource
def load_story_model():
    api_key = None

    # Prefer environment variable (works locally and in many CI setups)
    api_key = os.getenv("GROQ_API_KEY")

    # Only attempt to read Streamlit secrets if a secrets.toml exists
    try:
        home_secret = Path.home() / ".streamlit" / "secrets.toml"
        project_secret = Path.cwd() / ".streamlit" / "secrets.toml"

        if home_secret.exists() or project_secret.exists():
            try:
                # Use .get when available to avoid __getitem__ raising
                if hasattr(st.secrets, "get"):
                    api_key = st.secrets.get("GROQ_API_KEY", api_key)
                else:
                    api_key = st.secrets["GROQ_API_KEY"]
            except Exception:
                # If secrets parsing fails, ignore and fallback to env
                pass
    except Exception:
        # If Path or other checks fail, just continue with env var
        pass

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found in .env or Streamlit Secrets."
        )

    return Groq(api_key=api_key)