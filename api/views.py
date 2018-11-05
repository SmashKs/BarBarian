from django.http import HttpResponse, JsonResponse
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

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
from rest_framework.views import APIView


class Course:
    def __init__(self):
        self.name = ''
        self.course = ''


class CourseListView(APIView):
    def get(self, request, format=None):
        # json_data = serializers.serialize('json', Course())
        # json_data = json.loads(json_data)
        return JsonResponse('{"hello": 123,"name": "jieyi"}', safe=False)
        return HttpResponse('Hello, World!')
