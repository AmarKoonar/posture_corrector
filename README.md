# 🧍‍♂️ Posture Correction Application

This is a lightweight desktop application that uses [MediaPipe](https://mediapipe.dev/) and a built-in GUI to monitor and help correct your posture using your webcam. The app is built with Python, Flask, and PyWebview and must be compiled locally using PyInstaller.

## 📦 Features

- Real-time posture detection using webcam  
- Alerts for poor posture  
- Simple web-based UI embedded in a desktop window  
- Built with Python, Flask, MediaPipe, and PyWebview  
- Can be compiled into a **single executable**

## 🚀 How to Run

Since the `dist/` folder is not included, you need to compile the application yourself:

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Build the executable

```bash
pyinstaller --onefile --add-data "app:app" run.py
```

> 🔧 Make sure you have `pyinstaller` installed (`pip install pyinstaller`).

### 3. Run the app

Navigate to the `dist/` folder created by PyInstaller and run the generated `run` file.

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
run.py         <- Main launcher script
requirements.txt
README.md
```

## 🧠 How It Works

MediaPipe tracks posture via key body points using your webcam. Flask serves the posture visualization and logic, and PyWebview wraps it into a native desktop app.

## 📝 License

This project is for educational and personal use.