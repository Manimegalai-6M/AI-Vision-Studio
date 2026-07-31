import streamlit as st
from PIL import Image

from utils.classifier import classify_image
from services.timeline_service import get_timeline

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Image Timeline",
    page_icon="🕒",
    layout="wide"
)

st.title("🕒 AI Image Timeline")
st.markdown(
    "Upload an image to estimate its historical era and timeline."
)

# --------------------------------------------------
# IMAGE UPLOADER
# --------------------------------------------------

uploaded = st.file_uploader(
    "📷 Upload Image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------------------------
# MAIN
# --------------------------------------------------

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    with st.spinner("Analyzing image..."):

        predictions = classify_image(
            image,
            top_k=1
        )

    prediction = predictions[0]["label"]
    confidence = predictions[0]["score"] * 100

    st.divider()

    st.subheader("🔍 Prediction")

    st.write(f"**Object:** {prediction}")

    st.progress(confidence / 100)

    st.write(f"**Confidence:** {confidence:.2f}%")

    # ----------------------------------------------

    timeline = get_timeline(prediction)

    if timeline:

        st.divider()

        st.subheader("🏛 Estimated Era")

        st.success(timeline["era"])

        st.subheader("🗓 Timeline")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Start Year",
                timeline["start_year"]
            )

        with col2:
            st.metric(
                "End Year",
                timeline["end_year"]
            )

        st.progress(1.0)

        st.write(
            f"**{timeline['start_year']} ───────── {timeline['end_year']}**"
        )

        st.divider()

        st.subheader("📖 Historical Context")

        st.info(
            timeline["description"]
        )

        st.divider()

        st.subheader("📌 Important Events")

        for event in timeline["events"]:
            st.write(f"✔ {event}")

        st.divider()

        st.subheader("📚 Learn More")

        search_query = prediction.replace(" ", "+")

        st.markdown(
            f"[🔎 Search on Wikipedia](https://en.wikipedia.org/wiki/Special:Search?search={search_query})"
        )

    else:

        st.warning(
            "⚠ Timeline information is unavailable for this image."
        )

else:

    st.info(
        "Upload a JPG or PNG image to begin."
    )