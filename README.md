# 🧍‍♂️ Posture Correction Application

This is a lightweight desktop application that uses [MediaPipe](https://mediapipe.dev/) to monitor and help correct your posture using your webcam. No setup required — just run the executable and you're good to go!

## 📦 Features

- Real-time posture detection using your webcam  
- Alerts for poor posture  
- Built with Python and MediaPipe  
- No installation needed — single executable

## 🚀 How to Use

1. **Navigate to the `dist` folder** in this project directory.
2. **Run the file named `run`** (or `run.exe` on Windows).

That's it! The posture correction system will launch and start monitoring your posture immediately.

## 🛠️ Built With

- [Python](https://www.python.org/)
- [MediaPipe](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/) (for webcam access and display)
- [PyInstaller](https://www.pyinstaller.org/) (to package the app)

## 📂 File Structure

```
📁 dist/
 └── run       <- The compiled posture correction executable
📁 src/
 └── *.py      <- Source Python scripts
README.md
```

## 🧠 How It Works

The app uses MediaPipe's Pose solution to identify key landmarks on your body and checks for posture alignment based on the relative position of your shoulders, neck, and hips. If poor posture is detected (e.g., slouching or leaning), a visual cue or alert is triggered.

## 📝 License

This project is for educational and personal use.