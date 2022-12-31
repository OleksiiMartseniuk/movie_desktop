import logging

from typing import Optional

from PySide6.QtWidgets import QWidget

from src.services.db import user as user_db
from src.services.auth import security

from src.utils import validation, ui

from .ui_form import Ui_Form


logger = logging.getLogger('root')


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
        # Обновления профиля
        self.ui.pushButton_save.clicked.connect(self.update_profile)

    def show(self) -> None:
        user = self.get_user()
        if not user:
            self.close()
        self.ui.button_user.setText(user.username.capitalize())

        super().show()

    def get_user(self) -> Optional[user_db.User]:
        """Получения текучего пользователя"""
        user = user_db.get_id(self.user_id)
        if not user:
            logger.error(f'Not user id[{self.user_id}] in database')
        return user

    def profile_user(self) -> None:
        """Профиль пользователя"""
        user = self.get_user()

        self.ui.stackedWidget.setCurrentWidget(self.ui.profile)
        self.ui.lineEdit_username.setPlaceholderText(user.username)

    def update_profile(self) -> None:
        """Обновления данных пользователя"""
        user = self.get_user()

        layout = self.ui.verticalLayout_5
        username = self.ui.lineEdit_username.text()
        new_password = self.ui.lineEdit_password.text()
        confirm_password = self.ui.lineEdit_confirm_password.text()

        # Очистка ошибок с формы
        ui.clear_massage(layout)

        actions, error_list = validation.form_update_valid(
            new_username=username,
            new_password=new_password,
            confirm_password=confirm_password,
            hash_password=user.password_hash,
            current_username=user.username
        )

        if error_list:
            ui.show_massage_error(error_list, layout)
        else:
            for action in actions:
                if action == 'username':
                    user_db.update(self.user_id, username=username)
                    logger.info('User %s changed username', self.user_id)
                if action == 'password':
                    has_password = security.get_password_hash(new_password)
                    user_db.update(self.user_id, password_hash=has_password)
                    logger.info('User %s changed password', self.user_id)
            user = self.get_user()
            # Очистка полей
            self.ui.lineEdit_username.setText('')
            self.ui.lineEdit_password.setText('')
            self.ui.lineEdit_confirm_password.setText('')
            # Новые данные пользователя
            self.ui.lineEdit_username.setPlaceholderText(user.username)
            self.ui.button_user.setText(user.username.capitalize())
            # Сообщения об успехе регистрации
            message_info = ui.create_message(
                'Обновления выполнено успешно', 'green'
            )
            layout.addWidget(message_info)
