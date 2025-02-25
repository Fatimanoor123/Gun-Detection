import cv2
from ultralytics import YOLO

# Load the weapon detection model
model = YOLO("best.pt")  # Ensure 'best.pt' exists in the same folder

# Load the video
video_path = "video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Error: Could not open video file. Check the file path!")
    exit()

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define output video writer (to save processed video)
output_video_path = "weapon_detection_output.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Could not read the video frame! The file might be corrupted or at the end.")
        break

    # Resize frame to match YOLO input size
    frame_resized = cv2.resize(frame, (frame_width, frame_height))

    # Run YOLO detection
    results = model(frame_resized)

    # Draw detections on the frame
    annotated_frame = results[0].plot()

    # Write processed frame to output video
    out.write(annotated_frame)

    # Show the frame with detection
    cv2.imshow("Weapon Detection", annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()


