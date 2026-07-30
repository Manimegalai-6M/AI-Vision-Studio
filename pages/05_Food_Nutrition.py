import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

from components.uploader import image_uploader
from components.image_card import show_image_card
from utils.classifier import classify_image
from services.nutrition_service import get_nutrition

st.set_page_config(
    page_title="Food Nutrition",
    page_icon="🍕",
    layout="wide"
)

st.title("🍕 AI Food Nutrition Analyzer")

uploaded_file = image_uploader()

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(image, uploaded_file)

    if st.button("Analyze Food"):

        with st.spinner("Detecting food..."):

            prediction = classify_image(image, top_k=1)[0]

            food = prediction["label"]

            nutrition = get_nutrition(food)

        st.success(f"Detected Food: {food}")

        col1, col2 = st.columns(2)

        with col1:

            st.metric("Calories", nutrition["Calories"])

            st.metric("Protein (g)", nutrition["Protein"])

            st.metric("Fat (g)", nutrition["Fat"])

        with col2:

            st.metric("Carbohydrates (g)", nutrition["Carbohydrates"])

            st.metric("Health Score", f'{nutrition["Health Score"]}/10')

            st.info(
                f'🥗 Alternative: {nutrition["Alternative"]}'
            )

        if nutrition["Calories"] != "Unknown":

            df = pd.DataFrame({
                "Nutrient": [
                    "Protein",
                    "Fat",
                    "Carbohydrates"
                ],
                "Value": [
                    nutrition["Protein"],
                    nutrition["Fat"],
                    nutrition["Carbohydrates"]
                ]
            })

            fig = px.bar(
                df,
                x="Nutrient",
                y="Value",
                text="Value",
                title="Nutrition Breakdown"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

else:

    st.info("Upload a food image.")