import streamlit as st
from PIL import Image


def show_image_card(image: Image.Image, uploaded_file):
    """
    Display uploaded image and metadata.
    """

    width, height = image.size

    file_size = round(uploaded_file.size / 1024, 2)

    st.subheader("🖼 Image Preview")

    st.image(
        image,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Width",
            f"{width}px"
        )

        st.metric(
            "Format",
            image.format or "Unknown"
        )

        st.metric(
            "Color Mode",
            image.mode
        )

    with col2:

        st.metric(
            "Height",
            f"{height}px"
        )

        st.metric(
            "File Size",
            f"{file_size} KB"
        )

        st.metric(
            "Aspect Ratio",
            f"{width}:{height}"
        )