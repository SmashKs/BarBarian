import json
from collections import namedtuple

from django.db import models
from django.db.models import QuerySet


class News(models.Model):
    author = models.CharField(max_length=64, null=True, blank=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    country = models.CharField(max_length=2, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    url = models.CharField(max_length=512, null=True, blank=True)
    urlToImage = models.CharField(max_length=512, null=True, blank=True)
    published_at = models.DateTimeField()
    content = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):  # type: (News) -> str
        return self.title

    @staticmethod
    def json_to_object(json_str):  # type: (str) -> News
        def __json_object_hook(d):  # type: (dict) -> tuple
            return namedtuple('new_obj', d.keys())(*d.values())

        def __json2obj(data):  # type: (str) -> Any
            return json.loads(data, object_hook=__json_object_hook)

        obj = __json2obj(json_str)

        return News(author=obj.author,
                    title=obj.title,
                    description=obj.description,
                    url=obj.url,
                    urlToImage=obj.urlToImage,
                    published_at=obj.publishedAt,
                    content=obj.content)

    @staticmethod
    def get_all():  # type: () -> QuerySet
        return News.objects.all()


class Sources(models.Model):
    s_id = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)

    def __unicode__(self):  # type: (Sources) -> str
        return f'{self.s_id} {self.name}'
