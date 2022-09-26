from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import message, send_mail
from django.contrib.auth.models import User
import uuid
from django.conf import settings

class AppUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    otp = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=100, default='Student')
    description = models.CharField(max_length=256,default='')
    achievements = models.CharField(max_length=256,default='')
    github = models.CharField(max_length=100,default='')
    linkedin = models.CharField(max_length=100,default='')
    isverified = models.BooleanField(default=False)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profile_image/")

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:     
        profile = AppUser.objects.create(user=instance)
        profile.save()

TYPE = (
    ("Software", "Software"),
    ("Hardware", "Hardware"),
    ("Other", "Other"),
)

class event(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='events/eventPosters')
    description = models.TextField()
    type = models.CharField(choices=TYPE, max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    gallary_pic1 = models.ImageField(upload_to='events/eventsGallary')
    gallary_pic2 = models.ImageField(upload_to='events/eventsGallary')
    gallary_pic3 = models.ImageField(upload_to='events/eventsGallary')
    gallary_pic4 = models.ImageField(upload_to='events/eventsGallary')

class contactus(models.Model):
    name = models.CharField(max_length=100)
    email=  models.EmailField(blank=True, max_length=100)
    phoneNumber = models.CharField(max_length=15)
    message= models.CharField(blank=True, max_length=500)
    


    def __str__(self):
        return self.name