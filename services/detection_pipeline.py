# services/detection_pipeline.py
from ultralytics import YOLO
import cv2
import numpy as np
import tempfile
import os

# Load model once (adjust path to your model)
MODEL_PATH = os.path.join("models", "best.pt")
model = YOLO(MODEL_PATH)

def detect_helmet(image):
    """
    Takes an OpenCV image, runs YOLO detection, and returns:
    - annotated image
    - True/False if helmet detected
    """
    results = model.predict(source=image, save=False, imgsz=640, conf=0.25, device="cpu")
    helmet_detected = False

    for result in results:
        boxes = result.boxes.xyxy
        scores = result.boxes.conf
        class_ids = result.boxes.cls

        for box, score, class_id in zip(boxes, scores, class_ids):
            x1, y1, x2, y2 = map(int, box)
            label = model.names[int(class_id)]
            confidence = float(score)

            color = (0, 255, 0)
            if "helmet" in label.lower():
                helmet_detected = True
                color = (0, 0, 255)  # red box for helmet

            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            cv2.putText(image, f'{label} {confidence:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    return image, helmet_detected


def process_video(video_file):
    """
    Process uploaded video and save annotated output temporarily.
    """
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    cap = cv2.VideoCapture(video_file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(tfile.name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    helmet_detected = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        annotated_frame, detected = detect_helmet(frame)
        if detected:
            helmet_detected = True
        out.write(annotated_frame)

    cap.release()
    out.release()
    return tfile.name, helmet_detected
