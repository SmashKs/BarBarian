from newsapi import NewsApiClient

from external import NEWS_API_KEY


class Fetcher:
    def __init__(self):
        self.__news_api = NewsApiClient(NEWS_API_KEY)

    def top_headline(self, country='jp'):  # type: (Fetcher, str) -> dict
        """
        Get the newest top of the news.
        :param country: str
        :return: dict
        """
        return self.__news_api.get_top_headlines(country=country, page_size=60)
