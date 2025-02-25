# 🔫 Gun Detection Using YOLO

This project implements a **gun detection system** using **YOLO (You Only Look Once)** for object detection. It processes a video, detects weapons in each frame, and saves the annotated video.

---

## 🚀 Features
- Real-time weapon detection in videos
- Bounding box annotations on detected weapons
- Saves the output video with detections
- Easy-to-use Python implementation

---

## 📌 Requirements

Make sure you have the following dependencies installed before running the project:

```bash
pip install ultralytics opencv-python
```

---

# 🛠 Installation & Setup

## Clone the Repository
To get started, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/weapon-detection-yolo.git
cd weapon-detection-yolo
```

## Ensure You Have the Model File
Download `best.pt` (your trained YOLO model) and place it in the project directory.

## Install Dependencies
Make sure you have the required dependencies installed:

```bash
pip install ultralytics opencv-python
```

## Run the Detection Script
Execute the following command to run the detection script:

```bash
python weapon_detection.py
```

- Ensure `video.mp4` exists in the directory or update the script to match the correct file path.
- The output will be saved as `weapon_detection_output.mp4`.

## Exit the Program
- The program will display video frames with detected weapons.
- To stop execution, press **'q'** on your keyboard.

---

# 📜 Code Overview

- **Load the YOLO model** to detect weapons.
- **Process the input video**, frame by frame.
- **Apply object detection** using the trained model.
- **Save and display results** in a new video file with detections.
- **Exit when 'q' is pressed**.

---

# 📂 File Structure

```bash
weapon-detection-yolo/
├── best.pt                   # YOLO model file
├── video.mp4                 # Input video
├── weapon_detection.py       # Main script
├── README.md                 # Project documentation
└── weapon_detection_output.mp4  # Output video (after detection)
```

---

# 🖥 Example Output




https://github.com/user-attachments/assets/28a04e37-afad-45b2-8291-423bcf17fc6d




# 📢 Notes
- If you need to train your own model, refer to the official [Ultralytics YOLO documentation](https://docs.ultralytics.com/).
- For real-time detection, you can modify the code to process a webcam feed.

---

- Go to your repository link and check if all files are uploaded.

---

🎯 **Happy Coding!** 🚀

