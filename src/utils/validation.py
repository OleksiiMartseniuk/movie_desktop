import re

from typing import Optional

from . import massage


def password_valid(password: str) -> Optional[str]:
    """Валидация пароля
    -------------------
    * прописные буквы [A-Z]
    * строчные буквы [a-z]
    * числа [0-9]
    * любой из специальных символов [@#$%^&+=]
    * количество символов [6-20]
    """
    if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{6,20}', password):
        return massage.ERROR_PASSWORD_VALID


def password_confirm_valid(
    password: str,
    confirm_password: str
) -> Optional[str]:
    """Подтверждения пароля"""
    if not password == confirm_password:
        return massage.ERROR_CONFIRM_PASSWORD


def username_valid(username: str) -> Optional[str]:
    """Валидация имя_пользователя
    -----------------------------
    * прописные буквы [A-Z]
    * строчные буквы [a-z]
    * количество символов [4-20]
    """
    if not re.fullmatch(r'[A-Za-z]{4,20}', username):
        return massage.ERROR_USERNAME_VALID
