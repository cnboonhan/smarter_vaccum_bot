import streamlit as st
from ultralytics import YOLO
import cv2
import time
from init import init

def main():
    init()

    st.session_state["current_page"] = "test"
    st.title("Test Model")
    st.write(f"RTSP Url: {st.session_state['rtsp_connection_string']}")
    st.write(f"Model: {st.session_state['base_model']}")
    st.write(f"FPS: {st.session_state['inference_stream_fps']}")

    try:
        model = YOLO(st.session_state['base_model'])
    except Exception as e:
        print(e)

    try:
        vid_cap = cv2.VideoCapture(st.session_state['rtsp_connection_string'])
        vid_cap.set(cv2.CAP_PROP_BUFFERSIZE, 0)
        vid_cap_fps_ms = int(1 / int(st.session_state["inference_stream_fps"]) * 1000)
            
        st_frame = st.empty()
        start_time_ms = int(time.time() * 1000)
        while (vid_cap.isOpened()):
            current_time_ms = (int(time.time() * 1000))
            success, image = vid_cap.read()
            if success and st.session_state["current_page"] == "test":
                if (current_time_ms - start_time_ms > vid_cap_fps_ms):
                    res = model.track(image)
                    st_frame.image(image=res[0].plot(), channels="BGR") 
                    start_time_ms = int(time.time() * 1000)
                else:
                    pass
            else:
                vid_cap.release()
                break
    except Exception as e:
        print(e)
        vid_cap.release()
        

if __name__ == "__main__":
    main()