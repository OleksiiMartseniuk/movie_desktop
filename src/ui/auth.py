from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout
from PySide6 import QtCore

from src.utils import validation
from src.services.auth import security

from .ui_auth import Ui_Auth


class Auth(QMainWindow):
    """Форма аутентификации"""

    def __init__(self) -> None:
        super(Auth, self).__init__()
        self.ui = Ui_Auth()
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
                self.show_massage_error(action, layout)
            else:
                # TODO Переход на основное окно
                print(user)

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
                self.show_massage_error(action, layout)
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
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

        error_massage = validation.form_valid(
            username, password, confirm_password
        )
        if error_massage:
            self.error_massage[action] = error_massage

        if self.error_massage[action]:
            # Добавления ошибок в форму
            self.show_massage_error(action, layout)
            return False
        return True

    def show_massage_error(self, action: str, layout: QVBoxLayout) -> None:
        """Отображения ошибок в форме"""
        for error in self.error_massage[action]:
            layout.addWidget(self.create_message(error, 'red'))

    def create_message(self, text: str, color: str) -> QLabel:
        """Создания объекта label"""
        label = QLabel(text)
        label.setWordWrap(True)
        label.setStyleSheet(f"color: {color};")
        return label
