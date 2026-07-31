import streamlit as st

from PIL import Image
from io import BytesIO

from gtts import gTTS

from services.caption_service import generate_caption
from services.accessibility_service import (
    generate_accessibility_description
)
from services.translation_service import (
    translate_predictions
)

# -------------------------------------------------------

st.set_page_config(
    page_title="Accessibility Assistant",
    page_icon="♿",
    layout="wide"
)

st.title("♿ AI Accessibility Assistant")

uploaded = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

language = st.selectbox(

    "🌍 Translate To",

    [

        "English",

        "Tamil",

        "Hindi",

        "French",

        "Japanese"

    ]

)

# -------------------------------------------------------

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    with st.spinner("Generating caption..."):

        caption = generate_caption(image)

    st.subheader("📝 Image Caption")

    st.write(caption)

    # ---------------------------------------------------

    #
    # Replace this later with your YOLO Object Counter
    #
    objects = [
        "Person",
        "Tree",
        "Road"
    ]

    st.subheader("🔢 Detected Objects")

    for obj in objects:
        st.write("•", obj)

    # ---------------------------------------------------

    with st.spinner("Creating accessibility description..."):

        description = generate_accessibility_description(
            caption,
            objects
        )

    st.subheader("♿ Accessibility Description")

    st.write(description)

    # ---------------------------------------------------

    translated = translate_predictions(
        description,
        language
    )

    st.subheader("🌍 Translated")

    st.write(translated)

    # ---------------------------------------------------

    st.subheader("🔊 Audio")

    lang_map = {

        "English": "en",

        "Tamil": "ta",

        "Hindi": "hi",

        "French": "fr",

        "Japanese": "ja"

    }

    tts = gTTS(

        text=translated,

        lang=lang_map[language]

    )

    audio = BytesIO()

    tts.write_to_fp(audio)

    st.audio(audio.getvalue())

    # ---------------------------------------------------

    st.download_button(

        "📥 Download Description",

        data=translated,

        file_name="accessibility_description.txt",

        mime="text/plain"

    )

else:

    st.info("Upload an image to begin.")