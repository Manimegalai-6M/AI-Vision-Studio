from ultralytics import YOLO
import streamlit as st


@st.cache_resource
def load_yolo():

    return YOLO("yolov8n.pt")