import streamlit as st
from PIL import Image

from components.uploader import image_uploader
from components.image_card import show_image_card
from utils.face_detection import detect_faces

st.set_page_config(
    page_title="Face Detection",
    page_icon="😀",
    layout="wide"
)

st.title("😀 AI Face Detection")

st.write(
    "Upload an image to detect human faces."
)

uploaded_file = image_uploader()

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )

    if st.button("Detect Faces"):

        with st.spinner("Detecting faces..."):

            output_image, count = detect_faces(image)

        st.success(f"Faces Detected: {count}")

        st.image(
            output_image,
            caption="Detected Faces",
            use_container_width=True
        )

else:

    st.info("Upload a JPG or PNG image.")