import streamlit as st
from PIL import Image

from services.classifier_service import classify_image
from services.caption_service import generate_caption
from services.cultural_service import get_cultural_info
from services.story_service import generate_story


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="🌍 AI Cultural Explorer",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Cultural Explorer")
st.write(
    "Upload an image of a cultural object, monument, food, clothing, or festival "
    "to learn about its cultural significance."
)

st.divider()

# -------------------------------------------------
# IMAGE UPLOAD
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["jpg", "jpeg", "png"]
)

# -------------------------------------------------
# PROCESS IMAGE
# -------------------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    with st.spinner("🔍 Analyzing Image..."):

        # -----------------------------------------
        # IMAGE CLASSIFICATION
        # -----------------------------------------

        predictions = classify_image(image)

        prediction = predictions[0]["label"]
        confidence = predictions[0]["score"] * 100

        # -----------------------------------------
        # IMAGE CAPTION
        # -----------------------------------------

        caption = generate_caption(image)

        # -----------------------------------------
        # CULTURE DATABASE
        # -----------------------------------------

        culture = get_cultural_info(prediction)

    st.divider()

    st.subheader("🧠 AI Prediction")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Prediction",
            prediction.title()
        )

    with col2:
        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    st.markdown("### 📝 Caption")

    st.success(caption)

    # -----------------------------------------
    # CULTURAL INFORMATION
    # -----------------------------------------

    if culture:

        st.divider()

        st.header("🌍 Cultural Information")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f"### 🌎 Country\n{culture['country']}"
            )

            st.markdown(
                f"### 🏷 Category\n{culture['category']}"
            )

            st.markdown(
                f"### 🏛 Culture\n{culture['culture']}"
            )

        with col2:

            st.markdown(
                "### 📖 Description"
            )

            st.write(
                culture["description"]
            )

        st.divider()

        st.subheader("🎉 Traditions")

        for item in culture["traditions"]:
            st.write(f"✅ {item}")

        st.divider()

        st.subheader("🎊 Festivals")

        for item in culture["festivals"]:
            st.write(f"🎇 {item}")

        st.divider()

        st.subheader("⭐ Interesting Facts")

        for fact in culture["facts"]:
            st.write(f"✔ {fact}")

        st.divider()

        # -----------------------------------------
        # AI CULTURAL SUMMARY
        # -----------------------------------------

        with st.spinner("🤖 Generating AI Cultural Summary..."):

            prompt = f"""
You are an expert in world cultures.

Explain the cultural importance of the following item.

Item:
{prediction}

Caption:
{caption}

Country:
{culture['country']}

Culture:
{culture['culture']}

Description:
{culture['description']}

Traditions:
{', '.join(culture['traditions'])}

Festivals:
{', '.join(culture['festivals'])}

Interesting Facts:
{', '.join(culture['facts'])}

Write a simple explanation suitable for students.
"""

            summary = generate_story(prompt)

        st.subheader("🤖 AI Cultural Summary")

        st.info(summary)

        st.download_button(
            "📥 Download Report",
            summary,
            file_name="cultural_report.txt"
        )

    else:

        st.warning(
            "⚠️ No cultural information found for this object."
        )

else:

    st.info("📷 Upload an image to begin.")