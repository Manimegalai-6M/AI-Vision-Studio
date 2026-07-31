import streamlit as st
from PIL import Image

from utils.classifier import classify_image
from components.uploader import image_uploader
from components.image_card import show_image_card

from services.recycle_service import get_recycling_info


st.set_page_config(
    page_title="AI Recycling Assistant",
    page_icon="♻️",
    layout="wide"
)

st.title("♻️ AI Recycling Assistant")

st.write(
    "Upload an image of a waste item to get recycling guidance."
)

uploaded_file = image_uploader()

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )

    with st.spinner("Analyzing object..."):

        predictions = classify_image(
            image,
            top_k=5
        )

    best_prediction = predictions[0]

    label = best_prediction["label"]

    confidence = best_prediction["score"] * 100

    st.divider()

    st.subheader("🔍 Prediction")

    st.success(f"**{label.title()}**")

    st.write(f"Confidence : **{confidence:.2f}%**")

    recycle_info = get_recycling_info(label)

    st.divider()

    if recycle_info:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "♻️ Category",
                recycle_info["Category"]
            )

            st.metric(
                "🗑 Disposal Bin",
                recycle_info["Bin"]
            )

            st.metric(
                "📦 Material",
                recycle_info["Material"]
            )

        with col2:

            st.metric(
                "✅ Recyclable",
                recycle_info["Recyclable"]
            )

            st.subheader("💡 Recycling Tips")

            for tip in recycle_info["Tips"]:
                st.write(f"• {tip}")

    else:

        st.warning(
            "⚠️ Recycling information is not available for this object."
        )

        st.info(
            f"Detected Object: {label}"
        )

else:

    st.info("📷 Upload a JPG or PNG image.")