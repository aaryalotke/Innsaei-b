from email.mime import image
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from email import message
from .models import AppUser, Component, Initiatives, Remainder, UpcomingWorkshopmodels, contactus, councilMembers, developers, editorials,  events2



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




from django.core import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import validate_password

class UserSerializerNONMEMBER(serializers.ModelSerializer):
    password = serializers.HiddenField(default='innsaei')
    class Meta:
        model = User
        extra_kwargs = {'email': {'required': True, 'allow_blank': False},
                        'first_name': {'required': True, 'allow_blank': False},
                        'last_name': {'required': True, 'allow_blank': False},
                        }
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


    def validate(self, data):
        password = data.get('password')
        errors = dict()
        

        #try:
        #    # validate the password and catch the exception
        #    password_validation.validate_password(password=password, user=User)

        ## the exception raised here is different than serializers.ValidationError
        #except exceptions.ValidationError as e:
        #    errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializerNONMEMBER, self).validate(data)


class UpcomingWorkshopmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingWorkshopmodels
        fields = '__all__'

class InitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Initiatives
        fields = '__all__'



class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class RemainderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remainder
        fields = ['id','title','taskType','description','duration','color','is_pinned','date']




    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])

        user.save()
        return user



