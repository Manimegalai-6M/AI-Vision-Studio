import streamlit as st
from PIL import Image

from services.caption_service import generate_caption

st.set_page_config(
    page_title="AI Caption Generator",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ AI Caption Generator")

uploaded = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    st.image(
        image,
        use_container_width=True
    )

    with st.spinner("Generating caption..."):

        caption = generate_caption(image)

    st.success("Caption Generated")

    st.markdown("### 📝 Caption")

    st.write(caption)

    st.download_button(
        "📥 Download Caption",
        caption,
        file_name="caption.txt"
    )

else:

    st.info("Upload an image to generate a caption.")