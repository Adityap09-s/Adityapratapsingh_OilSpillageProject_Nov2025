# Adityapratapsingh_OilSpillageProject_Nov2025
[Adityapratapsingh_oil_spillageproject_Nov 2025.pdf](https://github.com/user-attachments/files/23944550/Adityapratapsingh_oil_spillageproject_Nov.2025.pdf)



🌊 Oil Spill Detection System
An innovative, comprehensive web application for detecting oil spills in images and videos using advanced YOLOv11 deep learning model. Built with Streamlit for an intuitive, user-friendly interface.

✨ Features
🎯 Core Capabilities
📸 Image Detection: Upload single or multiple images for batch processing
🎥 Video Detection: Process video files frame-by-frame with progress tracking
📹 Real-time Camera: Live detection from webcam with real-time statistics
📊 Analytics Dashboard: Comprehensive statistics, visualizations, and insights
⚙️ Customizable Settings: Adjust confidence thresholds and preferences
🚀 Advanced Features
Batch Processing: Handle multiple images simultaneously
Interactive Visualizations: Plotly charts for confidence distributions and timelines
Export Options: Download results in multiple formats (TXT, CSV, JSON)
Heatmap Overlays: Visualize detection density
Coverage Analysis: Calculate spill coverage percentages
Detection History: Track and analyze detection patterns over time
Real-time Statistics: Live metrics during processing
GPU Support: Automatic GPU acceleration when available
📋 Requirements
Python 3.10 or higher
CUDA-capable GPU (optional, for faster processing)
Webcam (optional, for real-time detection)
🛠️ Installation
Option 1: Using Conda (Recommended)
Create the conda environment:

conda env create -f environment.yml
Activate the environment:

conda activate oil_spill
Run the application:

streamlit run app.py
Option 2: Using pip
Create a virtual environment (optional but recommended):

python -m venv oil_spill_env
source oil_spill_env/bin/activate  # On Windows: oil_spill_env\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Run the application:

streamlit run app.py
📁 Project Structure
oil_spill/
├── app.py                      # Main Streamlit application
├── best.pt                     # YOLOv11 trained model
├── pages/                      # Multi-page application pages
│   ├── 1_📸_Image_Detection.py
│   ├── 2_🎥_Video_Detection.py
│   ├── 3_📹_Real-time_Camera.py
│   ├── 4_📊_Analytics_Dashboard.py
│   └── 5_⚙️_Settings.py
├── utils/                      # Utility modules
│   ├── model_loader.py         # Model loading and caching
│   ├── image_processor.py      # Image processing functions
│   ├── video_processor.py      # Video processing functions
│   ├── visualizations.py       # Visualization utilities
│   └── report_generator.py     # Report generation
├── requirements.txt            # Python dependencies
├── environment.yml             # Conda environment file
└── README.md                   # This file
🎮 Usage
Image Detection
Navigate to 📸 Image Detection page
Upload one or more images (PNG, JPG, JPEG, BMP, TIFF)
Adjust confidence threshold in the sidebar
View detection results with bounding boxes
Export results in various formats
Video Detection
Navigate to 🎥 Video Detection page
Upload a video file (MP4, AVI, MOV, MKV, etc.)
Preview sample frames
Process the video (progress bar shows status)
Download annotated video and analysis reports
Real-time Camera
Navigate to 📹 Real-time Camera page
Click "Start Camera" button
View live detections with real-time statistics
Click "Stop Camera" when finished
Analytics Dashboard
Navigate to 📊 Analytics Dashboard page
View comprehensive statistics and visualizations
Analyze detection patterns over time
Export analytics data
⚙️ Configuration
Model Settings
Confidence Threshold: Adjust detection sensitivity (0.0 - 1.0)
Device: Automatically uses GPU if available, falls back to CPU
Application Settings
Customize display preferences
Configure export formats
Adjust processing parameters
📊 Supported Formats
Input
Images: PNG, JPG, JPEG, BMP, TIFF
Videos: MP4, AVI, MOV, MKV, FLV, WMV
Output
Annotated Images/Videos: With bounding boxes and labels
Text Reports: Detailed detection information
CSV Files: Structured data for analysis
JSON Files: Machine-readable results
🔧 Technical Details
Model: YOLOv11 (Ultralytics)
Framework: PyTorch
Web Framework: Streamlit
Visualization: Plotly, Matplotlib
Image Processing: OpenCV, PIL
Data Handling: Pandas, NumPy
🎨 UI Features
Modern Design: Clean, intuitive interface
Responsive Layout: Works on different screen sizes
Custom Styling: Enhanced visual appearance
Progress Indicators: Real-time processing feedback
Interactive Charts: Plotly visualizations
Color-coded Alerts: Visual feedback for detections
🚀 Performance Tips
Use GPU: Ensure CUDA is available for faster processing
Batch Processing: Process multiple images together for efficiency
Adjust Thresholds: Lower confidence threshold for more detections (may include false positives)
Video Resolution: Lower resolution videos process faster
📝 Notes
The model file (best.pt) must be in the project root directory
First run may take longer as the model loads
GPU acceleration significantly improves processing speed
Large videos may take time to process - be patient!
🐛 Troubleshooting
Model not loading
Ensure best.pt exists in the project directory
Check file permissions
Camera not working
Verify camera permissions
Check if camera is being used by another application
Slow processing
Use GPU if available
Reduce image/video resolution
Process fewer images at once
Import errors
Ensure all dependencies are installed
Activate the correct conda/virtual environment
📄 License
This project is provided as-is for demonstration and research purposes.

🙏 Acknowledgments
YOLOv11 by Ultralytics
Streamlit for the web framework
All open-source contributors
📝 Practice Code Summaries
This section contains brief summaries of various practice codes covering image processing, computer vision, and NLP tasks, showing inputs and outputs for each.

Code_1:
Input: No input
Output: Live webcam video feed in a window titled "Camera Stream" until ‘q’ is pressed.

Code_2:
Input: No input
Output: Live webcam feed with each frame saved sequentially in a folder named frames.

Code_3:
Input: Image file path
Output: Displays the image or prints "Error: Could not read image."

Code_4:
Input: Image file path
Output: Four windows showing original and flipped images; error if loading fails.

Code_5:
Input: Image file path
Output: Shows original and resized 300x300 image; saves resized as resized_output.jpg.

Code_6:
Input: Image file path
Output: Shows original and grayscale images; saves grayscale as grayscale_output.jpg.

Code_7:
Input: Image file path
Output: Displays original and Gaussian-blurred images; saves blurred as blurred_output.jpg.

Code_8:
Input: No input
Output: Displays a 500x500 black image with a line, rectangle, circle, and text.

Code_9:
Input: Image file path
Output: Shows grayscale image and its binary thresholded version.

Code_10:
Input: Image file path
Output: Displays Canny edge-detected image in a window titled "Edges".

Code_11:
Input: Image file path
Output: Shows image with blue rectangles around detected faces.

Code_12:
Input: Image file path
Output: Displays image with detected contours highlighted in green.

Code_13:
Input: Image file path
Output: Shows original image, blue mask, and filtered blue regions.

Code_14:
Input: Image file path
Output: Displays extracted foreground in a window.

Code_15:
Input: No input
Output: Live webcam feed highlighting blue-colored regions in real time.

Code_16:
Input: Image file path
Output: Displays thresholded, eroded, and dilated images.

Code_17:
Input: Text string
Output: List of cleaned, tokenized, lemmatized words.

Code_18:
Input: List of sentences
Output: Classification report, confusion matrix, predictions, and class probabilities.

Code_19:
Input: List of sentences
Output: Best parameters, best CV F1 score, and a sample prediction.

Code_20:
Input: List of sentences
Output: Vocabulary list and TF-IDF matrix of the input texts.

Code_21:
Input: Text string
Output: Named Entities, POS with lemmas, and noun chunks extracted from text.

Code_22:
Input: List of sentences
Output: Classification report for sentiment prediction.

Code_23:
Input: List of sentences
Output: Cosine similarity matrix showing pairwise similarity scores.

Code_24:
Input: List of sentences
Output: Topics discovered with top words and their weights.

📧 Support
For issues, questions, or contributions, please refer to the project documentation or create an issue in the repository.

Built with ❤️ for environmental protection and oil spill detection

About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Report repository
Releases
No releases published
Packages
No packages published
Languages
Python
99.0%
 
Shell
1.0%
Footer
