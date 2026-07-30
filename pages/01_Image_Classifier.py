import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

from utils.classifier import classify_image
from utils.translator import translate_label
from components.uploader import image_uploader
from components.image_card import show_image_card
from services.translation_service import translate_predictions

st.set_page_config(
    page_title="Image Classifier",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ AI Image Classifier")
st.write("Upload an image and let AI identify what it contains.")

uploaded_file = image_uploader()
confidence_threshold = st.slider(
    "Confidence threshold",
    0,
    100,
    50,
    help="Only show predictions with confidence at or above this percentage."
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )
    language = st.selectbox(
        "🌍 Prediction Language",
        [
            "English",
            "Tamil",
            "Hindi",
            "French",
            "Japanese"
        ]
    )

    with st.spinner("Analyzing image..."):

        predictions = classify_image(image)


    predictions = translate_predictions(
        predictions,
        language
    )


    predictions = [
        p for p in predictions
        if p["score"] * 100 >= confidence_threshold
    ]

    st.subheader("🤖 Top Predictions")
    if predictions:
        best = predictions[0]
        st.success(f"🏆 Best Match: **{best['label']}**")
    else:
        st.warning(
            "No predictions met the confidence threshold. Try lowering the threshold or uploading a different image."
        )

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

    if predictions:
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
    else:
        st.info("No translation available because no predictions met the confidence threshold.")

    st.divider()

    st.subheader("📊 Confidence Chart")

    if table:
        df = pd.DataFrame(table)
        fig = px.bar(
            df,
            x="Confidence",
            y="Label",
            orientation="h",
            title="Prediction Confidence",
            text="Confidence"
        )

        fig.update_traces(
            texttemplate="%{text:.2f}",
            textposition="outside"
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
        st.info("No confidence chart available because there are no predictions above the selected threshold.")

else:

    st.info("Upload a JPG or PNG image."