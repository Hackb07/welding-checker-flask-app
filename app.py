from flask import Flask, render_template, request, redirect, url_for, Response
import os
import cv2
from detect import detect_image, detect_frame

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('static/outputs', exist_ok=True)

ip_cam_url = None  # Will be set by user input

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle image upload
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != "":
                img_path = os.path.join(UPLOAD_FOLDER, image.filename)
                image.save(img_path)
                result_path, boxes = detect_image(img_path)
                return render_template("index.html", result_image=result_path, boxes=boxes)

        # Handle IP camera URL input
        elif 'ip_url' in request.form:
            global ip_cam_url
            ip_cam_url = request.form.get("ip_url")
            return redirect(url_for('live'))

    return render_template("index.html")


def generate_ip_stream():
    cap = cv2.VideoCapture(ip_cam_url)
    while True:
        success, frame = cap.read()
        if not success:
            break
        detected_frame = detect_frame(frame)
        _, buffer = cv2.imencode('.jpg', detected_frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route("/live")
def live():
    return render_template("live_feed.html")


@app.route("/ip_camera_feed")
def ip_camera_feed():
    return Response(generate_ip_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
