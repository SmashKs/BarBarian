from sqlite3 import IntegrityError

import django
from django.db import models


class News(models.Model):
    author = models.CharField(max_length=64, null=True, blank=True)
    title = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=2, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    url = models.CharField(max_length=512, null=True, blank=True)
    urlToImage = models.CharField(max_length=512, null=True, blank=True)
    published_at = models.DateTimeField()
    content = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'news'
        unique_together = (('id', 'title'),)  # Set two primary keys together.

    def __unicode__(self):  # type: (News) -> str
        return self.title

    # @staticmethod
    # def json_to_object(json_str):  # type: (str) -> News
    #     def __json_object_hook(d):  # type: (dict) -> tuple
    #         return namedtuple('new_obj', d.keys())(*d.values())
    #
    #     def __json2obj(data):  # type: (str) -> Any
    #         return json.loads(data, object_hook=__json_object_hook)
    #
    #     obj = __json2obj(json_str)
    #
    #     return News(author=obj.author,
    #                 title=obj.title,
    #                 description=obj.description,
    #                 url=obj.url,
    #                 urlToImage=obj.urlToImage,
    #                 published_at=obj.publishedAt,
    #                 content=obj.content)

    @staticmethod
    def parse_dict(dict_news, country):  # type: (dict, str) -> List[News]
        # The data we don't need.
        _ = dict_news['status']
        _ = dict_news['totalResults']
        # Only articles content we need!
        articles = dict_news['articles']

        return list(map(lambda news: News(author=news['author'],
                                          title=news['title'],
                                          country=country,
                                          description=news['description'],
                                          url=news['url'],
                                          urlToImage=news['urlToImage'],
                                          published_at=news['publishedAt'],
                                          content=news['content']),
                        articles))

    @staticmethod
    def persist_to_database(list_news):  # type: (List[News]) -> None
        for news in list_news:
            try:
                print(f'persist the title of the data: {news.title}, author: {news.author}')
                news.save()
            except IntegrityError as err:
                print(f'Something wrong happened!\nerror: {err}')
            except django.db.utils.IntegrityError as integrity_err:
                print(f'Something internal wrong happened!\nerror: {integrity_err}')

    @staticmethod
    def get_all():  # type: () -> QuerySet
        return News.objects.all()


class Sources(models.Model):
    s_id = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'news_sources'

    def __unicode__(self):  # type: (Sources) -> str
        return f'{self.s_id} {self.name}'
