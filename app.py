import streamlit as st
from pathlib import Path
from components.sidebar import show_sidebar
from components.footer import show_footer

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Vision Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# -----------------------------
# LOAD CSS
# -----------------------------
css_file = Path("styles/style.css")

if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
show_sidebar()
# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown(
    """
    <div class='hero'>
        <h1>🤖 AI Vision Studio</h1>
        <h3>One Platform • Multiple AI Vision Tools</h3>
        <p>Analyze images with state-of-the-art Artificial Intelligence.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# FEATURE CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 🖼 Image Analysis

• Image Classification

• Image Information

• Image Comparison

• Image Quality
""")

with col2:
    st.success("""
### 🤖 AI Vision

• Face Detection

• Background Removal

• Object Counter

• Caption Generator
""")

with col3:
    st.warning("""
### 🌍 Smart Assistant

• Plant Doctor

• Food Nutrition

• Accessibility

• Story Generator
""")

st.divider()

# -----------------------------
# PROJECT OVERVIEW
# -----------------------------
st.header("📌 Project Overview")

st.write("""
AI Vision Studio is a professional computer vision application built using:

- Streamlit
- Hugging Face Transformers
- OpenCV
- Deep Learning Models
- Python
- Pillow
- Plotly

This application combines multiple AI-powered tools into a single platform.
""")

st.divider()

# -----------------------------
# FUTURE MODULES
# -----------------------------
st.header("🚀 Upcoming Modules")

modules = [
    "Image Classifier",
    "Face Detection",
    "Background Removal",
    "Image Quality Analyzer",
    "Food Nutrition",
    "Plant Doctor",
    "Recycling Assistant",
    "Fashion Advisor",
    "Interior Designer",
    "Travel Guide",
    "Caption Generator",
    "Story Generator",
    "Accessibility Assistant",
    "Image Comparison",
    "Object Counter",
    "Daily Challenge",
]

for module in modules:
    st.checkbox(module, value=False, disabled=True)

st.divider()

show_footer()