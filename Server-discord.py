import sys
import os
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Builder Interface")
        self.resize(500, 300)

        layout = QVBoxLayout()

        self.webhook_input = QLineEdit()
        self.webhook_input.setPlaceholderText("Entrer webhook Discord")

        self.build_btn = QPushButton("Build script")

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        layout.addWidget(QLabel("Webhook Discord"))
        layout.addWidget(self.webhook_input)
        layout.addWidget(self.build_btn)
        layout.addWidget(self.log)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.build_btn.clicked.connect(self.build_script)

    def build_script(self):

        webhook = self.webhook_input.text().strip()

        if not webhook:
            self.log.append("Webhook manquant")
            return

        file_path, _ = QFileDialog.getOpenFileName(self, "Choisir script", "", "Python Files (*.py)")
        if not file_path:
            return

        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        code = code.replace("WEBHOOK_URL_PLACEHOLDER", webhook)

        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        output = os.path.join(desktop, "built_script.py")

        with open(output, "w", encoding="utf-8") as f:
            f.write(code)

        self.log.append("Script buildé avec webhook")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
