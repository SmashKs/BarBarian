from rest_framework import routers

from news.api.views import NewsViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'subscriber', )
