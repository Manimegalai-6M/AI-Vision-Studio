import streamlit as st
from PIL import Image

from utils.classifier import classify_image
from components.uploader import image_uploader
from components.image_card import show_image_card

from services.plant_service import diagnose_plant

st.set_page_config(
    page_title="AI Plant Doctor",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 AI Plant Doctor")

st.write(
    "Upload a plant leaf image to identify the plant and check for possible diseases."
)

uploaded_file = image_uploader()

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )

    with st.spinner("Analyzing plant..."):

        predictions = classify_image(
            image,
            top_k=5
        )

    best_prediction = predictions[0]

    label = best_prediction["label"]

    confidence = best_prediction["score"] * 100

    st.divider()

    st.subheader("🌱 Prediction")

    st.success(f"**{label.title()}**")

    st.write(f"Confidence: **{confidence:.2f}%**")

    diagnosis = diagnose_plant(label)

    st.divider()

    if diagnosis:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🦠 Disease",
                diagnosis["Disease"]
            )

            st.metric(
                "⚠️ Severity",
                diagnosis["Severity"]
            )

        with col2:

            st.info(
                f"💊 Treatment\n\n{diagnosis['Treatment']}"
            )

            st.success(
                f"🌱 Prevention\n\n{diagnosis['Prevention']}"
            )

    else:

        st.warning(
            "⚠️ Plant not found in the local database."
        )

        st.write(
            f"Detected Label: **{label}**"
        )

else:

    st.info("📷 Upload a JPG or PNG plant image.")