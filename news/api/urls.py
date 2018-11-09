from django.urls import path

from news.api.views import CourseListView

urlpatterns = [
    path('index', CourseListView.as_view()),
]
