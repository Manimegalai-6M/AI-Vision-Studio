import streamlit as st

SUPPORTED_FORMATS = ["jpg", "jpeg", "png"]

MAX_SIZE_MB = 10


def image_uploader():

    st.subheader("📤 Upload Image")

    st.caption(
        f"Supported: {', '.join(SUPPORTED_FORMATS).upper()} | Maximum Size: {MAX_SIZE_MB} MB"
    )

    uploaded_file = st.file_uploader(
        "Drag and drop an image or browse your files",
        type=SUPPORTED_FORMATS,
        help="Upload an image for AI analysis."
    )

    if uploaded_file:

        file_size = uploaded_file.size / (1024 * 1024)

        if file_size > MAX_SIZE_MB:

            st.error(
                f"File size exceeds {MAX_SIZE_MB} MB."
            )

            return None

        return uploaded_file

    return None