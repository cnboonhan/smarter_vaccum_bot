import streamlit as st
from pathlib import Path
from init import init

def main():
    init()

    st.title("Configuration")
    st.session_state["current_page"] = "configuration"
    st.session_state["rtsp_connection_string"] = st.text_input("RTSP Connection String ( Camera )", st.session_state["rtsp_connection_string"])
    st.session_state["inference_stream_fps"] = st.text_input("Inference Stream FPS", st.session_state["inference_stream_fps"])
    st.session_state["base_model"] = st.text_input("Base Model", st.session_state["base_model"])
    st.session_state["object_label"] = st.text_input("Object Label", st.session_state["object_label"])
    st.session_state["workspace_path"] = st.text_input("Workspace Path", st.session_state["workspace_path"])

if __name__ == "__main__":
    main()