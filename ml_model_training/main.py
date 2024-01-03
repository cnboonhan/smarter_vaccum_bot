import streamlit as st
from pathlib import Path
import shutil
import glob
import os
import glob
from streamlit_image_select import image_select
from streamlit_image_annotation import detection
from init import init

def main():
    init()
    st.title("Train an image model on custom dataset")
    st.session_state["current_page"] = "main"

    st.write(f"Workspace Path: {st.session_state['workspace_path']}")
    image_paths = glob.glob(f"{st.session_state['workspace_path']}/raw/*.png")
    if image_paths:
        # Select image
        image_path = image_select("Raw Images", image_paths)
        st.button("Delete", on_click=delete_image, args=(image_path, ))
        st.write(image_path)

        # edit image
        label_list = [st.session_state["object_label"]]
        image_path_list = [image_path]
        bbox = {'bboxes': [],'labels':[0]}
        new_labels = detection(image_path=image_path, 
                  bboxes=bbox["bboxes"], 
                  labels=bbox["labels"],
                  label_list=label_list, 
                  key=image_path)

        image_name = os.path.basename(image_path)
        annotation_path = f"{st.session_state['workspace_path']}/processed/{Path(image_path).stem}.txt"
        shutil.copy(image_path, f"{st.session_state['workspace_path']}/processed/{image_name}")
        if new_labels:
            with open(annotation_path, "w") as f:
                # TODO: change to csv
                f.write(str(new_labels))
                st.write(f"Written image path: {image_path}")
                st.write(f"Written annotation path: {annotation_path}")
    else:
        st.write("No images found")

def delete_image(image_path):
    try:
        os.remove(image_path)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()