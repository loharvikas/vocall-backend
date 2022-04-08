from operator import ge
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from . import serializers
from django.contrib.auth import get_user_model
from voice.models import Voice


User = get_user_model()


class UserAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class VoiceAPIView(generics.ListCreateAPIView):
    premission_clasees = (AllowAny, )
    serializer_class = serializers.VoiceSerializer
    queryset = Voice.objects.all()

    def post(self, request, *args, **kwargs):
        print(request.data, request.FILES)
        serializer = serializers.VoiceSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoiceDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.VoiceSerializer
    queryset = Voice.objects.all()
    lookup_field = 'uuid'
