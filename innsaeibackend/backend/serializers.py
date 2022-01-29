from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import AppUser, event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AppUser
        fields = ['user', 'role', 'description', 'achievements', 'github', 'linkedin', 'profile_image']

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = event
        fields = '__all__'
