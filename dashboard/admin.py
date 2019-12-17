from django.contrib import admin

# Register your models here.
from  beautyapp.models import Appointment,User
admin.site.register(Appointment)

admin.site.register(User)
