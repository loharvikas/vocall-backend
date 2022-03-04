from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserAPIView.as_view(), name='view'),
    path('workspace/', views.WorkspaceAPIView.as_view(), name='workspace'),
    path('voice', views.VoiceAPIView.as_view(), name='voice')
]
