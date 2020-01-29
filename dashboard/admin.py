from django.contrib import admin

# Register your models here.
from  beautyapp.models import Appointment,User
from dashboard.models import Guest
admin.site.register(Appointment)
admin.site.register(Guest)

admin.site.register(User)
