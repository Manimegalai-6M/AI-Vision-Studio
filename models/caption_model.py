from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_caption_model():
    return pipeline(
        task="image-text-to-text",
        model="Salesforce/blip-image-captioning-base"
    )