import cv2

# Read the image
img = cv2.imread(r"C:\Users\psadi\Downloads\image.png")
# Check if image loaded properly
if img is None:
    print("Error: Could not read image. Check the file path and name.")
    exit()

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define blue color range (tweak if needed)
lower_blue = (100, 150, 0)
upper_blue = (140, 255, 255)

# Create a mask for blue color
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply mask on the original image
result = cv2.bitwise_and(img, img, mask=mask)

# Display results
cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Filtered (Blue Detection)", result)

# Wait for a key press, then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
