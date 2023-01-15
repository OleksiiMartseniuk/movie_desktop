import requests

from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton
from PySide6.QtGui import QFont, QPixmap, QImage
from PySide6.QtCore import QSize, Qt


def create_message(text: str, color: str) -> QLabel:
    """Создания объекта label"""
    label = QLabel(text)
    label.setWordWrap(True)
    label.setStyleSheet(f"color: {color};")
    return label


def show_massage_error(error_massage: list, layout: QVBoxLayout) -> None:
    """Отображения ошибок в форме"""
    for error in error_massage:
        layout.addWidget(create_message(error, 'red'))


def clear_massage(layout: QVBoxLayout):
    """Очистка сообщений с формы"""
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)


def cart(id: int, title: str, image_url: str, data: str) -> QWidget:
    """Cart"""
    cart = QWidget()
    layout = QVBoxLayout(cart)

    cart_image = QLabel(cart)
    cart_image.setMinimumSize(QSize(150, 225))
    cart_image.setMaximumSize(QSize(150, 225))
    cart_image.setStyleSheet(u"border-radius: 15px;""")

    image = QImage()
    image.loadFromData(requests.get(image_url).content)
    cart_image.setPixmap(QPixmap(image))

    layout.addWidget(cart_image)

    font2 = QFont()
    font2.setPointSize(12)
    font2.setBold(True)
    cart_title = QPushButton(cart)
    cart_title.setText(title)
    cart_title.setMaximumSize(QSize(150, 16777215))
    cart_title.setFont(font2)

    layout.addWidget(cart_title)

    cart_date = QLabel(cart)
    cart_date.setText(data)
    cart_date.setMaximumSize(QSize(150, 16777215))
    font = QFont()
    font.setPointSize(10)
    font.setBold(False)
    cart_date.setFont(font)
    cart_date.setAlignment(Qt.AlignCenter)

    layout.addWidget(cart_date)
    return cart
