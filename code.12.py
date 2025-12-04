import cv2

# Read the image
img = cv2.imread(r"C:\Users\psadi\Downloads\jpg_44-2.jpg")  # Replace with your image path
# Check if image is loaded correctly
if img is None:
    print("Error: Could not read image. Check the file path and name.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Display the image with contours
cv2.imshow("Contours", img)

# Wait for a key press, then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
