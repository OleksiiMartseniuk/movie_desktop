import pytest

from src.utils import validation, massage


@pytest.mark.parametrize(
    'password',
    ['qwerty', '123qwe', '@#ERdsdff', 'lkGH^%']
)
def test_password(password):
    result = validation.password_valid(password)
    assert result is None


@pytest.mark.parametrize(
    'password',
    ['qty', 'фывфвфыв', 'assdasdasdasdasdasdasd']
)
def test_password_not_valid(password):
    result = validation.password_valid(password)
    assert result == massage.ERROR_PASSWORD_VALID


def test_password_confirm_valid():
    result = validation.password_confirm_valid('test1', 'test1')
    assert result is None


def test_password_confirm_valid_not_valid():
    result = validation.password_confirm_valid('test1', 'test')
    assert result == massage.ERROR_CONFIRM_PASSWORD


@pytest.mark.parametrize(
    'username',
    ['test', 'MainTets', 'Joni', 'Alex']
)
def test_username(username):
    result = validation.username_valid(username)
    assert result is None


@pytest.mark.parametrize(
    'username',
    ['test1', '$MainTets', '_Joni', 'Тест']
)
def test_username_not_valid(username):
    result = validation.username_valid(username)
    assert result == massage.ERROR_USERNAME_VALID
