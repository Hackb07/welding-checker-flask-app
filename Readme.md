# 🧠 YOLOv8 Object Detection Web App with Image Upload & IP Camera Streaming

This project demonstrates a complete integration of **YOLOv8** (Ultralytics) with a **Flask web interface**, allowing users to:
- 📷 Upload images for object detection
- 🌐 Input and stream live video from any **IP Camera URL** (e.g., CCTV, mobile camera apps)

A modern, responsive UI in a clean blue-white theme is provided for user-friendly interaction.

---

## 📁 Project Structure

```

yolo\_flask\_app/
├── app.py                      # Main Flask backend
├── detect.py                   # YOLOv8 inference logic
├── yolov8\_model.pt             # Your YOLOv8 model (custom or pre-trained)
├── requirements.txt            # Required Python packages
├── static/
│   ├── uploads/                # For uploaded images
│   └── outputs/                # For detected results
├── templates/
│   ├── index.html              # Unified UI (Image + IP Cam)
│   └── live\_feed.html          # IP camera stream page
└── README.md                   # This file

````

---

## ⚙️ Requirements

- Python 3.8+
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- Flask
- OpenCV

Install all dependencies using:

```bash
pip install -r requirements.txt
````

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/yolo-flask-app.git
cd yolo-flask-app
```

### 2️⃣ Download or Place YOLOv8 Model

Place your model as:

```bash
yolov8_model.pt
```

To download a pre-trained model:

```bash
yolo download model=yolov8n.pt
```

### 3️⃣ Run the Flask App

```bash
python app.py
```

Access the app at:

```
http://127.0.0.1:5000/
```

---

## 🖼️ Features

| Feature                | Description                                        |
| ---------------------- | -------------------------------------------------- |
| 📁 Image Upload        | Upload local image and detect objects              |
| 🌐 IP Camera Detection | Stream from any camera URL (e.g., IP Webcam, CCTV) |
| 🧠 YOLOv8 Inference    | Uses Ultralytics YOLOv8 for real-time detection    |
| 🎨 Clean Modern UI     | Responsive frontend in blue-white theme            |
| 📊 Bounding Box Output | List of box coordinates and metadata               |
| 💻 Local Deployment    | Simple Flask backend with OpenCV integration       |

---

## 🌐 IP Camera Support

You can stream from any **MJPEG-compatible URL**, e.g.:

* Mobile IP Webcam (Android):

  ```
  http://<phone_ip>:8080/video
  ```
* CCTV stream (if MJPEG or RTSP, may require conversion)

---

## 🧠 Technologies Used

| Technology         | Role                            |
| ------------------ | ------------------------------- |
| Flask              | Web framework                   |
| Ultralytics YOLOv8 | Object detection engine         |
| OpenCV             | Video stream and frame handling |
| HTML + CSS         | Frontend UI                     |
| Python             | Backend logic                   |

---

## 📺 Demo Screens

### Image Upload

![Image Upload](https://user-images.githubusercontent.com/placeholder/image-upload.png)

### IP Camera Live Detection

![Live Stream](https://user-images.githubusercontent.com/placeholder/live-stream.png)

> 📌 *(Replace screenshots above with actual usage images if available)*

---

## 🔮 Future Enhancements

* Webcam (`/dev/video0`) support
* Dropdown to select multiple YOLO models (v5, v8)
* Overlay class labels and confidence on stream
* Save detection history and analytics
* Deploy to cloud (Render, Railway, HuggingFace Spaces)

---

## 👨‍💻 Author

**Name:** B. Tharun Bala
**Department:** Artificial Intelligence and Data Science
**College:** ER. Perumal Manimekalai College of Engineering, Hosur
**Email:** balat4880@gmial.com
**Roll No:** 610823U243059

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🗂 Sample IP Camera Apps

| App                                                                       | Platform              | URL Format                               |
| ------------------------------------------------------------------------- | --------------------- | ---------------------------------------- |
| [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) | Android               | `http://<IP>:8080/video`                 |
| [DroidCam](https://www.dev47apps.com/)                                    | Android/Windows/Linux | Custom                                   |
| Any RTSP IP Camera                                                        | -                     | Use RTSP-to-MJPEG converter or GStreamer |

---
