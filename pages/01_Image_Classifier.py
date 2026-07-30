import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

from utils.classifier import classify_image
from utils.image_info import get_image_info
from utils.translator import translate_label
from components.uploader import image_uploader

st.set_page_config(
    page_title="Image Classifier",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ AI Image Classifier")
st.write("Upload an image and let AI identify what it contains.")

uploaded_file = image_uploader()

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    st.divider()

    st.subheader("📏 Image Information")

    info = get_image_info(image, uploaded_file)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Width", f"{info['Width']} px")
        st.metric("Format", info["Format"])

    with col2:
        st.metric("Height", f"{info['Height']} px")
        st.metric("Mode", info["Mode"])

    with col3:
        st.metric("File Size", f"{info['File Size (KB)']} KB")

    st.divider()

    with st.spinner("Analyzing image..."):

        predictions = classify_image(image)

    st.subheader("🤖 Top Predictions")

    table = []

    for prediction in predictions:

        label = prediction["label"]

        score = round(prediction["score"] * 100, 2)

        st.write(f"### {label}")

        st.progress(float(prediction["score"]))

        st.caption(f"{score}% Confidence")

        table.append({
            "Label": label,
            "Confidence": score
        })

    st.divider()

    st.subheader("🌍 Translation")

    best_label = predictions[0]["label"]

    translated = translate_label(best_label)

    df_translation = pd.DataFrame(
        {
            "Language": translated.keys(),
            "Translation": translated.values()
        }
    )

    st.dataframe(
        df_translation,
        use_container_width=True
    )

    st.divider()

    st.subheader("📊 Confidence Chart")

    df = pd.DataFrame(table)

    fig = px.bar(
        df,
        x="Label",
        y="Confidence",
        text="Confidence",
        title="Prediction Confidence"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.download_button(
        "📥 Download Results",
        data=df.to_csv(index=False),
        file_name="prediction_results.csv",
        mime="text/csv"
    )

else:

    st.info("Upload a JPG or PNG image.")