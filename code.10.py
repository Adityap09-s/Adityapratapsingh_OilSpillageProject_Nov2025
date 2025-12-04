import cv2

# Read the image in grayscale mode
img = cv2.imread(r"C:\Users\psadi\Downloads\jpg_44-2.jpg", 0)

# Check if the image loaded successfully
if img is None:
    print("Error: Could not read image.")
    exit()

# Apply Canny Edge Detection
edges = cv2.Canny(img, 100, 200)

# Show the edges
cv2.imshow("Edges", edges)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
