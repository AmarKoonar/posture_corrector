import webview
from threading import Thread, Event
from app import app


stop_event = Event()
app_title = "posture_fixer"
host ="http://127.0.0.1"
port = 5000

def run():
    while not stop_event.is_set():
        app.run(port = port, use_reloader=False)

if __name__ == '__main__':
    t = Thread(target=run)
    t.dameon = True
    t.start()
    webview.create_window(
        app_title,
        f"{host}:{port}",
        resizable=False,
        height=800,
        width=800,
        frameless=False,
        easy_drag=True,
        on_top=True
    )
    webview.start()
    stop_event.set()
