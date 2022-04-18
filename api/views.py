from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers
from django.contrib.auth import get_user_model
from voice.models import Voice


User = get_user_model()


class UserAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": serializer.data,
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class LoginAPIView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer
    permission_class = (AllowAny, )
    authentication_classes = []


class VoiceAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.VoiceSerializer
    queryset = Voice.objects.all()

    def get(self, request, *args, **kwargs):
        qs = Voice.objects.all().filter(user=request.user).order_by('-created_date')
        serializer = serializers.VoiceSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = serializers.VoiceSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.VoiceSerializer
    queryset = Voice.objects.all()
    lookup_field = 'uuid'


class PasswordChangeAPIView(APIView):
    serializer_class = serializers.PasswordChangeSerializer
    model = User

    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                return Response(
                    "Password updated successfully",
                    status.HTTP_200_OK
                )
            return Response(
                "Password wrong",
                status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
