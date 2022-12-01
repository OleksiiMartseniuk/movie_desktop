from unittest import mock
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


@mock.patch('src.services.auth.security.user_db.get')
def test_registration_user_exist(mock_get_user):
    mock_get_user.return_value = get_user()
    result = security.registration('test', 'password')
    assert isinstance(result, str)
    assert result == massage.ERROR_USER_EXIST


@mock.patch('src.services.auth.security.user_db.create')
@mock.patch('src.services.auth.security.user_db.get')
def test_registration(mock_get_user, mock_create_user):
    mock_get_user.return_value = None
    security.registration('test', 'password')
    mock_create_user.assert_called_once()


@mock.patch('src.services.auth.security.current_user')
@mock.patch('src.services.auth.security.user_db.get')
def test_login(mock_get_user, mock_current_user):
    mock_get_user.return_value = get_user()
    security.login('test', 'password')
    mock_current_user.assert_called_once()


@mock.patch('src.services.auth.security.user_db.get')
def test_login_error_password(mock_get_user):
    mock_get_user.return_value = get_user()
    result = security.login('test', 'password1')
    assert isinstance(result, str)
    assert result == massage.ERROR_PASSWORD


@mock.patch('src.services.auth.security.user_db.get')
def test_login_not_user_exist(mock_get_user):
    mock_get_user.return_value = None
    result = security.login('test', 'password')
    assert isinstance(result, str)
    assert result == massage.ERROR_USER_NOT_EXIST
