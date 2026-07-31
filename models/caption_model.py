from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_caption_model():
    """
    Load the BLIP Image Captioning model.
    The model is cached so it loads only once.
    """
    return pipeline(
        "image-to-text",
        model="Salesforce/blip-image-captioning-base"
    )