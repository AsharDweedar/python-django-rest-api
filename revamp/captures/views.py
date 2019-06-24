# from django.shortcuts import render
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from captures.serializers import UserSerializer, GroupSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


from captures.models import Captures
from captures.serializers import CaptureSerializer
# from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
# from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework_mongoengine import viewsets as meviewsets
from django.shortcuts import render


# class CapturesViewSet(MongoModelViewSet):
class CapturesViewSet(meviewsets.ModelViewSet):
    model = Captures
    lookup_field = 'id'
    queryset = Captures.objects.all()
    serializer_class = CaptureSerializer
    # def get_queryset(self):
    #     return Captures.objects.all()
