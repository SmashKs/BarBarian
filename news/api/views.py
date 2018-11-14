import uuid
from typing import Dict

from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from news.models import News, Subscriber
from news.serializers import NewsSerializer, SubscriberSerializer


@permission_classes((permissions.AllowAny,))
class NewsViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = News.objects.all().order_by('-created_at')  # Reverse the data, the newest news will show in order.
    serializer_class = NewsSerializer


@permission_classes((permissions.AllowAny,))
class SubscriberViewSet(CreateModelMixin,
                        UpdateModelMixin,
                        DestroyModelMixin,
                        GenericViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        request.data['token'] = uuid.uuid4().hex  # Auto generate token.

        res = super(SubscriberViewSet, self).create(request, *args, **kwargs)
        self.__modify_response_json(res.data)

        return res

    def update(self, request, *args, **kwargs):
        request.data['token'] = kwargs['pk']  # Add the token from pk field into request dict.

        res = super(SubscriberViewSet, self).update(request, *args, **kwargs)
        self.__modify_response_json(res.data)

        return res

    def __modify_response_json(self, data):  # type: (SubscriberViewSet, Dict[str, str]) -> None
        """
        Remove the redundant fields from the data.

        :param data: response dict data.
        """
        for k, _ in dict(data).items():
            if k not in ['token', 'firebase_token']:
                data.pop(k)
