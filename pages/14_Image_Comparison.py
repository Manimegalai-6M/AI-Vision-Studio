import streamlit as st
from PIL import Image

from services.comparison_service import compare_image_data


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="🆚 AI Image Comparison",
    page_icon="🆚",
    layout="wide"
)

st.title("🆚 AI Image Comparison")

st.write(
    "Upload two images to compare their predictions, "
    "similarity score and image information."
)

st.divider()

# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    uploaded1 = st.file_uploader(
        "📤 Upload Image 1",
        type=["jpg", "jpeg", "png"],
        key="image1"
    )

with col2:
    uploaded2 = st.file_uploader(
        "📤 Upload Image 2",
        type=["jpg", "jpeg", "png"],
        key="image2"
    )

# --------------------------------------------------
# PROCESS
# --------------------------------------------------

if uploaded1 and uploaded2:

    image1 = Image.open(uploaded1).convert("RGB")
    image2 = Image.open(uploaded2).convert("RGB")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.image(image1, caption="Image 1", use_container_width=True)

    with col2:
        st.image(image2, caption="Image 2", use_container_width=True)

    with st.spinner("Comparing Images..."):

        result = compare_image_data(
            image1,
            image2,
            uploaded1,
            uploaded2
        )

    st.divider()

    st.header("🏷 Prediction")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Image 1",
            result["prediction1"]["label"],
            f'{result["prediction1"]["confidence"]:.2f}%'
        )

    with c2:

        st.metric(
            "Image 2",
            result["prediction2"]["label"],
            f'{result["prediction2"]["confidence"]:.2f}%'
        )

    st.divider()

    st.header("📊 Similarity Scores")

    a, b, c = st.columns(3)

    with a:
        st.metric(
            "Histogram",
            f'{result["similarity"]["histogram"]:.2f}%'
        )

    with b:
        st.metric(
            "SSIM",
            f'{result["similarity"]["ssim"]:.2f}%'
        )

    with c:
        st.metric(
            "Average",
            f'{result["similarity"]["average"]:.2f}%'
        )

    st.progress(result["similarity"]["average"] / 100)

    st.divider()

    st.header("🖼 Image Information")

    left, right = st.columns(2)

    with left:

        info = result["info1"]

        st.write(f"**Width:** {info['Width']}")
        st.write(f"**Height:** {info['Height']}")
        st.write(f"**Format:** {info['Format']}")
        st.write(f"**File Size:** {info['File Size']}")

    with right:

        info = result["info2"]

        st.write(f"**Width:** {info['Width']}")
        st.write(f"**Height:** {info['Height']}")
        st.write(f"**Format:** {info['Format']}")
        st.write(f"**File Size:** {info['File Size']}")

    st.divider()

    st.header("🤖 AI Summary")

    st.success(result["summary"])

    st.download_button(
        "📥 Download Report",
        result["summary"],
        file_name="comparison_report.txt"
    )

else:

    st.info("Upload two images to begin comparison.")