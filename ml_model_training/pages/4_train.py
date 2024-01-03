import streamlit as st
from init import init

def main():
    init()
    st.session_state["current_page"] = "train"
    st.title("Train Model")

if __name__ == "__main__":
    main()