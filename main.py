import sys
import logging.config

from PySide6.QtWidgets import QApplication

from src.ui.auth import Auth
from src.ui.form import Form

from src.config.settings import LOGGING_CONFIG


def main():
    logging.config.dictConfig(LOGGING_CONFIG)

    app = QApplication(sys.argv)

    form = Form()
    auth = Auth(ui_form=form)
    auth.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
