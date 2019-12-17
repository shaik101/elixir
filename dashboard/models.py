from django.db import models
from beautyapp.models import Services
from beautyapp.models import Citys
import datetime

# Create your models here.



class Addstaff(models.Model):
    name = models.CharField(max_length=250)
    mobileno=models.CharField(max_length=12)
    city = models.ForeignKey(Citys, on_delete=models.CASCADE,null=True)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

class Addprice(models.Model):
    price = models.IntegerField()

    def __str__(self):
        return self.price

class Addduration(models.Model):
    duration=models.CharField(max_length=250)

    def __str__(self):
        return self.duration


class Guest(models.Model):
    date=models.DateField(default=datetime.datetime.now())
    gname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=100)
    city = models.ForeignKey(Citys, on_delete=models.CASCADE,null=True)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)
    treatment_by = models.ForeignKey(Addstaff, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.CharField(max_length=50)
    time_in = models.TimeField()
    time_out = models.TimeField()
    total_time = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    payment  =models.CharField(max_length=100)
    comments = models.CharField(max_length=500,default="NA")

    def __str__(self):
        return self.gname
