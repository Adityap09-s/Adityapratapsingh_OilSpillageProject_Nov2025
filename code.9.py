import cv2

# Load the image in grayscale mode
img = cv2.imread(r"C:\Users\psadi\Downloads\jpg_44-2.jpg", 0)  # Replace with your correct file path

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not read image.")
    exit()

# Apply thresholding (127 is threshold value, 255 is max value)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow("Original", img)
cv2.imshow("Thresholded", thresh)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
