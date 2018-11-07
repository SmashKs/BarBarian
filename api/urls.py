from django.urls import path

from api.views import CourseListView, IndexView

urlpatterns = [
    path('index', IndexView.as_view()),
    path('test', CourseListView.as_view(), name='test'),
]
