import json
from http.client import HTTPResponse

from django.http import JsonResponse
from django.views import View
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.request import Request
from rest_framework.views import APIView

from api.models import TestData


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HTTPResponse('hello world')


@permission_classes((permissions.AllowAny,))
class CourseListView(APIView):
    def get(self, request, *args, **kwargs):  # type: (CourseListView, Request, [], {}) -> JsonResponse
        # Get api from url version.
        print(request.version)
        # 獲取版本管理的類
        print(request.versioning_scheme)
        # 反向生成URL
        reverse_url = request.versioning_scheme.reverse('test', request=request)
        print(reverse_url)
        print(request.query_params)

        data = TestData().to_json()
        return JsonResponse(json.loads(data))
