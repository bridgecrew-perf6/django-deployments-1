from django.contrib import admin
from first_app.models import acessrecord,Topic,Webpage
from first_app.models import UserProfileInfo

# Register your models here.
admin.site.register(acessrecord)
admin.site.register(Topic)
admin.site.register(Webpage)

admin.site.register(UserProfileInfo)