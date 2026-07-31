import streamlit as st

from PIL import Image

from services.quality_service import analyze_quality

st.set_page_config(
    page_title="Image Quality",
    page_icon="📷",
    layout="wide"
)

st.title("📷 AI Image Quality Analyzer")

uploaded = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    st.image(image, use_container_width=True)

    with st.spinner("Analyzing image..."):

        result = analyze_quality(image)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Blur", result["Blur"])

        st.metric("Brightness", result["Brightness"])

        st.metric("Contrast", result["Contrast"])

    with col2:

        st.metric("Sharpness", result["Sharpness"])

        st.metric("Overall Score", f"{result['Overall']}/100")

    st.divider()

    st.subheader("💡 Suggestions")

    if result["Blur"] < 100:
        st.warning("Image appears blurry.")
    else:
        st.success("Image is sharp.")

    if result["Brightness"] < 70:
        st.warning("Increase brightness.")
    elif result["Brightness"] > 190:
        st.warning("Image is too bright.")
    else:
        st.success("Brightness is good.")

    if result["Contrast"] < 40:
        st.warning("Low contrast.")
    else:
        st.success("Contrast is good.")