from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO(r"C:\Users\psadi\Downloads\yolo11n-seg.pt")

# Define source as YouTube video URL
source = "https://youtu.be/LNwODJXcvt4"

# Run inference on the source
results = model(source, stream=True)  # generator of Results objects
