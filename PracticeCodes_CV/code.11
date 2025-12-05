import cv2

# Load pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Read the image (use your correct file path)
img = cv2.imread(r"C:\Users\psadi\Downloads\wp8548463-sunita-williams-wallpapers.jpg")

# Check if image is loaded correctly
if img is None:
    print("Error: Could not read image. Check the file path and name.")
    exit()

# Convert to grayscale (required for detection)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow("Face Detection", img)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
