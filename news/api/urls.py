from django.urls import path

from news.api.views import NewsViewSet

urlpatterns = [
    path('index', NewsViewSet.as_view()),
]
