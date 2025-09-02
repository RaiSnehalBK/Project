from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2

# 🎥 Video generator
def gen_frames():
    # Change this to your RTSP camera stream
    cap = cv2.VideoCapture("rtsp://rtspstream:tt5Hws7W2bHhqTfXIIRV8@zephyr.rtsp.stream/traffic")

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# 🎥 Video feed endpoint
def video_feed(request):
    return StreamingHttpResponse(gen_frames(),
        content_type='multipart/x-mixed-replace; boundary=frame'
    )

# 🏠 Dashboard view
def dashboard(request):
    # Dummy data (replace with database values later)
    patient = {
        "name": "John Doe",
        "age": 45,
        "disease": "Cardiac Arrest"
    }


    return render(request, "main/dashboard.html", {
        "patient": patient,
 
    })

# Other pages

def profile(request):
    return render(request, "main/profile.html")

def settings(request):
    return render(request, "main/settings.html")

def logout(request):
    return render(request, "main/logout.html")


