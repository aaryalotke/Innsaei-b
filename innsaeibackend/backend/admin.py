from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import AppUser, Component, DevelopersURL, Initiatives, UpcomingWorkshopmodels, contactus, councilMembers, developers, editorials,  events2
#Register your models here.


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email', 'password')

class UserAdmin(ImportExportModelAdmin):
    list_display = ('id','username','first_name', 'last_name', 'email', 'password')
    # list_filter = ('created_at',)
    resource_class = UserResource
    pass


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(AppUser)

admin.site.register(contactus)
admin.site.register(editorials)
admin.site.register(developers)
admin.site.register(councilMembers)
admin.site.register(events2)
admin.site.register(UpcomingWorkshopmodels)
admin.site.register(Component)
admin.site.register(Initiatives)
admin.site.register(DevelopersURL)
