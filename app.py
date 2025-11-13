import streamlit as st
import cv2
import numpy as np
from services.detection_pipeline import detect_helmet, process_video
from services.audio import play_beep

st.set_page_config(page_title="Helmet Detection AI", layout="wide")

st.title("Helmet Detection AI for ATM")

st.sidebar.header("Choose Input Type")
choice = st.sidebar.radio("Select input", ["Image", "Video", "Camera"])

st.sidebar.markdown("---")
st.sidebar.info("Model: Custom YOLOv8 Helmet Detection\n Detects helmets in images or videos")

if choice == "Image":
    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Uploaded Image", use_container_width=True)

        if st.button("Run Detection"):
            with st.spinner("Detecting..."):
                annotated_image, helmet_detected = detect_helmet(image.copy())
                st.image(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB), caption="Detection Result", use_container_width=True)

                if helmet_detected:
                    st.success("No helmet detected — Access granted.")
                else:
                    play_beep()
                    st.error("Helmet detected — Door locked / ATM blocked!")

elif choice == "Video":
    uploaded_video = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])
    if uploaded_video:
        with st.spinner("Processing video..."):
            video_path, helmet_detected = process_video(uploaded_video.name)
            st.video(video_path)

            
            if helmet_detected:
                st.success("No helmet detected in video — Access granted.")
            else:
                play_beep()
                st.error("Helmet detected in video — Door locked / ATM blocked!")

elif choice == "Camera":
    st.info("Turn on your camera and capture a frame")
    camera_input = st.camera_input("Take a picture")
    if camera_input:
        bytes_data = camera_input.getvalue()
        image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

        with st.spinner("Detecting..."):
            annotated_image, helmet_detected = detect_helmet(image.copy())
            st.image(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB), caption="Detection Result", use_container_width=True)

            
            if helmet_detected:
                st.success("No helmet detected — Access granted.")
            else:
                play_beep()
                st.error("Helmet detected — Door locked / ATM blocked!")
