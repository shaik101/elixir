from django.contrib import admin

# Register your models here.
from  .models import Citys
from .models import Services
from .models import Carriers

from .models import Gift
class GiftAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile','address','message','price')


admin.site.register(Gift)

admin.site.register(Citys)
admin.site.register(Carriers)

admin.site.register(Services)
