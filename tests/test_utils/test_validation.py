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


@pytest.mark.parametrize(
    'username, password, password_confirm, result',
    [
        ('username', 'password', 'password', 0),
        ('username', 'password', None, 0),
        ('username', 'password', 'password', 0),
        ('u', 'password', None, 1),
        ('username', 'p', None, 1),
        ('u', 'p', None, 2),
        ('username', 'password', 'p', 1),
        ('u', 'p', '', 3)
    ]
)
def test_form_valid(
    username,
    password,
    password_confirm,
    result
):
    result_data = validation.form_valid(
        username, password, password_confirm
    )
    assert len(result_data) == result


@pytest.mark.parametrize(
    'new_username, new_password, confirm_password,'\
        ' hash_password, current_username, error_len, action_r',
    [
        ('aadmin',  '', '', '213', 'admin', 0, ['username']),
        (
            '',
            'qwerty',
            'qwerty',
            '$2b$12$I8b79Oi8HEnOhneBRkQ8HOEqdDp34L4lNNx9iH4HSj6K5eDdGDPpy',
            'admin',
            0,
            ['password']
        ),
        (
            'aadmin',
            'qwerty',
            'qwerty',
            '$2b$12$I8b79Oi8HEnOhneBRkQ8HOEqdDp34L4lNNx9iH4HSj6K5eDdGDPpy',
            'admin',
            0,
            ['username', 'password']
        ),
        (
            '',
            'adminadmin',
            'adminadmin',
            '$2b$12$I8b79Oi8HEnOhneBRkQ8HOEqdDp34L4lNNx9iH4HSj6K5eDdGDPpy',
            'admin',
            1,
            ['password']
        ),
        ('', '', '', '213', 'admin', 1, []),
        ('admin',  '', '', '213', 'admin', 1, ['username']),
        ('', 'qwerty', '', '213', '', 2, [])
    ]
)
def test_form_update_valid(
    new_username,
    new_password,
    confirm_password,
    hash_password,
    current_username,
    error_len,
    action_r
):
    action, error_list = validation.form_update_valid(
        new_username,
        new_password,
        confirm_password,
        hash_password,
        current_username
    )
    assert len(error_list) == error_len
    assert action == action_r
