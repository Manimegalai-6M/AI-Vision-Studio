from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_classifier():
    """
    Load the Hugging Face image classification model once.
    """
    return pipeline(
        task="image-classification",
        model="google/vit-base-patch16-224"
    )

def classify_image(image, top_k=5):
    """
    Classify an uploaded image.
    """
    classifier = load_classifier()
    return classifier(image, top_k=top_k)