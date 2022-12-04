import requests
import logging

from typing import Optional


logger = logging.getLogger(__name__)


class TheMovieDatabaseApi:

    def __init__(
        self,
        api_key: str,
        url: str = "https://api.themoviedb.org/",
        version: int = 3,
        language: str = 'ru-Ru',
    ) -> None:
        self.url = f'{url}{version}'
        self.__api_key = api_key
        self.language = language

    def get(self, url: str, **kwargs):
        try:
            response = requests.get(url=url, **kwargs)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(
                    f'status code [{response.status_code}] url [{url}]'
                )
                return None
        except requests.exceptions.ConnectionError:
            logger.error(f'Not connect net. url [{url}]')
            return None

    def __set_params(self, **kwargs) -> dict:
        params = {
            'api_key': self.__api_key,
            'language': self.language,
        }
        if kwargs:
            # Параметры со значением None игнорируются
            params_add = {key: value for key, value in kwargs.items() if value}
            params.update(params_add)
        return params

    def get_details(self, id: int, type: str) -> Optional[dict]:
        """Получить первичную информацию movie/TV

        Parameters
        ----------
        id : int
            ID movie/TV
        type : str
            ['movie', 'tv']
        """
        if type != 'movie' and type != 'tv':
            logger.error('Invalid parameter [type]')
            return None

        url = f'{self.url}/{type}/{id}'
        params = self.__set_params()
        return self.get(url=url, params=params)
