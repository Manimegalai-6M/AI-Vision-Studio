import streamlit as st
from PIL import Image

from utils.classifier import classify_image
from components.uploader import image_uploader
from components.image_card import show_image_card

from services.travel_service import get_travel_information

st.set_page_config(
    page_title="AI Travel Guide",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Travel Guide")

st.write(
    "Upload a landmark image and receive AI-powered travel information."
)

uploaded_file = image_uploader()

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )

    with st.spinner("Analyzing landmark..."):

        predictions = classify_image(
            image,
            top_k=5
        )

    travel_info = None
    label = ""
    confidence = 0

    for prediction in predictions:

        travel_info = get_travel_information(
            prediction["label"]
        )

        if travel_info:

            label = prediction["label"]

            confidence = prediction["score"] * 100

            break

    # If no matching landmark is found
    if not travel_info:

        label = predictions[0]["label"]

        confidence = predictions[0]["score"] * 100

    st.divider()

    st.subheader("🏛️ Landmark Prediction")

    st.success(f"**{label.title()}**")

    st.write(f"Confidence : **{confidence:.2f}%**")

    st.divider()

    if travel_info:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🌍 Country",
                travel_info["Country"]
            )

            st.metric(
                "📍 City",
                travel_info["City"]
            )

        with col2:

            st.metric(
                "⭐ Tourist Rating",
                travel_info["Rating"]
            )

            st.metric(
                "🕒 Best Time",
                travel_info["Best Time"]
            )

        st.divider()

        st.subheader("📖 Description")

        st.info(travel_info["Description"])

        st.divider()

        st.subheader("💰 Entry Fee")

        st.success(travel_info["Entry Fee"])

        st.divider()

        st.subheader("🚗 Nearby Attractions")

        for place in travel_info["Nearby"]:

            st.write(f"✔ {place}")

        st.divider()

        st.subheader("🍴 Local Food")

        for food in travel_info["Food"]:

            st.write(f"✔ {food}")

        st.divider()

        st.subheader("💡 Travel Tips")

        for tip in travel_info["Tips"]:

            st.success(f"✔ {tip}")

    else:

        st.warning(
            "⚠️ Travel information is not available for this landmark."
        )

else:

    st.info("📷 Upload a landmark image (JPG or PNG).")