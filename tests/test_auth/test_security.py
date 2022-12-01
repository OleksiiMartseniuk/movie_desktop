from datetime import datetime

from src.services.auth import security
from src.services.db.user import User
from src.utils import massage


def get_user(
    id='63886e7368252b59c4265e5e',
    username='test',
    password='password',
    data_join=datetime(2022, 12, 1, 11, 5, 55, 682000),
    active=True,
    viewed=[],
    favorites=[]
) -> User:
    return User(
        _id=id,
        username=username,
        password_hash=security.get_password_hash(password),
        data_join=data_join,
        active=active,
        viewed=viewed,
        favorites=favorites
    )


def test_current_user():
    user = get_user()
    result = security.current_user(user)
    assert result is user


def test__current_user():
    user = get_user(active=False)
    result = security.current_user(user)
    assert isinstance(result, str)
    assert result == massage.ERROR_USER_ACTION
