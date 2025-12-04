import cv2
import numpy as np

# Step 1: Read the image in grayscale
img = cv2.imread(r"C:\Users\psadi\Downloads\jpg_44-2.jpg", 0)  # replace with correct path

# Check if image loaded correctly
if img is None:
    print("Error: Could not read image.")
    exit()

# Step 2: Apply binary inverse thresholding
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# Step 3: Define a 5x5 kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Step 4: Apply erosion
erosion = cv2.erode(thresh, kernel, iterations=1)

# Step 5: Apply dilation
dilation = cv2.dilate(thresh, kernel, iterations=1)

# Step 6: Display results
cv2.imshow("Original Thresholded Image", thresh)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)

# Step 7: Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
