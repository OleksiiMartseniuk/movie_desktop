import sys

from PySide6.QtWidgets import QApplication

from src.ui.auth import Auth


if __name__ == "__main__":
    app = QApplication(sys.argv)

    auth = Auth()
    auth.show()

    sys.exit(app.exec())
