import streamlit as st
from init import init

def main():
    init()
    st.session_state["current_page"] = "image_processing"
    st.title("Image Processing")

if __name__ == "__main__":
    main()