# 🧍‍♂️ Posture Correction Application

This is a lightweight desktop application that uses [MediaPipe](https://mediapipe.dev/) and a built-in GUI to monitor and help correct your posture using your webcam. Just run the provided executable — no setup required!

## 📦 Features

- Real-time posture detection using webcam  
- Alerts for poor posture  
- Simple web-based UI embedded in a desktop window  
- Built with Python, Flask, MediaPipe, and PyWebview  
- Bundled as a **single executable**

## 🚀 How to Use

1. **Navigate to the `dist` folder**
2. **Run the file named `run`** (or `run.exe` on Windows)

The application will launch a desktop window and begin posture monitoring automatically.

## 🏗️ Build Instructions

If you want to build this yourself:

```bash
pyinstaller --onefile --add-data "app:app" run.py
```

- This bundles everything into one file under `dist/`
- Replace `run.py` with your launcher filename if different

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [MediaPipe](https://mediapipe.dev/)
- [PyWebview](https://pywebview.flowrl.com/)
- [PyInstaller](https://www.pyinstaller.org/)

## 📂 File Structure

```
📁 app/
 └── app.py, templates/, static/  <- Flask + posture logic
📁 dist/
 └── run       <- One-file executable output
run.py         <- Main launcher script
README.md
```

## 🧠 How It Works

MediaPipe tracks posture via key body points using your webcam. Flask serves the posture visualization and logic, and PyWebview wraps it into a native desktop app.

## 📝 License

This project is for educational and personal use.