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

    def _error(self, type: str) -> bool:
        """Проверка параметра type"""
        if type != 'movie' and type != 'tv':
            logger.error('Invalid parameter [type]')
            return True
        return False

    def get_details(self, id: int, type: str) -> Optional[dict]:
        """Получить первичную информацию movie/TV

        Parameters
        ----------
        id : int
            ID movie/TV
        type : str
            ['movie', 'tv']
        """
        if self._error(type=type):
            return None

        url = f'{self.url}/{type}/{id}'
        params = self.__set_params()
        return self.get(url=url, params=params)

    def get_popular(self, type: str, page: int = 1) -> Optional[dict]:
        """Получите список текущих популярных movie/tv на TMDB.
        Этот список обновляется ежедневно

        Parameters:
        ----------
        type : str
            ['movie', 'tv']
        """
        if self._error(type=type):
            return None

        url = f'{self.url}/{type}/popular'
        params = self.__set_params(page=page)
        return self.get(url=url, params=params)

    def get_top_rated(self, type: str, page: int = 1) -> Optional[dict]:
        """Получите movie/tv с самым высоким рейтингом на TMDB.

        Parameters:
        ----------
        type : str
            ['movie', 'tv']
        """
        if self._error(type=type):
            return None

        url = f'{self.url}/{type}/top_rated'
        params = self.__set_params(page=page)
        return self.get(url=url, params=params)

    def get_recommendations(
        self,
        id: int,
        type: str,
        page: int = 1
    ) -> Optional[dict]:
        """Получить список рекомендуемых movie/tv для movie/tv.

        Parameters:
        ----------
        type : str
            ['movie', 'tv']
        """
        if self._error(type=type):
            return None

        url = f'{self.url}/{type}/{id}/recommendations'
        params = self.__set_params(page=page)
        return self.get(url=url, params=params)

    def get_trending(
        self,
        media_type: str,
        time_window: str,
        page: int = 1
    ) -> Optional[dict]:
        """Получите ежедневные или еженедельные трендовые товары.

        Parameters:
        ----------
        media_type : str
            >>> [all] Включите все фильмы, телешоу и людей в результаты в
                виде глобального списка трендов.
            >>> [movie] Показать популярные фильмы в результатах.
            >>> [tv] Показать популярные телешоу в результатах.
            >>> [person] Покажите популярных людей в результатах.
        time_window : str
            >>> [day] Просмотрите список трендов дня.
            >>> [week] Просмотрите список трендов на неделю.
        """
        list_media_type = ['all', 'movie', 'tv', 'person']
        list_time_window = ['day', 'week']

        if media_type not in list_media_type:
            logger.error('Invalid parameter [media_type]')
            return None

        if time_window not in list_time_window:
            logger.error('Invalid parameter [time_window]')
            return None

        url = f'{self.url}/trending/{media_type}/{time_window}'
        params = self.__set_params(page=page)
        return self.get(url=url, params=params)

    def get_person_details(self, id: int) -> Optional[dict]:
        """Получить данные основного лица по идентификатору."""
        url = f'{self.url}/person/{id}'
        params = self.__set_params()
        return self.get(url=url, params=params)

    def get_person_popular(self, page: int = 1) -> Optional[dict]:
        """Получить список популярных людей на TMDB"""
        url = f'{self.url}/person/popular'
        params = self.__set_params(page=page)
        return self.get(url=url, params=params)

    def search_multi(self, query: str, page: int = 1) -> Optional[dict]:
        """Поиск нескольких моделей в одном запросе."""
        url = f'{self.url}/search/multi'
        params = self.__set_params(query=query, page=page)
        return self.get(url=url, params=params)
