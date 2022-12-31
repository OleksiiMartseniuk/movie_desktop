import re

from typing import Optional, List, Tuple, Union

from src.services.auth.security import verify_password

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


def form_valid(
    username: str,
    password: str,
    confirm_password: str = None
) -> Union[List[str], List]:
    """Валидация формы"""
    error_message_list = []

    username_error = username_valid(username)
    password_error = password_valid(password)

    if username_error:
        error_message_list.append(username_error)

    if password_error:
        error_message_list.append(password_error)

    if isinstance(confirm_password, str):
        confirm_password_error = password_confirm_valid(
            password, confirm_password
        )
        if confirm_password_error:
            error_message_list.append(confirm_password_error)
    return error_message_list


def form_update_valid(
    new_username: str,
    new_password: str,
    confirm_password: str,
    hash_password: str,
    current_username: str
) -> Tuple[list, list]:
    """Валидация формы обновления профиля пользователя
    --------------------------------------
    >>> 'action' Активные поля для изменений
    >>> 'error_message_list' Список ошибок
    """
    error_message_list = []
    # поля для изменений ['username', 'password']
    action = []

    if new_username:
        action.append('username')
        username_error = username_valid(new_username)
        if username_error:
            error_message_list.append(username_error)
        if new_username == current_username:
            error_message_list.append(massage.ERROR_NEW_USERNAME)

    if ((new_password and not confirm_password)
            or (not new_password and confirm_password)):
        error_message_list.append(massage.ERROR_PASSWORD_AND_CONFIRM)

    if new_password and confirm_password:
        action.append('password')
        password_error = password_valid(new_password)
        if password_error:
            error_message_list.append(password_error)

        confirm_password_error = password_confirm_valid(
            new_password, confirm_password
        )
        if confirm_password_error:
            error_message_list.append(confirm_password_error)
        if verify_password(new_password, hash_password):
            error_message_list.append(massage.ERROR_NEW_PASSWORD)

    if len(action) < 1:
        error_message_list.append(massage.ERROR_ACTION)

    return action, error_message_list
