from django.db import models
from datetime import datetime
# from beautyapp.models import Services
# from beautyapp.models import Citys
from beautyapp.models import Citys
from beautyapp.models import Services
# Create your models here.



class Addstaff(models.Model):
    name = models.CharField(max_length=250)
    mobileno=models.CharField(max_length=12)
    city = models.ForeignKey(Citys, on_delete=models.CASCADE,null=True)
    # services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)


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

class Paymentmod(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name




class Guest(models.Model):
    # PAY_CHOICES = (("ONLINE","online"),("CASH","cash"))
    date=models.DateField(default=datetime.now())
    gname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=100)
    city = models.ForeignKey(Citys, on_delete=models.CASCADE,null=True)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)
    treatment_by = models.ForeignKey(Addstaff, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.ForeignKey(Addduration, on_delete=models.CASCADE,null=True)
    time_in = models.TimeField()
    time_out = models.TimeField()
    # total_time = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    payment  =models.ForeignKey(Paymentmod, on_delete=models.CASCADE,null=True)

    comments = models.CharField(max_length=500,default="NA",)

    def __str__(self):
        return self.gname


class Attendence(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    name = models.ForeignKey(Addstaff, on_delete=models.CASCADE, null=True, blank=True)
    time_in = models.TimeField(null=True,blank=True)
    time_out = models.TimeField(null=True,blank=True)
    remarks = models.CharField(max_length=250,default="present")

    def __str__(self):
        return self.name


class Expenses(models.Model):
    date=models.DateField(default=datetime.now())
    particular = models.CharField(max_length=250)
    bill_no = models.CharField(max_length=400)
    amount = models.CharField(max_length=50)
    remarks = models.CharField(max_length=250)
    reciept=models.ImageField(upload_to='Images/expenses/')
    city = models.ForeignKey(Citys, on_delete=models.CASCADE,null=True)
