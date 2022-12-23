from email.mime import image
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from email import message
from .models import AppUser, contactus, councilMembers, developers, editorials, event, events2



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']



class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AppUser
        fields = ['user', 'role', 'github', 'linkedin', 'profile_image','phone_number','isMember']

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data



class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = event
        fields = '__all__'



class EventSerializer_2(serializers.ModelSerializer):
   
    class Meta:
        model = events2
        fields = '__all__'



class ContactSerailizer(serializers.Serializer):

    name = serializers.CharField(min_length=1)
    email = serializers.CharField(max_length=254,allow_blank=False) 
    message = serializers.CharField(min_length=1, max_length=500 )
    phoneNumber= serializers.CharField( max_length=15)

    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        return contactus.objects.create(**validated_data)



class EditorialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = editorials
        fields = '__all__'



class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = developers
        fields = '__all__'



class Councilserializer(serializers.ModelSerializer):
    
    class Meta:
        model = councilMembers
        fields = '__all__'

