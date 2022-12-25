import sys

from PySide6.QtWidgets import QApplication

from src.ui.auth import Auth
from src.ui.form import Form


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    auth = Auth(ui_form=form)
    auth.show()

    sys.exit(app.exec())
