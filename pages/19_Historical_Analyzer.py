import streamlit as st
from PIL import Image

from services.classifier_service import classify_image
from services.caption_service import generate_caption
from services.historical_service import get_historical_info
from services.story_service import generate_story


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Historical Analyzer",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ AI Historical Analyzer")
st.write(
    "Upload a historical image to analyze its background, importance, and timeline."
)

st.divider()

# ---------------------------------------------------
# IMAGE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "📷 Upload Historical Image",
    type=["jpg", "jpeg", "png"]
)

# ---------------------------------------------------
# PROCESS IMAGE
# ---------------------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("🔍 Analyze History", use_container_width=True):

        with st.spinner("Analyzing image..."):

            try:

                # -------------------------------
                # IMAGE CLASSIFICATION
                # -------------------------------

                predictions = classify_image(image)

                if not predictions:
                    st.error("Unable to classify image.")
                    st.stop()

                prediction = predictions[0]["label"]
                confidence = predictions[0]["score"] * 100

                # -------------------------------
                # IMAGE CAPTION
                # -------------------------------

                caption = generate_caption(image)

                # -------------------------------
                # HISTORICAL DATABASE
                # -------------------------------

                history = get_historical_info(prediction)

                st.success("Analysis Completed")

                st.divider()

                st.subheader("🏛 Historical Name")
                st.write(prediction)

                st.metric(
                    "Confidence",
                    f"{confidence:.2f}%"
                )

                st.divider()

                st.subheader("📝 Image Caption")
                st.info(caption)

                st.divider()

                if history:

                    st.subheader("📅 Historical Period")
                    st.write(history["period"])

                    st.subheader("📍 Location")
                    st.write(history["location"])

                    st.subheader("🕒 Construction / Era")
                    st.write(history["years"])

                    st.subheader("👤 Built By")
                    st.write(history["built_by"])

                    st.subheader("⭐ Historical Importance")
                    st.write(history["importance"])

                    st.subheader("🎓 Interesting Facts")

                    for fact in history["facts"]:
                        st.write(f"✔ {fact}")

                    st.divider()

                    # -------------------------------
                    # AI SUMMARY
                    # -------------------------------

                    prompt = f"""
Historical Object:
{prediction}

Image Caption:
{caption}

Historical Information:

Period:
{history['period']}

Location:
{history['location']}

Years:
{history['years']}

Built By:
{history['built_by']}

Importance:
{history['importance']}

Facts:
{', '.join(history['facts'])}

Write a student-friendly historical explanation in about 150 words.
"""

                    summary = generate_story(
                        caption=prompt,
                        story_type="Educational",
                        story_length="Short"
                    )

                    st.subheader("🤖 AI Historical Summary")

                    st.write(summary)

                    st.divider()

                    report = f"""
AI HISTORICAL ANALYZER REPORT

------------------------------------

Historical Name:
{prediction}

Confidence:
{confidence:.2f}%

Image Caption:
{caption}

Historical Period:
{history['period']}

Location:
{history['location']}

Years:
{history['years']}

Built By:
{history['built_by']}

Historical Importance:
{history['importance']}

Interesting Facts:

{chr(10).join(['- '+fact for fact in history['facts']])}

------------------------------------

AI Historical Summary

{summary}
"""

                    st.download_button(
                        "📥 Download Historical Report",
                        report,
                        file_name="historical_report.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

                else:

                    st.warning(
                        "⚠ Historical information is unavailable for this image."
                    )

            except Exception as e:

                st.error(f"Error : {e}")