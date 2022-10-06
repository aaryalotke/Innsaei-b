from django.http import JsonResponse
from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ContactSerailizer, UserSerializer, ProfileSerializer, EventSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utils import Util
import random
from django.contrib.sites.shortcuts import get_current_site
from .models import AppUser, event
from rest_framework import status
from django.contrib.auth.models import User
from django.core.mail import send_mail
from email import message



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data =super().validate(attrs)

        data['username'] = self.user.username 
        data['email'] = self.user.email

        # print(data)
        token = data['refresh']
        # current_site = get_current_site(request)

        otp_generated = random.randint(1000,9999)
        profile = AppUser.objects.get(user=self.user)
        profile.otp=otp_generated
        profile.save()

        #absurl = 'http://127.0.0.1:8000/?token='+str(token)
        email_body = 'Hi '+self.user.username+' Your otp to login is ' + str(otp_generated)
        credentials={'to_email': self.user.email,'email_body': email_body, 'email_subject': 'Email verification' }
        Util.send_email(credentials)

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    profile = AppUser.objects.get(user=user)
    if profile.isverified:
        serialized_profile = ProfileSerializer(profile,many = False)
        return Response({'status': 1, 'profile':serialized_profile.data})
    else:
        return Response({'status': 0, 'message':"User not verified. Please Verify account"})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    try:
        user = request.user
        serialized_users = UserSerializer(user,many = False)
        profile = AppUser.objects.get(user=user)
        serialized_profile = ProfileSerializer(profile,many = False)
        data = request.data
        print(data)
        if profile.isverified:
            if "description" in data:
                profile.description = data['description']
                print(profile.description)
            if "achievements" in data:
                profile.achievements = data['achievements']
                print(profile.achievements)
            if "github" in data:    
                profile.github = data['github']
                print(profile.github)
            if "linkedin" in data:
                profile.linkedin = data['linkedin']
                print(profile.linkedin)
            if "profile_image" in data:
                profile.profile_image = data['profile_image']
            print(profile)
            profile.save()
            return Response({'status': 1, 'message':"User updated successfully",'profile':serialized_profile.data})
        else:
            return Response({'status': 0, 'message':"User not verified. Please Verify account"})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong while updating profile!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verifyOtp(request):
    try:
        user = request.user
        profile = AppUser.objects.get(user=user)
        data = request.data
       
        print(data['otp'])
        if (int(profile.otp)==int(data['otp'])):
            print("Otp matched!")
            profile.isverified = True
            profile.save()
            return Response({'status': 1, 'message':"User verified successfully"})
        else:
            return Response({'status': 0, 'message':"OTP didnt match. please try again"})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userLogout(request):
    user = request.user
    profile = AppUser.objects.get(user=user)
    if profile.isverified:
        profile.isverified = False
        profile.save()
        return Response({'status': 1, 'message':"User Logged out"})
    else:
        return Response({'status': 0, 'message':"Please Log in first"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEvent(request):
    user = request.user
    profile = AppUser.objects.get(user=user)
    eventlist = event.objects.all()
    print(eventlist)
    if profile.isverified:
        serialized_events = EventSerializer(eventlist, many = True)
        return Response({'status': 1,'post':serialized_events.data})
    else:
        return Response({'status': 0, 'message':"User not verified. Please Verify account"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_contact_view(request):
    if request.method == "POST":
        serializer = ContactSerailizer(data=request.data)
        if serializer.is_valid():
            name = request.data['name']
            email = request.data['email']
            message = request.data['message']
            phone = request.data['phoneNumber']

            # send mail
            send_mail(
                "mail from" + " " + name,
                message + " "+ "\n \nMail From: "+ email + " "+"\nPhone Number: "+ phone ,
                email,
                ['alumnihub.isavesit@gmail.com'],  #mail to 
                fail_silently=False,
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
def home(request):
    return JsonResponse('Hello',safe=False)

