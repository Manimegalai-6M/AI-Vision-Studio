import streamlit as st
from PIL import Image

from utils.classifier import classify_image
from components.uploader import image_uploader
from components.image_card import show_image_card

from services.emotion_service import get_emotion

st.set_page_config(
    page_title="AI Emotion From Scene",
    page_icon="🎭",
    layout="wide"
)

st.title("🎭 AI Emotion From Scene")

st.write(
    "Upload an image and let AI predict the overall mood of the scene."
)

uploaded_file = image_uploader()

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    show_image_card(
        image,
        uploaded_file
    )

    with st.spinner("Analyzing scene..."):

        predictions = classify_image(
            image,
            top_k=5
        )

    best_prediction = predictions[0]

    label = best_prediction["label"]

    confidence = best_prediction["score"] * 100

    emotion = get_emotion(label)

    # Emotion Details
    if emotion == "Calm":
        emoji = "😌"
        mood = "This image creates a peaceful and relaxing atmosphere."
        music = [
            "🎵 Piano",
            "🎵 Lo-fi",
            "🎵 Nature Sounds"
        ]
        activities = [
            "Meditation",
            "Reading",
            "Evening Walk"
        ]

    elif emotion == "Happy":
        emoji = "😊"
        mood = "This scene feels cheerful and full of positive energy."
        music = [
            "🎵 Pop",
            "🎵 Acoustic",
            "🎵 Happy Playlist"
        ]
        activities = [
            "Photography",
            "Picnic",
            "Travel"
        ]

    elif emotion == "Excited":
        emoji = "🤩"
        mood = "The image gives an energetic and exciting feeling."
        music = [
            "🎵 EDM",
            "🎵 Rock",
            "🎵 Dance"
        ]
        activities = [
            "Sports",
            "Adventure",
            "Celebrate"
        ]

    elif emotion == "Fear":
        emoji = "😨"
        mood = "The scene appears intense or potentially dangerous."
        music = [
            "🎵 Cinematic",
            "🎵 Suspense",
            "🎵 Thriller"
        ]
        activities = [
            "Stay Alert",
            "Observe Carefully",
            "Ensure Safety"
        ]

    elif emotion == "Sad":
        emoji = "😢"
        mood = "This image conveys a quiet and emotional atmosphere."
        music = [
            "🎵 Soft Piano",
            "🎵 Instrumental",
            "🎵 Slow Acoustic"
        ]
        activities = [
            "Journaling",
            "Relax",
            "Listen to Music"
        ]

    elif emotion == "Peaceful":
        emoji = "🌿"
        mood = "The environment feels fresh, natural, and peaceful."
        music = [
            "🎵 Nature Sounds",
            "🎵 Meditation",
            "🎵 Ambient"
        ]
        activities = [
            "Yoga",
            "Nature Walk",
            "Deep Breathing"
        ]

    else:
        emoji = "🙂"
        mood = "The scene has a neutral atmosphere."
        music = [
            "🎵 Chill",
            "🎵 Instrumental"
        ]
        activities = [
            "Relax",
            "Explore"
        ]

    st.divider()

    st.subheader("🖼️ Detected Scene")

    st.success(f"**{label.title()}**")

    st.write(f"Confidence : **{confidence:.2f}%**")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🎭 Predicted Emotion",
            f"{emoji} {emotion}"
        )

    with col2:

        st.metric(
            "📊 Emotion Score",
            f"{confidence:.2f}%"
        )

    st.divider()

    st.subheader("💬 Mood Description")

    st.info(mood)

    st.divider()

    st.subheader("🎵 Suggested Music")

    for item in music:

        st.write(item)

    st.divider()

    st.subheader("🏃 Suggested Activities")

    for activity in activities:

        st.success(f"✔ {activity}")

else:

    st.info("📷 Upload a JPG or PNG image.")