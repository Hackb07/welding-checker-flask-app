from ultralytics import YOLO
import cv2

model = YOLO("welding.pt")

def detect_image(image_path):
    results = model(image_path)
    annotated_path = f"static/outputs/result.jpg"
    for r in results:
        r.save(filename=annotated_path)
    return annotated_path, results[0].boxes.data.tolist()

def detect_frame(frame):
    results = model(frame)
    return results[0].plot()
