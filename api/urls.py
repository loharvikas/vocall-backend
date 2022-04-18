from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserAPIView.as_view(), name='view'),
    path('voice/', views.VoiceAPIView.as_view(), name='voice'),
    path('voice/<uuid:uuid>/', views.VoiceDetailAPIView.as_view(), name='voice-detail'),
    path('user/update/', views.UserUpdateAPIView.as_view(),
         name='update-user'),
    path('user/password-change/',
         views.PasswordChangeAPIView.as_view(), name='password-change'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('register/', views.UserAPIView.as_view(), name='register')
]
