from email.mime import image
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import message, send_mail
from django.contrib.auth.models import User
import uuid
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class AppUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    otp = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=100, default='Student')
    github = models.URLField(max_length=100,default='')
    linkedin = models.URLField(max_length=100,default='')
    isverified = models.BooleanField(default=False)
    profile_image = models.URLField(default="https://drive.google.com/uc?export=download&id=1-mYSwvSe_mlXsuRBLriygnnURC_NodEy")
    phone_number=models.CharField(null=True,max_length=13,blank=True,unique=True)
    isMember = models.BooleanField(default=True)
    #models.ImageField(null=True, blank=True, upload_to="profile_image/") 

    def __str__(self):
        return self.user.email

#@receiver(post_save, sender=User)
#def create_profile_signal(sender, instance, created, **kwargs):
#    if created:     
#        profile = AppUser.objects.create(user=instance, isMember=True)
#        profile.save()

TYPE = (
    ("Software", "Software"),
    ("Hardware", "Hardware"),
    ("Other", "Other"),
)



class AppUserNONMEMBER(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100,default='')
    otp = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=100, default='Student')
    description = models.CharField(max_length=256,default='')
    achievements = models.CharField(max_length=256,default='')
    github = models.CharField(max_length=100,default='')
    linkedin = models.CharField(max_length=100,default='')
    isverified = models.BooleanField(default=False)
    phone_number=models.CharField(null=True,max_length=13,blank=True,unique=True)
    isMember = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profileNONMEMBER = AppUserNONMEMBER.objects.create(user=instance, isMember=False)
        profileNONMEMBER.save()




class contactus(models.Model):
    name = models.CharField(max_length=100)
    email=  models.EmailField(blank=True, max_length=100)
    phoneNumber = models.CharField(max_length=15)
    message= models.CharField(blank=True, max_length=500)
    def __str__(self):
        return "{} {}".format(self.email, self.phoneNumber)

class editorials(models.Model):
    editorial_name=models.CharField(max_length=100)
    editorial_link=models.URLField()
    
    def __str__(self):
        return self.editorial_name

COUNCIL = (
    ("SE", "SE"),
    ("TE", "TE"),
    ("BE", "BE"),
    ("FACULTY ADVISORS ", "FACULTY ADVISORS"),
)


class developers(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='developers')
    council = models.CharField(choices=COUNCIL, max_length=100)
    post = models.CharField(max_length=100)
    order_number = models.IntegerField(default=0, blank=True)
    insta_id = models.URLField(blank=True)
    linked_in =  models.URLField(blank=True)
    email=  models.CharField(blank=False,max_length=100)
    phoneNumber = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.phoneNumber)


class events2(models.Model):
    name = models.CharField(max_length=100)
    poster1 =  models.ImageField(null=True, blank=True, upload_to='events')   #hardware
    poster2 =  models.ImageField(null=True, blank=True, upload_to='events')   #software
    poster3 =  models.ImageField(null=True, blank=True, upload_to='events')   #others
    order_number = models.IntegerField(default=0, blank=True)
    description = models.TextField()
    type = models.CharField(choices=TYPE, max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    gallary_pic1_link = models.ImageField(null=True, blank=True, upload_to='events')
    gallary_pic2_link = models.ImageField(null=True, blank=True, upload_to='events')
    gallary_pic3_link = models.ImageField(null=True, blank=True, upload_to='events')
    gallary_pic4_link = models.ImageField(null=True, blank=True, upload_to='events')
    
    def __str__(self):
        return "{} {} {}".format(self.name, self.start_date, self.type)


class councilMembers(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='developers')
    council = models.CharField(choices=COUNCIL, max_length=100)
    post = models.CharField(max_length=100)
    order_number = models.IntegerField(default=0, blank=True)
    insta_id = models.URLField(blank=True)
    linked_in =  models.URLField(blank=True)
    email=  models.CharField(blank=False,max_length=100)
    phoneNumber = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.council)



class Remainder(models.Model):

    description = models.CharField(max_length=150, blank=True)
    duration = models.DateField()
    is_pinned = models.BooleanField(default=False)
    color = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


class UpcomingWorkshopmodels(models.Model):
    EventName = models.CharField(max_length=500, blank=True)
    PosterImage =models.ImageField(null=True, blank=True, upload_to='UpcomingEvents')
    FormLink = models.URLField(blank=True)
    Description = models.TextField()
    DurationDate = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.EventName
    


class Initiatives(models.Model):
    Name = models.CharField(max_length=500, blank=True)
    Image = models.URLField(null=True, blank=True)
    InitiativesLink = models.URLField(blank=True)
    Description = models.TextField()
    
    def __str__(self):
        return self.Name
    


class Component(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to='Components')
    Small_Specs = models.CharField(max_length=254,null=False)
    Info = models.TextField(null=False)
    Is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name



class DevelopersURL(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='council')
    post = models.CharField(max_length=100)
    order_number = models.IntegerField(default=0, blank=True)
    insta_id = models.URLField(blank=True)
    linked_in =  models.URLField(blank=True)
    email=  models.URLField(blank=True)

    def __str__(self):
        return self.first_name


YEARS=(
    ("2020", "2020"),
    ("2021", "2021"),
    ("2022", "2022"),
    ("2023", "2023"),
    ("2025", "2025"),
    
)
class certificates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(AppUser, default=1, on_delete=models.CASCADE)
    certificate_year = models.CharField(max_length=150,choices=YEARS)
    workshop_name= models.CharField(max_length=150, blank=True)
    certificates = models.URLField(blank=True)

    def __str__(self):
        return "{} {} {}".format(self.user, self.workshop_name, self.certificate_year)




def __str__(self):
    return self.name