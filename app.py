import streamlit as st
from pathlib import Path
from components.sidebar import show_sidebar
from components.footer import show_footer
from dotenv import load_dotenv

load_dotenv()
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
css_root = Path("styles")
css_file = css_root / "style.css"

if css_file.exists():
    css_text = css_file.read_text()

    # Inline any local @import rules from the styles directory.
    inlined_css = []
    for line in css_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("@import url(") and stripped.endswith(");"):
            import_path = stripped[len("@import url("):-2].strip().strip('"\'')
            local_file = css_root / import_path
            if local_file.exists():
                inlined_css.append(local_file.read_text())
                continue
        inlined_css.append(line)

    st.markdown(f"<style>{'\n'.join(inlined_css)}</style>", unsafe_allow_html=True)

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