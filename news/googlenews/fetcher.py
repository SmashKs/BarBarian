from newsapi import NewsApiClient

from external import NEWS_API_KEY
from news.models import News


class Fetcher:
    def __init__(self):
        self.__news_api = NewsApiClient(NEWS_API_KEY)

    def top_headline(self, country='tw'):  # type: (Fetcher, str) -> dict
        return self.__news_api.get_top_headlines(country=country, page_size=60)

    @staticmethod
    def to_news_objs(newses):
        status = newses['status']
        total = newses['totalResults']
        articles = newses['articles']

        to_news_list = lambda news: News(author=news['author'],
                                         title=news['title'],
                                         description=news['description'],
                                         url=news['url'],
                                         urlToImage=news['urlToImage'],
                                         published_at=news['publishedAt'],
                                         content=news['content'])
        return list(map(to_news_list, articles))
