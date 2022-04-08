from rest_framework import serializers
from django.contrib.auth import get_user_model

from voice.models import Voice

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False, write_only=True)
    full_name = serializers.CharField(required=False, max_length=255)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'full_name',
            'password',
            'is_active',
            'date_joined',
            'last_modified_date'
        ]


class VoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voice
        fields = '__all__'
