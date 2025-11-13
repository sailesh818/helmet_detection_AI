# 🪖 Helmet Detection System using YOLOv8 and Streamlit

This project is a **real-time Helmet Detection System** built with **YOLOv8** and **Streamlit**.  
It detects whether a person is **wearing a helmet or not** from **images, videos, or live camera input**.  
The app also includes an alert system — it plays a **beep sound** and shows a warning message if a person is **not wearing a helmet**.

---

## 🚀 Features

✅ Detect helmets using a **custom fine-tuned YOLOv8 model**  
✅ Supports **image upload**, **video upload**, and **camera input**  
✅ **Audio alert (beep)** when a person is not wearing a helmet  
✅ **Visual feedback** (green for helmet, red for no helmet)  
✅ Simulates real-world scenarios like:
- 🚫 Door lock or ATM access denied if no helmet detected  
✅ Clean and responsive **Streamlit UI**

---

## 🧠 Tech Stack

- **Python 3.8+**
- **YOLOv8 (Ultralytics)**
- **OpenCV**
- **Streamlit**

---

## 🗂️ Folder Structure
helmet_detection_app/
│
├── app.py # Streamlit main app (UI)
│
├── models/
│ └── best.pt # Custom YOLOv8 trained model
│
└── services/
├── detection_pipeline.py # YOLO detection logic (image/video)
└── audio.py # Beep sound alert system


---

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/helmet-detection-app.git
cd helmet-detection-app


2️⃣ Install dependencies
pip install streamlit ultralytics opencv-python


(Optional for sound support on Linux/Mac)

sudo apt install sox

3️⃣ Place your model

Copy your YOLO trained weights file (e.g., best.pt) into the models/ folder.

▶️ Run the App
streamlit run app.py


Then open your browser — usually at:

http://localhost:8501

🧩 How It Works

Upload an image, video, or capture from camera

The YOLOv8 model detects objects in the frame

If a helmet is detected → ✅ Access granted

If no helmet is detected → 🚫 Door locked / ATM blocked + 🔊 Beep sound
