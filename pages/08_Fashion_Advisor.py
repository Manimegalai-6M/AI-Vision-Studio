import streamlit as st
from PIL import Image

from utils.classifier import classify_image
from components.uploader import image_uploader
from components.image_card import show_image_card

from utils.color_detector import detect_dominant_color
from utils.color_match import get_matching_colors
from services.fashion_service import get_fashion_advice

st.set_page_config(
    page_title="AI Fashion Advisor",
    page_icon="👕",
    layout="wide"
)

st.title("👕 AI Fashion Advisor")

st.write(
    "Upload a clothing image and receive AI-powered fashion advice."
)

uploaded_file = image_uploader()

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )

    with st.spinner("Analyzing fashion..."):

        predictions = classify_image(
            image,
            top_k=5
        )

    best_prediction = predictions[0]

    label = best_prediction["label"]

    confidence = best_prediction["score"] * 100

    dominant_color = detect_dominant_color(image)

    matching_colors = get_matching_colors(dominant_color)

    fashion = get_fashion_advice(label)

    st.divider()

    st.subheader("👔 Prediction")

    st.success(f"**{label.title()}**")

    st.write(f"Confidence : **{confidence:.2f}%**")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🎨 Dominant Color",
            dominant_color
        )

        st.subheader("🌈 Matching Colors")

        if matching_colors:

            for color in matching_colors:
                st.write(f"• {color}")

        else:

            st.info("No matching colors available.")

    with col2:

        if fashion:

            st.metric(
                "👔 Occasion",
                fashion["Occasion"]
            )

            st.metric(
                "⭐ Fashion Score",
                f"{fashion['Score']} / 10"
            )

        else:

            st.warning("Fashion advice not available.")

    st.divider()

    if fashion:

        st.subheader("💡 Style Tips")

        for tip in fashion["Tips"]:

            st.success(f"✔ {tip}")

    else:

        st.warning(
            "⚠ Clothing type not found in the fashion database."
        )

else:

    st.info("📷 Upload a JPG or PNG clothing image.")