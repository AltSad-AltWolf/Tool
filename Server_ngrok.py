import sys
import os
import subprocess
import threading
import requests
import json

from PyQt5.QtWidgets import *
from flask import Flask, request, jsonify
from PyQt5.QtCore import QTimer


# ---------------- FLASK SERVER ----------------

app = Flask(__name__)
received_data = []

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    received_data.append(data)
    print("Data reçue :", data)
    return jsonify({"status": "ok"})


def run_flask():
    app.run(port=5000)


# ---------------- INTERFACE ----------------

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Server Interface")
        self.resize(600, 400)

        self.ngrok_url = None

        layout = QVBoxLayout()

        self.start_btn = QPushButton("Start ngrok")
        self.build_btn = QPushButton("Build script")

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        layout.addWidget(self.start_btn)
        layout.addWidget(self.build_btn)
        layout.addWidget(self.log)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.start_btn.clicked.connect(self.start_server)
        self.build_btn.clicked.connect(self.build_script)

        # refresh affichage data
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_log)
        self.timer.start(2000)

    # ---------- START SERVER ----------
    def start_server(self):

        self.log.append("Starting Flask server...")

        threading.Thread(target=run_flask, daemon=True).start()

        self.log.append("Starting ngrok...")

        subprocess.Popen("ngrok http 5000", shell=True)

        threading.Thread(target=self.get_ngrok_url, daemon=True).start()

    # ---------- GET NGROK URL ----------
    def get_ngrok_url(self):
        import time
        time.sleep(3)

        try:
            res = requests.get("http://127.0.0.1:4040/api/tunnels")
            self.ngrok_url = res.json()['tunnels'][0]['public_url']
            self.log.append(f"NGROK URL : {self.ngrok_url}")
        except:
            self.log.append("Erreur récupération URL ngrok")

    # ---------- BUILD SCRIPT ----------
    def build_script(self):

        if not self.ngrok_url:
            self.log.append("Lance ngrok d'abord")
            return

        file_path, _ = QFileDialog.getOpenFileName(self, "Choisir script", "", "Python Files (*.py)")
        if not file_path:
            return

        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        code = code.replace("URL_NGROK_ICI", self.ngrok_url)

        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        output = os.path.join(desktop, "built_script.py")

        with open(output, "w", encoding="utf-8") as f:
            f.write(code)

        self.log.append("Script buildé sur le bureau")

    # ---------- UPDATE LOG ----------
    def update_log(self):
        if received_data:
            formatted = json.dumps(received_data[-1], indent=2, ensure_ascii=False)
            self.log.append(formatted)


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app_qt = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app_qt.exec_())
