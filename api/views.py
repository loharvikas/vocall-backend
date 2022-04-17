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


# class RegisterAPIView(generics.CreateAPIView):
#     perminssion_classes = (AllowAny)
#     authentication_classes = []
#     serializer_class = serializers.UserSerializer

    # def post(self, request, *arg, **kwargs):
    #     serializer = serializers.RegisterSerializer(
    #         data=request.data
    #     )
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         refresh = RefreshToken.for_user(user)
    #         res = {
    #             "refresh": str(refresh),
    #             "access": str(refresh.access_token),
    #         }
    #         return Response({
    #             "user": serializer.data,
    #             "access": res["access"],
    #             "refresh": refresh["refresh"]
    #         }, status=status.HTTP_201_CREATED)
