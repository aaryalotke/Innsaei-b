from . import views
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('',views.home),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/',views.getUserProfile),
    path('users/updateprofile/',views.updateUserProfile),
    path('users/verifyotp/', views.verifyOtp),
    path('users/logout/', views.userLogout),
    path('users/gallery/',views.getEvent),
    path('users/ContactUs/',views.api_create_contact_view), #3
    path('users/editorial/',views.editorialsList), #4
    path('users/Developers/',views.developersList), #5
    path('users/Council/',views.councilsList), #6
    #path('users/Gallery_2/',views.getEvent_2), #6


]