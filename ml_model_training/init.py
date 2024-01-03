import streamlit as st
from pathlib import Path

def init():
    if "rtsp_connection_string" not in st.session_state:
        st.session_state["rtsp_connection_string"] = "rtsp://192.168.50.17:8080/h264_ulaw.sdp"

    if "inference_stream_fps" not in st.session_state:
        st.session_state["inference_stream_fps"] = "30"

    if "base_model" not in st.session_state:
        st.session_state["base_model"] = "yolov8n.pt"

    if "object_label" not in st.session_state:
        st.session_state["object_label"] = "robot"

    if "workspace_path" not in st.session_state:
        st.session_state["workspace_path"] = "/tmp/smarter_vaccum_bot"

    Path(st.session_state["workspace_path"]).mkdir(parents=True, exist_ok=True) 
    Path(f"{st.session_state['workspace_path']}/raw").mkdir(parents=True, exist_ok=True) 
    Path(f"{st.session_state['workspace_path']}/processed").mkdir(parents=True, exist_ok=True) 