from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ('author',
                  'title',
                  'country',
                  'description',
                  'url',
                  'urlToImage',
                  'published_at',
                  'content',
                  'created_at',
                  'updated_at')
