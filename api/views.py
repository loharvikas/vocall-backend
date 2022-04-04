from operator import ge
from rest_framework import generics
from rest_framework.permissions import AllowAny
from . import serializers
from django.contrib.auth import get_user_model
from workspace.models import Workspace
from voice.models import Voice


User = get_user_model()


class UserAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class WorkspaceAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.WorkspaceSerializer
    queryset = Workspace.objects.all()


class VoiceAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.VoiceSerializer
    queryset = Voice.objects.all()


class VoiceDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.VoiceSerializer
    queryset = Voice.objects.all()
    lookup_field = 'uuid'
