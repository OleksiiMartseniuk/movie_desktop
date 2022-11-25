import os

from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
ICON_DIR = BASE_DIR.joinpath('icon')

MONGO_DB_URL = os.getenv('MONGO_DB_URL')
