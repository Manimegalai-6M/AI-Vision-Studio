import streamlit as st

from PIL import Image

from services.face_detection_service import detect_faces

st.set_page_config(
    page_title="Face Detection",
    page_icon="😀",
    layout="wide"
)

st.title("😀 AI Face Detection")

uploaded = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    st.image(
        image,
        caption="Original Image",
        use_container_width=True
    )

    with st.spinner("Detecting faces..."):

        output, count = detect_faces(image)

    st.success(f"Faces Detected : {count}")

    st.image(
        output,
        caption="Detected Faces",
        use_container_width=True
    )