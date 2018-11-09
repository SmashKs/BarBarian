# Create your views here.

from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet

from news.models import News
from news.serializers import NewsSerializer


@permission_classes((permissions.AllowAny,))
class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
