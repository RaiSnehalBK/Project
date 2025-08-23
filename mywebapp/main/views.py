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

    journey = {
        "distance": 12,   # in km
        "eta": 25         # in minutes
    }

    return render(request, "main/dashboard.html", {
        "patient": patient,
        "journey": journey
    })

# Other pages
def location(request):
    return render(request, "main/location.html")

def profile(request):
    return render(request, "main/profile.html")

def settings(request):
    return render(request, "main/settings.html")

def logout(request):
    return render(request, "main/logout.html")

import json
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
def update_profile(request):
    if request.method == "POST":
        data = json.loads(request.body)
        profile = request.user.profile
        profile.phone = data.get("phone", profile.phone)
        request.user.email = data.get("email", request.user.email)
        profile.save()
        request.user.save()
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"}, status=400)

@login_required
def upload_photo(request):
    if request.method == "POST" and request.FILES.get("photo"):
        profile = request.user.profile
        profile.photo = request.FILES["photo"]
        profile.save()
    return redirect("profile")  # reload profile page
