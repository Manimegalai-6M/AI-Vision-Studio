import streamlit as st

from transformers import BlipProcessor, BlipForConditionalGeneration


@st.cache_resource
def load_caption_model():

    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    return processor, model