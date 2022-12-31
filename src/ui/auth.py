from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6 import QtCore

from src.utils import validation, ui
from src.services.auth import security

from .ui_auth import Ui_Auth
from .form import Form


class Auth(QWidget):
    """Форма аутентификации"""

    def __init__(self, ui_form: Form) -> None:
        super(Auth, self).__init__()
        self.ui = Ui_Auth()
        self.ui_form = ui_form
        self.ui.setupUi(self)
        # Список сообщений о ошибке
        self.error_massage = {'sing_in': [], 'sing_up': []}
        # Убрать рамку
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Добавить сигнал кнопки
        self.ui.sing_in.clicked.connect(self.sing_in)
        self.ui.sing_up.clicked.connect(self.sing_up)
        # Добавления события при нажатии (Label)
        self.ui.exit.mousePressEvent = self.exit

    def sing_in(self) -> None:
        """Логин"""
        action = 'sing_in'
        layout = self.ui.verticalLayout_2
        username = self.ui.username_1.text()
        password = self.ui.password_1.text()
        # Валидация формы
        if self.is_validation_form(action, layout, username, password):
            # Авторизация пользователя
            user = security.login(username, password)
            if isinstance(user, str):
                self.error_massage[action].append(user)
                ui.show_massage_error(self.error_massage[action], layout)
            else:
                self.ui_form.user_id = user._id
                self.ui_form.show()
                self.close()

    def sing_up(self) -> None:
        """Регистрация"""
        action = 'sing_up'
        layout = self.ui.verticalLayout
        username = self.ui.username_2.text()
        password = self.ui.password_2.text()
        confirm_password = self.ui.confirm_password.text()
        # Валидация формы
        if self.is_validation_form(
            action, layout, username, password, confirm_password
        ):
            # Регистрация пользователя
            message_error = security.registration(username, password)
            if message_error:
                self.error_massage[action].append(message_error)
                ui.show_massage_error(self.error_massage[action], layout)
            else:
                # Сообщения об успехе регистрации
                message_info = self.create_message(
                    f'Пользователь {username} зарегистрирован', 'green'
                )
                layout.addWidget(message_info)
            # Очистка полей
            self.ui.username_2.setText('')
            self.ui.password_2.setText('')
            self.ui.confirm_password.setText('')

    def exit(self, event) -> None:
        """Выход"""
        self.close()

    def is_validation_form(
        self,
        action: str,
        layout: QVBoxLayout,
        username: str,
        password: str,
        confirm_password: str = None
    ) -> bool:
        """Валидация формы"""
        # Очистка списка ошибок
        self.error_massage[action].clear()
        # Очистка ошибок с формы
        ui.clear_massage(layout)

        error_massage = validation.form_valid(
            username, password, confirm_password
        )
        if error_massage:
            self.error_massage[action] = error_massage

        if self.error_massage[action]:
            # Добавления ошибок в форму
            ui.show_massage_error(self.error_massage[action], layout)
            return False
        return True
