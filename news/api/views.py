# Create your views here.
from requests import Response
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ReadOnlyModelViewSet

from news.models import News
from news.serializers import NewsSerializer


@permission_classes((permissions.AllowAny,))
class NewsViewSet(ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    # def list(self, request, **kwargs):
    #     serializer = NewsSerializer(self.queryset, many=True)
    #
    #     return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        news = NewsSerializer(self.queryset, many=True)
        # count = len(news.data)

        return Response({
            'news': news.data,
            # 'count': count
        })
