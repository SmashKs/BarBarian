from django.urls import path

from api.views import CourseListView

urlpatterns = [
    path('', CourseListView.as_view(), name='index'),
]
