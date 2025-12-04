import cv2

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to access the webcam.")
        break

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define blue color range (tune if needed)
    lower_blue = (100, 150, 0)
    upper_blue = (140, 255, 255)

    # Create mask for blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply mask to original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display windows
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Tracked", result)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    # Press 's' to save the current frame
    if key == ord('s'):
        cv2.imwrite("captured_frame.jpg", frame)
        print("Image saved as 'captured_frame.jpg'")

    # Press 'q' to quit
    elif key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
