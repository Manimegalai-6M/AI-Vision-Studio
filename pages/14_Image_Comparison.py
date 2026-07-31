import streamlit as st
from PIL import Image
from io import BytesIO

from services.object_counter_service import detect_objects

st.set_page_config(
    page_title="AI Object Counter",
    page_icon="🔢",
    layout="wide"
)

st.title("🔢 AI Object Counter")

uploaded = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    with st.spinner("Detecting objects..."):

        output, counts, total = detect_objects(image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Detected Objects")
        st.image(output, use_container_width=True)

    st.divider()

    st.subheader("📊 Object Counts")

    for name, count in counts.items():
        st.metric(name.title(), count)

    st.metric("Total Objects", total)

    buffer = BytesIO()

    output.save(buffer, format="PNG")

    st.download_button(
        "📥 Download Result",
        buffer.getvalue(),
        file_name="object_detection.png",
        mime="image/png"
    )