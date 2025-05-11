from flask import Flask, render_template, Response, request
import cv2
import mediapipe as mp
import numpy as np
from playsound import playsound
import threading

app = Flask(__name__)

# Global variables
camera = cv2.VideoCapture(0)
camera_active = True
min_posture_y = 1
latest_landmarks = None
sound_played = False

# MediaPipe setup
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

def play_alert_sound():
    threading.Thread(target=playsound, args=('alert.wav',), daemon=True).start()

def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.degrees(np.arccos(cosine_angle))

def generate_frames():
    global latest_landmarks, camera_active, sound_played, min_posture_y

    while True:
        if not camera_active:
            break

        success, frame = camera.read()
        if not success:
            continue

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, _ = frame.shape
        results = pose.process(image)


        cv2.line(frame, (0, int(min_posture_y * h)), (w, int(min_posture_y * h)), (255, 0, 0), 2)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            latest_landmarks = landmarks

            left_y = landmarks[11].y
            right_y = landmarks[12].y

            posture_good = not (left_y > min_posture_y or right_y > min_posture_y)
            color = (0, 255, 0) if posture_good else (0, 0, 255)

            if not posture_good:
                if not sound_played:
                    play_alert_sound()
                    sound_played = True
            else:
                sound_played = False

            cv2.putText(frame, "Posture OK" if posture_good else "Bad Posture",
                        (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            #mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set-posture', methods=['POST'])
def set_posture():
    global latest_landmarks, min_posture_y
    if latest_landmarks:
        left_y = latest_landmarks[11].y
        right_y = latest_landmarks[12].y
        min_posture_y = max(left_y, right_y) + 0.01
        print("Posture baseline set to:", min_posture_y)
        return ('', 204)
    else:
        return 'No pose detected', 400

@app.route('/stop-camera', methods=['POST'])
def stop_camera():
    global camera_active
    camera_active = False
    print("Camera display stopped by user.")
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
