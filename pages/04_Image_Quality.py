import streamlit as st
from PIL import Image

from components.uploader import image_uploader
from components.image_card import show_image_card
from utils.image_quality import analyze_image_quality

st.set_page_config(
    page_title="Image Quality",
    page_icon="📷",
    layout="wide"
)

st.title("📷 AI Image Quality Analyzer")

st.write(
    "Upload an image to evaluate its quality."
)

uploaded_file = image_uploader()

if uploaded_file:

    image = Image.open(uploaded_file)

    show_image_card(
        image,
        uploaded_file
    )

    if st.button("Analyze Quality"):

        with st.spinner("Analyzing image..."):

            result = analyze_image_quality(image)

        st.success("Analysis Completed!")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Blur",
                result["Blur"]
            )

            st.metric(
                "Brightness",
                result["Brightness"]
            )

        with col2:

            st.metric(
                "Contrast",
                result["Contrast"]
            )

            st.metric(
                "Sharpness",
                result["Sharpness"]
            )

        st.divider()

        st.subheader("Overall Quality")

        st.progress(min(result["Score"] / 100, 1.0))

        st.metric(
            "Quality Score",
            f"{result['Score']}/100"
        )

        st.success(result["Status"])

else:

    st.info("Upload an image to begin.")