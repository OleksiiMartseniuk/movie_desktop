from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Сопоставления хеш-пароля с паролем"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    """Получить хеш-пароля"""
    return pwd_context.hash(password)
