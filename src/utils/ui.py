from PySide6.QtWidgets import QVBoxLayout, QLabel


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
