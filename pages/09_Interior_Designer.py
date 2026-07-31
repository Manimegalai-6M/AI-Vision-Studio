import streamlit as st
from PIL import Image

from utils.classifier import classify_image
from components.uploader import image_uploader
from components.image_card import show_image_card

from services.interior_service import get_room_information
from utils.room_color import detect_room_color

st.set_page_config(
    page_title="AI Interior Designer",
    page_icon="🛋️",
    layout="wide"
)

st.title("🛋️ AI Interior Designer")

st.write(
    "Upload a room image and receive AI-powered interior design suggestions."
)

uploaded_file = image_uploader()

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )

    with st.spinner("Analyzing room..."):

        predictions = classify_image(
            image,
            top_k=5
        )

    room_info = None
    label = ""
    confidence = 0

    for prediction in predictions:

        room_info = get_room_information(
            prediction["label"]
        )

        if room_info:

            label = prediction["label"]

            confidence = prediction["score"] * 100

            break

    # If nothing matched, use the first prediction
    if not room_info:

        label = predictions[0]["label"]

        confidence = predictions[0]["score"] * 100

    room_color = detect_room_color(image)

    st.divider()

    st.subheader("🏠 Room Prediction")

    st.success(f"**{label.title()}**")

    st.write(f"Confidence : **{confidence:.2f}%**")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🎨 Dominant Color",
            room_color
        )

    with col2:

        if room_info:

            st.metric(
                "🛋️ Interior Style",
                room_info["Style"]
            )

            st.metric(
                "⭐ Interior Score",
                f"{room_info['Score']} / 10"
            )

        else:

            st.warning("Room information not available.")

    st.divider()

    if room_info:

        st.subheader("🪑 Recommended Furniture")

        for furniture in room_info["Furniture"]:

            st.success(f"✔ {furniture}")

        st.divider()

        st.subheader("🌿 Decoration Ideas")

        for decor in room_info["Decor"]:

            st.info(f"✔ {decor}")

    else:

        st.warning(
            "⚠️ Room type not found in the local database."
        )

else:

    st.info("📷 Upload a room image (JPG or PNG).")