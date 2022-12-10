import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

ICON_DIR = BASE_DIR.joinpath('icon')

MONGO_DB_URL = os.getenv('MONGO_DB_URL')

KEY_THEMOVIEDB = os.getenv('KEY_THEMOVIEDB')
