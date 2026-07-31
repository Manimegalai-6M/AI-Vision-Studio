import streamlit as st
from PIL import Image

from utils.classifier import classify_image
from components.uploader import image_uploader
from components.image_card import show_image_card

from services.nutrition_service import get_food_information

st.set_page_config(
    page_title="AI Food Nutrition",
    page_icon="🍕",
    layout="wide"
)

st.title("🍕 AI Food Nutrition Analyzer")

st.write(
    "Upload a food image to estimate its nutrition information."
)

uploaded_file = image_uploader()

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )

    with st.spinner("Analyzing food..."):

        predictions = classify_image(
            image,
            top_k=5
        )

    best_prediction = predictions[0]

    label = best_prediction["label"]

    confidence = best_prediction["score"] * 100

    st.divider()

    st.subheader("🍽 Prediction")

    st.success(
        f"**{label.title()}**"
    )

    st.write(
        f"Confidence: **{confidence:.2f}%**"
    )

    nutrition = get_food_information(label)

    st.divider()

    if nutrition:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🔥 Calories",
                f"{nutrition['Calories']} kcal"
            )

            st.metric(
                "🥩 Protein",
                f"{nutrition['Protein']} g"
            )

            st.metric(
                "🥑 Fat",
                f"{nutrition['Fat']} g"
            )

            st.metric(
                "🍞 Carbohydrates",
                f"{nutrition['Carbohydrates']} g"
            )

        with col2:

            st.metric(
                "💚 Health Score",
                f"{nutrition['Health Score']} / 10"
            )

            st.info(
                f"🥗 Healthier Alternative\n\n{nutrition['Alternative']}"
            )

            st.success(
                f"💡 Recommendation\n\n{nutrition['Recommendation']}"
            )

    else:

        st.warning(
            "⚠ Food not available in the local nutrition database."
        )

        st.write(
            "Detected label:",
            label
        )