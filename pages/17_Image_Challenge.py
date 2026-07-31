import streamlit as st
from PIL import Image

from utils.challenge_data import generate_challenge
from services.challenge_service import update_progress
from services.object_counter_service import detect_objects

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Image Challenge",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 AI Image Challenge Mode")
st.markdown(
    "Find the target objects by uploading images!"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "challenge_objects" not in st.session_state:
    st.session_state.challenge_objects = generate_challenge()

if "score" not in st.session_state:
    st.session_state.score = 0

# --------------------------------------------------
# NEW CHALLENGE BUTTON
# --------------------------------------------------

if st.button("🔄 New Challenge"):
    st.session_state.challenge_objects = generate_challenge()
    st.session_state.score = 0
    st.rerun()

challenge_objects = st.session_state.challenge_objects

# --------------------------------------------------
# SHOW TARGETS
# --------------------------------------------------

st.subheader("🎯 Today's Challenge")

for item in challenge_objects:
    st.write(f"⬜ {item.title()}")

st.divider()

# --------------------------------------------------
# IMAGE UPLOADER
# --------------------------------------------------

uploaded = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------------------------
# PROCESS IMAGE
# --------------------------------------------------

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    with st.spinner("Detecting objects..."):

        output_image, counts, total = detect_objects(image)

    st.image(
        output_image,
        caption="Detected Objects",
        use_container_width=True
    )

    detected = list(counts.keys())

    # --------------------------------------------

    progress = update_progress(
        challenge_objects,
        detected
    )

    completed = progress["completed"]
    remaining = progress["remaining"]
    score = progress["score"]

    st.session_state.score = score

    # --------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Completed")

        if completed:

            for obj in completed:
                st.success(obj.title())

        else:
            st.info("No objects found yet.")

    with col2:

        st.subheader("⬜ Remaining")

        if remaining:

            for obj in remaining:
                st.warning(obj.title())

        else:
            st.success("All objects completed!")

    # --------------------------------------------

    st.divider()

    progress_value = len(completed) / len(challenge_objects)

    st.subheader("📊 Progress")

    st.progress(progress_value)

    st.write(
        f"{len(completed)} / {len(challenge_objects)} Completed"
    )

    # --------------------------------------------

    st.subheader("⭐ Score")

    st.metric(
        label="Points",
        value=score
    )

    # --------------------------------------------

    st.subheader("🔍 Detected Objects")

    if counts:

        for obj, count in counts.items():
            st.write(f"**{obj.title()}** : {count}")

    else:
        st.info("No objects detected.")

    # --------------------------------------------

    if len(completed) == len(challenge_objects):

        st.balloons()

        st.success(
            "🎉 Congratulations! You completed today's challenge!"
        )

        st.metric(
            "Final Score",
            score
        )

else:

    st.info(
        "Upload an image to begin the challenge."
    )