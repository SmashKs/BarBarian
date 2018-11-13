from rest_framework import serializers

from news.models import News, Subscriber


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


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        # fields = '__all__'
        fields = ('token',
                  'firebase_token',
                  'keywords',
                  'created_at',
                  'updated_at')
