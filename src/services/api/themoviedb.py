import requests


class TheMovieDatabaseApi:

    def __init__(
        self,
        api_key: str,
        url: str = "https://api.themoviedb.org/",
        version: int = 3,
        language: str = 'ru-Ru',
    ) -> None:
        self.url = f'{url}{version}'
        self.api_key = api_key
        self.language = language
