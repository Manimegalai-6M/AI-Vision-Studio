import streamlit as st
from PIL import Image

from services.background_service import remove_background

st.set_page_config(
    page_title="Background Removal",
    page_icon="🪄",
    layout="wide"
)

st.title("🪄 AI Background Removal")

uploaded = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    with st.spinner("Removing background..."):

        output = remove_background(image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Background Removed")
        st.image(output, use_container_width=True)

    from io import BytesIO

    img_bytes = BytesIO()

    output.save(img_bytes, format="PNG")

    st.download_button(
        "📥 Download Transparent PNG",
        data=img_bytes.getvalue(),
        file_name="background_removed.png",
        mime="image/png"
    )

else:
    st.info("Upload a JPG or PNG image.")