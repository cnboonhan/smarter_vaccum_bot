import streamlit as st
import cv2
from streamlit_image_coordinates import streamlit_image_coordinates
import tempfile
from init import init

def main():
    init()
    st.session_state["current_page"] = "image_capture"
    st.title("Image Capture")
    st.write(f"Workspace Path: {st.session_state['workspace_path']}")
    st.button("Capture", on_click=capture_image)

    try:
        vid_cap = cv2.VideoCapture(st.session_state['rtsp_connection_string'])
        vid_cap.set(cv2.CAP_PROP_BUFFERSIZE, 0)
        st_frame = st.empty()
        while (vid_cap.isOpened()):
            success, image = vid_cap.read()
            if success and st.session_state["current_page"] == "image_capture":
                st_frame.image(image=image, channels="BGR") 
            else:
                vid_cap.release()
                break
    except Exception as e:
        print(e)
        vid_cap.release()

def capture_image():
    vid_cap = cv2.VideoCapture(st.session_state['rtsp_connection_string'])
    while (vid_cap.isOpened()):
        success, image = vid_cap.read()
        if success:
            with tempfile.NamedTemporaryFile(prefix=f"{st.session_state['workspace_path']}/raw/", 
                                             suffix='.png',
                                             delete=False) as f:
                cv2.imwrite(f.name, image)
            break
    
if __name__ == "__main__":
    main()