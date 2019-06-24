# from django.contrib.auth.models import User, Group#, model
# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


from .models import Captures
from rest_framework_mongoengine import serializers


class CaptureSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Captures
        fields = ('label', 'description')#, 'inputs')
