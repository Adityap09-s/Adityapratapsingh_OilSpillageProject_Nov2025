import cv2
import numpy as np

# Create a black image (500x500 pixels, 3 color channels)
img = np.zeros((500, 500, 3), dtype="uint8")

# Draw a blue line
cv2.line(img, (0, 0), (500, 500), (255, 0, 0), 5)

# Draw a green rectangle
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)

# Draw a red filled circle
cv2.circle(img, (300, 300), 80, (0, 0, 255), -1)

# Add white text
cv2.putText(img, "OpenCV Demo", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the image
cv2.imshow("Shapes and Text", img)
print("Press any key on the image window to close...")
cv2.waitKey(0)
cv2.destroyAllWindows()
