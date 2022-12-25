import logging

from PySide6.QtWidgets import QWidget

from src.services.db import user as user_db

from .ui_form import Ui_Form


logger = logging.getLogger(__name__)


class Form(QWidget):
    """Main form"""

    def __init__(self, user_id: str = None) -> None:
        super(Form, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # id пользователя
        self.user_id = user_id
        # Добавить сигнал кнопки
        self.ui.button_user.clicked.connect(self.profile_user)

    def show(self) -> None:
        user = user_db.get_id(self.user_id)
        if not user:
            logger.error(f'Not user id[{self.user_id}] in database')
            return
        self.ui.button_user.setText(user.username.capitalize())

        super().show()

    def profile_user(self) -> None:
        self.ui.stackedWidget.setCurrentWidget(self.ui.profile)
