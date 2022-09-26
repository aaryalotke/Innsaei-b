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
    path('users/ContactUs/',views.api_create_contact_view)#3


]