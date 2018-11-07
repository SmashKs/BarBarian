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
    def get_all():  # type: () -> QuerySet
        return News.objects.all()


class Sources(models.Model):
    s_id = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)

    def __unicode__(self):  # type: (Sources) -> str
        return f'{self.s_id} {self.name}'
