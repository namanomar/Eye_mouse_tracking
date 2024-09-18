import cv2
import mediapipe as mp
import pyautogui

# Initialize camera and MediaPipe Face Mesh model
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Get screen dimensions for cursor positioning
screen_w, screen_h = pyautogui.size()

while True:
    # Capture frame from the camera
    _, frame = cam.read()
    # Flip the frame horizontally to match the mirror image
    frame = cv2.flip(frame, 1)
    # Convert the frame to RGB as MediaPipe requires RGB input
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame with MediaPipe to detect face landmarks
    output = face_mesh.process(rgb_frame)
    # Get the landmarks from the output
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        # Get landmarks for the detected face
        landmarks = landmark_points[0].landmark
        # Loop through specific landmarks for eyes (right eye landmarks)
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)  # Convert normalized x to pixel coordinate
            y = int(landmark.y * frame_h)  # Convert normalized y to pixel coordinate
            # Draw a circle at the landmark position
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:  # Track the second landmark (typically the center of the iris)
                # Map the iris position to screen coordinates
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                # Move the mouse cursor to the calculated screen position
                pyautogui.moveTo(screen_x, screen_y)

        # Detect eye blink by comparing vertical positions of specific eye landmarks
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            # Draw circles around the eye landmarks
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        # Check if the vertical distance between the two landmarks is small, indicating a blink
        if (left[0].y - left[1].y) < 0.004:
            # Simulate a mouse click if a blink is detected
            pyautogui.click()
            pyautogui.sleep(1)  # Sleep to avoid multiple clicks

    # Display the frame with detected landmarks and mouse movement
    cv2.imshow('Eye Controlled Mouse', frame)
    # Press 'ESC' to exit
    key = cv2.waitKey(30)
    if key == 27:
        break

# Release camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
