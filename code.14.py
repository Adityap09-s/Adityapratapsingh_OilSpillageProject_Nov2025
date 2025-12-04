import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\psadi\Downloads\jpg_44-2.jpg")  # Replace with your image path

# Check if image loaded properly
if img is None:
    print("Error: Could not read image. Check the file path and name.")
    exit()

# Create mask and models
mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Define rectangle for the object (x, y, width, height)
rect = (50, 50, 400, 500)

# Apply GrabCut algorithm
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Create final mask
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Extract the foreground
result = img * mask2[:, :, np.newaxis]

# Display results
cv2.imshow("Original", img)
cv2.imshow("Foreground Extracted", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
