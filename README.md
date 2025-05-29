# 🧠 Face & Gesture Recognition 

A Python-based computer vision project using OpenCV and DeepFace that allows you to:
- Capture a user's face via webcam
- Verify the face against known users
- Analyze facial attributes (age, gender, emotion, race)
- Extend functionality for gesture-based controls (future scope)

---

## 📦 Requirements

Install all dependencies using:

pip install opencv-python deepface mediapipe pyautogui pynumpy

---

## 🖼️ 1. Face Capture

**File:** `face_capture.py`

Captures an image using your webcam and saves it locally.

### Usage:
python face_capture.py


**Controls:**
- Press **'c'** to capture and save the face.
- Press **'q'** to quit.

---

## 🧾 2. Face Verification

**File:** `face_verifier.py`

Compares the captured image with a list of known faces in the `known_users/` folder.

### Usage:
python face_verifier.py


### Notes:
- Uses the **Facenet** model and **RetinaFace** detector from `DeepFace`.
- Ensure `known_users/` exists and contains `.jpg`, `.png`, or `.jpeg` files.

---

## 🔍 3. Face Analysis

**File:** `face_analysis.py`

Analyzes the captured face for the following attributes:
- Age
- Gender
- Dominant Emotion
- Dominant Race

### Usage:
python face_analysis.py


---

## ✋ 4. Gesture (Optional / Expandable)

**File:** `virtual_mouse.py`

This module is a placeholder for future gesture-based extensions using OpenCV and MediaPipe.

---

## 📂 Folder Setup

Ensure this folder structure exists before running:
face-gesture/
|──Gesture_Control
├── known_users/
│ ├── user1.jpg
│ └── user2.png

Captured face is saved as `captured_face.jpg` in the main directory.








