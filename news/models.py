import logging
from sqlite3 import IntegrityError
from typing import List

import django
from django.db import models
from django.db.models import QuerySet

from log.logger import Logger


class News(models.Model):
    author = models.CharField(max_length=64, null=True, blank=True)
    title = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=2, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    urlToImage = models.CharField(max_length=256, null=True, blank=True)
    published_at = models.DateTimeField()
    content = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'newses'
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
    def persist_to_database(list_news):  # type: (List[News]) -> List[News]
        new_list = list_news[:]  # type: List[News]
        Logger.create_log_file(Logger.get_today())  # Create new log for today.

        for news in list_news:
            try:
                news.save()

                info_msg = f'persist the title of the data: {news.title}, author: {news.author}'
                logging.info(info_msg)
            except (IntegrityError, django.db.utils.IntegrityError) as err:
                new_list.remove(news)  # The news have already been in the DB then remove it.

                err_msg = f'data: {news.title} <- {err}'
                logging.error(err_msg)

        return new_list

    @staticmethod
    def get_all():  # type: () -> QuerySet
        return News.objects.all()


class Source(models.Model):
    s_id = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'news_sources'

    def __unicode__(self):  # type: (Source) -> str
        return f'{self.s_id} {self.name}'


class Subscriber(models.Model):
    token = models.CharField(max_length=256, primary_key=True, null=False)
    firebase_token = models.CharField(max_length=256, unique=True)
    keywords = models.CharField(max_length=1024, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subscribers'

    @staticmethod
    def get_all():  # type: () -> QuerySet
        return Subscriber.objects.all()

    @staticmethod
    def get_all_with_keywords():  # type: () -> List[Subscriber]
        all_data = Subscriber.get_all()[:]

        # Separate the keywords to a list.
        for data in all_data:  # type: Subscriber
            data.list_keyword = data.keywords.split(',')

        return all_data
