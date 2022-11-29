import inspect

from typing import List, Optional
from dataclasses import dataclass

from datetime import datetime
from bson.objectid import ObjectId

from .database import db


@dataclass
class User:
    """Пользователь"""
    _id: str
    username: str
    password_hash: str
    data_join: datetime
    active: bool
    viewed: List[int]
    favorites: List[int]

    @classmethod
    def format_dict(cls, params: dict):
        return cls(**{
            k: v for k, v in params.items()
            if k in inspect.signature(cls).parameters
        })


def create(username: str, password_hash: str, active: bool = True) -> None:
    """Создания пользователя"""
    data = {
        'username': username,
        'password_hash': password_hash,
        'data_join': datetime.now(),
        'active': active,
        'viewed': [],
        'favorites': []
    }
    db.user.insert_one(data)


def get_id(user_id: str) -> Optional[User]:
    """Получения пользователя по id"""
    user = db.user.find_one({'_id': ObjectId(user_id)})
    if not user:
        return None
    return User.format_dict(user)


def get(**kwargs) -> Optional[User]:
    """Получения пользователя"""
    user = db.user.find_one(kwargs)
    if not user:
        return None
    return User.format_dict(user)
