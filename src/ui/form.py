import logging

from typing import Optional

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
        # Переход на редактирования профиля
        self.ui.button_user.clicked.connect(self.profile_user)

    def show(self) -> None:
        user = self.get_user()
        if not user:
            self.close()
        self.ui.button_user.setText(user.username.capitalize())

        super().show()

    def profile_user(self) -> None:
        """Профиль пользователя"""
        user = self.get_user()

        self.ui.stackedWidget.setCurrentWidget(self.ui.profile)
        self.ui.lineEdit_username.setText(user.username)

    def get_user(self) -> Optional[user_db.User]:
        """Получения текучего пользователя"""
        user = user_db.get_id(self.user_id)
        if not user:
            logger.error(f'Not user id[{self.user_id}] in database')
        return user
