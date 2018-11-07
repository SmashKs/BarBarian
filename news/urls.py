from django.urls import include, path

urlpatterns = [
    path('', include('news.api.urls'))
]
