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

    def get(self, url: str, **kwargs):
        try:
            response = requests.get(url=url, **kwargs)
            if response.status_code == 200:
                response.json()
            else:
                # TODO logger
                return None
        except requests.exceptions.ConnectionError:
            # TODO logger
            return None
