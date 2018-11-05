from django.contrib.auth.models import Group, User
from rest_framework import viewsets


# Serializers define the API representation.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    print("hello world")
    # serializer_class = UserSerializer


# ViewSets define the view behavior.
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    # serializer_class = GroupSerializer
