from rest_framework import mixins, permissions
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from news.models import News
from news.serializers import NewsSerializer, SubscriberSerializer


@permission_classes((permissions.AllowAny,))
class NewsViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def list(self, request, *args, **kwargs):
        response = super(NewsViewSet, self).list(request, args, kwargs)
        # TODO(jieyi): 2018-11-11 Add some extra operations.
        return response


@permission_classes((permissions.AllowAny,))
class SubscriberViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):
    serializer_class = SubscriberSerializer
