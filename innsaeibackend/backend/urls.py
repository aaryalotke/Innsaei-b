from . import views
from django.contrib import admin
from django.urls import path, include



urlpatterns = [

    path('',views.home), #1
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'), #2
    path('users/profile/',views.getUserProfile), #3
    path('users/updateprofile/',views.updateUserProfile), #4
    path('users/verifyotp/', views.verifyOtp), #5
    path('users/logout/', views.userLogout), #6 
    path('users/ContactUs/',views.api_create_contact_view), ##7
    path('users/editorial/',views.editorialsList), #8
    path('users/Developers/',views.developersList), #9
    path('users/Council/',views.councilsList), #10
    path('users/Gallery_2/',views.getEvent_2), #11
    path('users/phone/',views.get_phone), #12
    path('users/RegistrationNONMEMBERS/',views.RegisterUserNONMEMBERS.as_view(), name='Registration'), #13
    path('users/loginNONMEMBERS/', views.MyTokenObtainPairViewNONMEMBERS.as_view(), name='token_obtain_pair'), #14
    path('users/verifyotpNONMEMBERS/', views.verifyOtpNONMEMBERS), #15
    path('users/phoneNONMEMBERS/',views.get_phoneNONMEMBERS), #16
    path('users/calender/',views.getCalender), #17
    path('users/UpcomingWorkshop/',views.UpcomingEventsList), #17
    path('users/Product/', views.ComponentList.as_view()), #18
    path('users/Product/<int:pk>/', views.ComponentList.as_view()), #19
    path('users/Initiatives/',views.InitiativesList), #20
    path('users/DevelopersURL/',views.DevelopersURLmethod), #21
    path('users/certificateList/',views.certificateList), #22

]