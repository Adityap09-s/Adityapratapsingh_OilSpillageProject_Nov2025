import cv2
import os

# Start webcam
cap = cv2.VideoCapture(0)

# Create output folder
os.makedirs("frames", exist_ok=True)
frame_count = 0

while True:
    ret, frame = cap.read()  # Read frame from camera
    if not ret:
        break

    # Show live video
    cv2.imshow("Camera Stream", frame)

    # Save each frame as an image
    filename = f"frames/frame_{frame_count:06d}.jpg"
    cv2.imwrite(filename, frame)
    frame_count += 1

    # Stop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
