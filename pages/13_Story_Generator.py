import streamlit as st
from PIL import Image

from components.uploader import image_uploader
from components.image_card import show_image_card

from services.caption_service import generate_caption
from services.story_service import generate_story

st.set_page_config(
    page_title="AI Story Generator",
    page_icon="📖",
    layout="wide"
)

st.title("📖 AI Story Generator")

st.write(
    "Upload an image and let AI create a story based on it."
)

uploaded_file = image_uploader()

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )

    with st.spinner("Generating image caption..."):

        caption = generate_caption(image)

    st.divider()

    st.subheader("📝 Image Caption")

    st.info(caption)

    story_type = st.selectbox(
        "📚 Story Type",
        [
            "Kids Story",
            "Adventure",
            "Fantasy",
            "Mystery",
            "Motivational",
            "Sci-Fi"
        ]
    )

    story_length = st.selectbox(
        "📏 Story Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )

    if st.button("📖 Generate Story", use_container_width=True):

        with st.spinner("Writing story..."):

            story = generate_story(
                caption=caption,
                story_type=story_type,
                story_length=story_length
            )

        st.divider()

        st.subheader("📖 AI Story")

        st.write(story)

        st.divider()

        st.download_button(
            "📥 Download Story",
            data=story,
            file_name="ai_story.txt",
            mime="text/plain",
            use_container_width=True
        )

else:

    st.info("📷 Upload a JPG or PNG image.")