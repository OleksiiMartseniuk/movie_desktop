from typing import Optional, Union

from passlib.context import CryptContext

from src.services.db import user as user_db
from src.utils import massage


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Сопоставления хеш-пароля с паролем"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    """Получить хеш-пароля"""
    return pwd_context.hash(password)


def get_current_user(user: user_db.User) -> Union[user_db.User, str]:
    """Получить активного пользователя"""
    if user.active:
        return user
    else:
        return massage.ERROR_USER_ACTION


def registration(username: str, password: str) -> Optional[str]:
    """Регистрация пользователя"""
    if user_db.get(username=username):
        return massage.ERROR_USER_EXIST
    return user_db.create(username, get_password_hash(password))


def login(username: str, password: str) -> Union[user_db.User, str]:
    """Авторизация пользователя"""
    user = user_db.get(username=username)
    if user:
        if verify_password(password, user.password_hash):
            return get_current_user(user)
        else:
            return massage.ERROR_PASSWORD
    else:
        return massage.ERROR_USER_NOT_EXIST
