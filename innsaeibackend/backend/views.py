from django.http import JsonResponse
from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CertificateSerializer, ComponentSerializer, ContactSerailizer, Councilserializer, Councilserializerurl, DeveloperSerializer, EditorialSerializer, EventSerializer_2, InitiativeSerializer, RemainderSerializer, UpcomingWorkshopmodelsSerializer,  UserSerializer, ProfileSerializer, UserSerializerNONMEMBER
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utils import Util
import random
from django.contrib.sites.shortcuts import get_current_site
from .models import AppUser, Component, DevelopersURL, Initiatives, Remainder, UpcomingWorkshopmodels, certificates, councilMembers, developers, editorials,  events2, AppUserNONMEMBER
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
        serialized_profile = ProfileSerializer(profile,many = False, context={'request': request})
        return Response({'status': 1, 'profile':serialized_profile.data, })
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_phone(request):
    try:
        user = request.user
        profile = AppUser.objects.get(user=user)
        data = request.data
        print(data['phone_number'])
        profile.phone_number = (data['phone_number'])
        
        profile.save()
        return Response({'status': 1,'post': "mobile number saved!"})
    except:
        detail = { 'status':0, 'post': "phone number not saved"}
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)




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
            #return Response(serializer.data, status=1)
            return Response({'status': 1,'contact_us':serializer.data})
        #return Response(serializer.errors, status=0) // use commented Response code in above and current line if API not working.
        return Response({'status': 0, 'message':serializer.errors})

        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def editorialsList(request):
    try:
        user = request.user
        profile = AppUser.objects.get(user=user)
        editorial = editorials.objects.all()
        print(editorial)
        serialized_links = EditorialSerializer(editorial, many = True)
        return Response({'status': 1, 'link':serialized_links.data})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def developersList(request):
    try:
        
        user = request.user
        profile = AppUser.objects.get(user=user)
        developer = developers.objects.all()
        print(developer)
        serialized_links = DeveloperSerializer(developer, many = True)
        return Response({'status': 1, 'link':serialized_links.data})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def councilsList(request):
    try:
        user = request.user
        profile = AppUser.objects.get(user=user)
        council = councilMembers.objects.all()
        print(council)
        serialized_links = Councilserializer(council, many = True)
        return Response({'status': 1, 'link':serialized_links.data})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEvent_2(request):
    user = request.user
    profile = AppUser.objects.get(user=user)
    eventlist = events2.objects.all()
    print(eventlist)
    if profile.isverified:
        serialized_events = EventSerializer_2(eventlist, many = True)
        return Response({'status': 1,'post':serialized_events.data})
    else:
        return Response({'status': 0, 'message':"User not verified. Please Verify account"})





class MyTokenObtainPairSerializerNONMEMBERS(TokenObtainPairSerializer):
    def validate(self, attrs):
        data =super().validate(attrs)

        data['username'] = self.user.username 
        data['email'] = self.user.email

        # print(data)
        token = data['refresh']
        # current_site = get_current_site(request)

        otp_generated = random.randint(1000,9999)
        profileNONMEMBER = AppUserNONMEMBER.objects.get(user=self.user)
        profileNONMEMBER.otp=otp_generated
        profileNONMEMBER.isMember=True
        profileNONMEMBER.save()

        #absurl = 'http://127.0.0.1:8000/?token='+str(token)
        email_body = 'Hi '+self.user.username+' Your otp to login is ' + str(otp_generated)
        credentials={'to_email': self.user.email,'email_body': email_body, 'email_subject': 'Email verification' }
        Util.send_email(credentials)

        return data

class MyTokenObtainPairViewNONMEMBERS(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializerNONMEMBERS


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verifyOtpNONMEMBERS(request):
    try:
        user = request.user
        profileNONMEMBER = AppUserNONMEMBER.objects.get(user=user)
        data = request.data
       
        print(data['otp'])
        if (int(profileNONMEMBER.otp)==int(data['otp'])):
            print("Otp matched!")
            profileNONMEMBER.isverified = True
            profileNONMEMBER.save()
            return Response({'status': 1, 'message':"User verified successfully"})
        else:
            return Response({'status': 0, 'message':"OTP didnt match. please try again"})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView 
class RegisterUserNONMEMBERS(APIView):
    '''
    Register new user
    '''
    serializer_class = UserSerializerNONMEMBER

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)



#here2
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_phoneNONMEMBERS(request):
    try:
        user = request.user
        profileNONMEMBER = AppUserNONMEMBER.objects.get(user=user)
        data = request.data
        print(data['phone_number'])
        profileNONMEMBER.phone_number = (data['phone_number'])
        
        profileNONMEMBER.save()
        return Response({'status': 1,'post': "mobile number saved!"})
    except:
        detail = { 'status':0, 'post': "phone number not saved"}
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def getCalender(request):
    try:
        task = Remainder.objects.all()
        serializer = RemainderSerializer(task,many=True)
        return Response( {'status':1,'CalenderData':serializer.data} )
    except:
        detail = { 'status':0, 'post': "Calender Event cannot be displayed" }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UpcomingEventsList(request):
    try:
        user = request.user
        profile = AppUser.objects.get(user=user)
        upcomingws = UpcomingWorkshopmodels.objects.all()
        print(upcomingws)
        serialized_links_upcomingws = UpcomingWorkshopmodelsSerializer(upcomingws, many = True)
        return Response({'status': 1, 'link':serialized_links_upcomingws.data})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def InitiativesList(request):
    try:
        user = request.user
        profile = AppUser.objects.get(user=user)
        initiative = Initiatives.objects.all()
        print(initiative)
        serialized_links_intitiatives = InitiativeSerializer(initiative, many = True)
        return Response({'status': 1, 'link':serialized_links_intitiatives.data})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)
    


from django.shortcuts import get_object_or_404

class ComponentList(APIView):

    serializer_class = ComponentSerializer

    def get_object(self, id):
        return get_object_or_404(self.get_queryset(), id=id)

    def get_queryset(self, *args, **kwargs):
        Components = Component.objects.all()
        return Components

    def get(self, request, pk=None, *args, **kwargs):     
        id = pk or request.query_params.get('id')
        user = request.user
        profile = AppUser.objects.get(user=user)
        
        if ( id ):
            serializer = ComponentSerializer(self.get_object(id))
            return Response({'status':1,'ComponentList':serializer.data})
        else:
            serializer = ComponentSerializer(self.get_queryset(), many=True)
            return Response({'status':1,'ComponentList':serializer.data})    
        
        return Response({'status':0,'ComponentList':"You are not an ISA MEMBER"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def certificateList(request):
    try:
        user = request.user
        profile = AppUser.objects.get(user=user)
        certi = certificates.objects.filter(user=user)
        print(certi)
        serialized_links = CertificateSerializer(certi, many = True)
        return Response({'status': 1, 'link':serialized_links.data})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def DevelopersURLmethod(request):
    try:
        user = request.user
        profile = AppUser.objects.get(user=user)
        Developers1 = DevelopersURL.objects.all()
        print(Developers1)
        serialized_links1 = Councilserializerurl(Developers1, many = True, context={'request': request})
        return Response({'status': 1, 'link':serialized_links1.data})
    except:
        detail = { 'status': 0, 'message' : 'Oof something went wrong!' }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return JsonResponse('Hello',safe=False)

