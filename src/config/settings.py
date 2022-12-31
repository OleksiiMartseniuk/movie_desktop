import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

ICON_DIR = BASE_DIR.joinpath('icon')

MONGO_DB_URL = os.getenv('MONGO_DB_URL')

KEY_THEMOVIEDB = os.getenv('KEY_THEMOVIEDB')

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": ("%(asctime)s\t%(name)s:%(module)s[%"
                       "(lineno)d]:%(levelname)s %(message)s")
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "level": "INFO",
            "filename": "info.log",
            "mode": "a",
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO"
        },
        "full": {
            "handlers": ["console", "file"],
            "level": "INFO"
        }
    }
}
