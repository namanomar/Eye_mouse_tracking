# 👀Eye Controlled Mouse

![Python](https://img.shields.io/badge/Python-3.9-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5.3-brightgreen)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8.9-yellow)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9.53-orange)

## Project Overview

Eye Controlled Mouse is a project that enables controlling the mouse cursor and performing clicks based on eye movements using a webcam. The project leverages **OpenCV** for image processing, **MediaPipe** for face and eye landmark detection, and **PyAutoGUI** for cursor control and clicking.

## Tech Stack

- **Python**: Programming language used.
- **OpenCV**: Library for computer vision tasks.
- **MediaPipe**: Framework for face mesh and landmark detection.
- **PyAutoGUI**: Library for automating GUI interactions.

## Workflow

1. **Capture Video**:
   - The project uses a webcam to capture real-time video frames.

2. **Face and Eye Landmark Detection**:
   - MediaPipe’s Face Mesh model processes each frame to detect facial landmarks.
   - The landmarks corresponding to the eyes are used for gaze and blink detection.

3. **Cursor Control**:
   - The position of the iris (detected from specific landmarks) is mapped to screen coordinates.
   - The cursor is moved based on the iris position using PyAutoGUI.

4. **Blink Detection**:
   - Eye blink is detected by monitoring the vertical position of specific eye landmarks.
   - A significant decrease in the vertical distance between landmarks indicates a blink, which is used to simulate a mouse click.

5. **Display and Interaction**:
   - The video feed with detected landmarks is displayed in a window.
   - The user can interact with the application by blinking to perform clicks.

## Usage

1. **Install Dependencies**:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```
2. **Run the Application:**
  ```bash
  python app.py
  ```
