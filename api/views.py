import json

from django.http import JsonResponse
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
from rest_framework.views import APIView

from api.models import TestData


# # Serializers define the API representation.
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     print("hello world")
#     # serializer_class = UserSerializer
#
#
# # ViewSets define the view behavior.
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     # serializer_class = GroupSerializer


class CourseListView(APIView):
    def get(self, request, format=None):
        # json_data = serializers.serialize('json', Course())
        # json_data = json.loads(json_data)
        data = TestData().to_json()
        return JsonResponse(json.loads(data))
