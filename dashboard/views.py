from django.shortcuts import render,redirect
from django.http import HttpResponse
from beautyapp.models import Citys
from beautyapp.models import Appointment
from django.contrib import messages
from beautyapp.models import Services
from beautyapp.models import Gift
from beautyapp.models import Carriers
from .models import Addstaff,Attendence,Expenses, Paymentmod,Addduration
# from .models import Addmanager
from .models import Guest
from beautyapp.models import Franchisee
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import auth


from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .msg91 import msg91

import datetime

from django.db.models import Q

# for weasyprint
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
# from django.template.loader import render_to_string

# from weasyprint import HTML


# Create your views here.
@login_required(login_url='/dashboard/admin_login/')
def dashboard(request):
        if request.method == 'POST':
            to_date = request.POST['to_date']
            f_date = request.POST['from_date']

            if request.user.is_superuser:
                guests = Guest.objects.filter(date__range=(to_date,f_date))
            else:
                city = request.user.city
                guests = Guest.objects.filter(city=city,date__range=(to_date,f_date))

        else:
            if request.user.is_superuser:
                guests = Guest.objects.all()
            else:
                city = request.user.city
                guests = Guest.objects.filter(city=city)
        return render(request,'dashboard/guest_list.html',{'guests':guests})

def guest(request):
    if request.method == 'POST':
        date = request.POST['date']
        name = request.POST['name']
        mobileno = request.POST['mobileno']
        service = request.POST['service']
        serviceby = request.POST['serviceby']
        duration = request.POST.get('duration')
        timein = request.POST['timein']
        timeout = request.POST['timeout']
        # totaltime = request.POST['totaltime']
        price = request.POST['price']
        paym = request.POST['paym']

        # comments = request.POST.get('comments')

        city=request.POST['city']
        city = Citys.objects.get(name=city)

        print(service)
        s = Services.objects.get(pk=service)
        a = Addstaff.objects.get(pk=serviceby)
        p = Paymentmod.objects.get(pk=paym)
        d = Addduration.objects.get(duration=duration)


        new_guest = Guest(date=date,gname=name,mobile=mobileno,city=city,services=s,treatment_by=a,duration=d,time_in=timein,time_out=timeout,price=price,payment=p)
        new_guest.save()
        messages.success(request,' ')
        return redirect(guest)
    services = Services.objects.all()

    if request.user.is_superuser:
        staffs = Addstaff.objects.all()
    else:
        staff_city = request.user.city
        staffs = Addstaff.objects.filter(city=staff_city)

    city = Citys.objects.all()
    paym = Paymentmod.objects.all()
    duration = Addduration.objects.all()
    user_city = request.user.city
    return render(request,'dashboard/guest.html',{'services':services,'staffs':staffs,'city':city,'paym':paym,'duration':duration,'user_city':user_city})


# def guest_list(request):
#     guests = Guest.objects.all()
#     return render(request,'dashboard/guest_list.html',{'guests':guests})

def gdel(request,id):
    dc=Guest.objects.get(id=id)
    dc.delete()
    return redirect(dashboard)

def carriers(request):
    careers=Carriers.objects.all()


    return render(request,'dashboard/carriers.html', {'careers':careers})

def gifts(request):
    gifts = Gift.objects.all()
    return render(request,'dashboard/gifts.html',{'gifts':gifts})

def appointment(request):
    if request.user.is_superuser:
        appointment = Appointment.objects.all()
    else:
        city = request.user.city
        if city is None:
            return redirect(dashboard)
        print(city,' ----- ',city.name)
        appointment = Appointment.objects.filter(city=city).order_by('-date')

    paginator = Paginator(appointment, 5)  # 10 appointments in each page
    page = request.GET.get('page')
    try:
        appointment_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        appointment_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        appointment_list = paginator.page(paginator.num_pages)


    return render(request,'dashboard/appointment.html',{'appointment':appointment_list,'page': page} )
# def edit(request, id):
#     city = Citys.objects.get(id=id)
#     context = {'city': city}
#     return render(request, 'crud/edit.html', context)

def confirm_appointment(request,id):
    appointment = Appointment.objects.get(id=id)
    if request.method == 'POST':
        comments = request.POST['comments']
        mobileno = appointment.mobileno

        print(msg91(mobileno,comments))

        appointment.status = "MSG Sent"

        appointment.save()



    return redirect("adminappointment")

def update(request, id):
    city = Citys.objects.get(id=id)
    city.name = request.POST['name']
    city.save()
    return redirect(addcity)

def clientupdate(request, id):
    print('client update')
    if request.method == 'POST':
        g  = Guest.objects.get(id=id)
        g.time_in = request.POST['time_in']
        g.time_out= request.POST['time_out']
        g.duration=request.POST['duration']
        g.total_time = request.POST['total_time']
        g.comments = request.POST['comments']
        g.save()
        print(request.POST['time_out'])
        return redirect(dashboard)
    return redirect(dashboard)

def update_guest(request, id):
    print('client update')
    if request.method == 'POST':

        g  = Guest.objects.get(id=id)
        g.comments = request.POST.get('cmt')
        g.save()
        return redirect(dashboard)

def modify(request, id):
    service = Services.objects.get(id=id)
    service.name = request.POST['name']

    service.save()
    return redirect(addservice)





def deletes(request,id):
    service = Services.objects.get(id=id)
    service.delete()
    # messages.success(request,('item has been deleted!'))
    return redirect(addservice)

def jobdelete(request,id):
    ca=Carriers.objects.get(id=id)
    ca.delete()
    return redirect(carriers)

def deletgift(request,id):
    g=Gift.objects.get(id=id)
    g.delete()
    return redirect(gifts)


def deleted(request,id):
    appointments=Appointment.objects.get(id=id)
    appointments.delete()
    return redirect(appointment)


def delete(request,id):
    city = Citys.objects.get(id=id)
    city.delete()
    # messages.success(request,('item has been deleted!'))
    return redirect( addcity)

def addservice(request):
    if request.method == 'POST':
        name = request.POST['name']
        service = Services(name=name)
        service.save()
        return redirect(addservice)
    else:
        context_data = {
        'service':Services.objects.all()
        }
    return render(request,'dashboard/addservices.html',context_data)


# def price(request):
#     if request.method == 'POST':
#         price = request.POST['price']
#         p = Price(price=price)
#         p.save()
#         return redirect(price)
#     else:
#         context_data = {
#         'p':Addprice.objects.all()
#         }
#     return render(request,'dashboard/price.html',context_data)


def addstaff(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobileno = request.POST['mobileno']
        # services=request.POST['service']
        city=request.POST['city']
        city = Citys.objects.get(id=city)
        # se=Services.objects.get(id=services)
        staff=Addstaff(name=name,mobileno=mobileno,city=city)
        staff.save()
        return redirect(addstaff)
    else:
        if request.user.is_superuser:
            staff = Addstaff.objects.all()
        else:
            staff_city = request.user.city
            staff = Addstaff.objects.filter(city=staff_city)

        context_data = {
        # 'service':Services.objects.all(),
        'staff':staff,
        'city':Citys.objects.all()
        }
    return render(request,'dashboard/addstaff.html',context_data)

def delete_staff(request,id):
    staff = Addstaff.objects.get(id=id)
    staff.delete()

    return redirect(addstaff)

def update_staff(request, id):
    if request.method == 'POST':
        staff = Addstaff.objects.get(id=id)
        staff.name = request.POST['name']
        staff.mobileno = request.POST['mobileno']
        # s = request.POST.get('service')
        # service = Services.objects.get(id=s)

        # service.save()
        # staff.services = service

        staff.save()
        return redirect(addstaff)
    return redirect(addstaff)

def addcity(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = Citys(name=name)
        city.save()
        return redirect(addcity)
    else:
        context_data = {

          'city':Citys.objects.all()


        }

    return render(request,'dashboard/addcity.html',context_data)


def addprice(request):
    if request.method == 'POST':
        name = request.POST['name']
        price =Addprice(name=name)
        price.save()
        return redirect(addprice)
    else:
        context_data = {

          'price':Addprice.objects.all()


        }

    return render(request,'dashboard/addcity.html',context_data)






def admin_login(request):
    print("inside")
    if request.method=='POST':
        print("in post")
        register=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        print('test')
        if register is not None:
            auth.login(request,register)
            print("admin logged in!")
            return redirect(dashboard)
        else:
            messages.info(request,'invalid credentials')
            return redirect(admin_login)
    else:
        return render(request,'dashboard/admin_login.html')


def franch(request):
    f=Franchisee.objects.all()
    return render(request,'dashboard/franch.html', {'f':f})

def deletefranch(request, id):
    f = Franchisee.objects.get(id=id)
    f.delete()
    return redirect(franch)

def report(request):
    guests = Guest.objects.all()
    return render(request,'dashboard/report.html',{'guests':guests})


# def html_to_pdf_view(request):
#     guests = Guest.objects.all()
#     html_string = render_to_string('dashboard/report.html',{'guests':guests})

#     html = HTML(string=html_string)
#     html.write_pdf(target='/tmp/mypdf.pdf');

#     fs = FileSystemStorage('/tmp')
#     with fs.open('mypdf.pdf') as pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
#         return response

#     return response
def admin_logout(request):
    auth.logout(request)
    return redirect(admin_login)

def addmanager(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobileno = request.POST['mobileno']
        city=request.POST['city']
        city = Citys.objects.get(id=city)
        username=request.POST['username']
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect(addmanager)
        elif User.objects.filter(email=mobileno).exists():
                messages.info(request,'mobile number is taken')
                return redirect(addmanager)
        else:
                user=User.objects.create_user(first_name=name,username=username,email=mobileno,password=password,city=city)
                user.is_staff = True
                user.save()
                return redirect(addmanager)
    else:
        manager = User.objects.filter(is_superuser=False)
        context_data = {
        'manager':manager,
        'city':Citys.objects.all()
        }
    return render(request,'dashboard/addmanager.html',context_data)


def update_manager(request, id):
    if request.method == 'POST':
        m = User.objects.get(id=id)
        m.first_name = request.POST['name']
        m.email = request.POST['mobileno']
        c=request.POST.get('city')
        city=Citys.objects.get(id=c)
        city.save()
        m.city = city
        m.username = request.POST['username']
        m.set_password(str(request.POST['password']))

        m.save()
        return redirect(addmanager)
    return redirect(addmanager)

def delete_manager(request,id):
    manager = User.objects.get(id=id)
    manager.delete()

    return redirect(addmanager)


def attendence(request):
    atten = Attendence.objects.all()
    return render(request,'dashboard/attendence.html',{'atten':atten})



def timein(request):
    if request.method == 'POST':
        name = request.POST['name']
        time_in=request.POST['timein']
        remarks = request.POST['remarks']
        a = Addstaff.objects.get(pk=name)
        print(time_in,'---- ', type(time_in))
        # if Attendence.objects.filter(name=a,date__startswith = datetime.datetime.today().strftime('%Y-%m-%d')).exists():
        #     messages.info(request,a.name+' already entered attendance for the day.')
        #     return redirect(timein)
        c = 0
        for i in Attendence.objects.filter(name=a,date__startswith = datetime.datetime.today().strftime('%Y-%m-%d')):
            c = c+1

        if c >= 1:
            messages.info(request,a.name+' already entered attendance for the day.')
            return redirect(timein)
        else:

            if time_in in " ":
                at = Attendence(name=a,remarks=remarks)
            else:
                at = Attendence(name=a,time_in=time_in,remarks=remarks)
            at.save()
            return redirect(attendence)
    else:
        staf=Addstaff.objects.all()


    return render(request,'dashboard/timein.html',{'staf':staf})

def timeout(request):
    if request.method == 'POST':
        name = request.POST['name']
        time_out = request.POST['timeout']
        # print(name)
        b = Addstaff.objects.get(id=name)
        # print(type(b),' ---')
        a = get_object_or_404( Attendence,Q(name=b) & Q(date__startswith = datetime.datetime.today().strftime('%Y-%m-%d') ))
        # a = Attendence.objects.get( name=b)
        # print(dir(a))
        # print(a.time_in)
        a.time_out = time_out
        a.save()
        return redirect(timeout)

    else:
        staff = Addstaff.objects.all()



    return render(request,'dashboard/timeout.html',{'staff':staff})



def delete_atten(request,id):
    t = Attendence.objects.get(id=id)
    t.delete()
    return redirect(attendence)


def expenses(request):
    if request.method == 'POST':
        date = request.POST['date']
        particular = request.POST['particular']
        bill_no = request.POST['bill_no']
        amount = request.POST['amount']
        reciept = request.FILES.get('rc')

        print(reciept)


        city = request.POST['city']
        city = Citys.objects.get(id=city)

        ex = Expenses(date=date,particular=particular,bill_no=bill_no,amount=amount,reciept=reciept,city=city)
        ex.save()
        return redirect(expenses)
    else:
        city = Citys.objects.all()

    return render(request,'dashboard/expenses.html',{'city':city})


def update_expense(request, id):
    if request.method == 'POST':
        e = Expenses.objects.get(id=id)
        e.date = request.POST['date']
        e.particular = request.POST['particular']
        e.bill_no = request.POST['bill_no']
        e.amount = request.POST['amount']
        #e.city = city

        e.save()
        return redirect(expenses)
    return redirect(expenses)

def delete_expense(request,id):
    exp = Expenses.objects.get(id=id)
    exp.delete()
    return redirect(exdetail)

def exdetail(request):
    # ex=Expenses.objects.all()
    if request.method == 'POST':
        to_date = request.POST.get('to_date')
        f_date = request.POST.get('from_date')

        if request.user.is_superuser:
            ex = Expenses.objects.filter(date__range=(to_date,f_date))
        else:
            city = request.user.city
            ex = Expenses.objects.filter(city=city,date__range=(to_date,f_date))

    else:
        if request.user.is_superuser:
            ex = Expenses.objects.all()
        else:
            city = request.user.city
            ex = Expenses.objects.filter(city=city)
    return render(request,'dashboard/expensedetails.html', {'ex':ex})

def paymentmod(request):
    if request.method == 'POST':
        name = request.POST['name']
        pay = Paymentmod(name=name)
        pay.save()
        return redirect(paymentmod)
    else:
        context_data = {

          'pay': Paymentmod.objects.all()


        }

    return render(request,'dashboard/paymentmod.html',context_data)



def paymentmod(request):
    if request.method == 'POST':
        name = request.POST['name']
        pay = Paymentmod(name=name)
        pay.save()
        return redirect(paymentmod)
    else:
        context_data = {

          'pay': Paymentmod.objects.all()


        }

    return render(request,'dashboard/paymentmod.html',context_data)

def paymentmodchange(request, id):
    p = Paymentmod.objects.get(id=id)
    p.name = request.POST['name']
    p.save()
    return redirect(paymentmod)


def deletepaymentmod(request,id):
    p = Paymentmod.objects.get(id=id)
    p.delete()
    return redirect(paymentmod)

def adduration(request):
    if request.method == 'POST':
        name= request.POST['name']
        dn = Addduration(duration=name)
        dn.save()
        return redirect(adduration)
    else:
        context_data = {

          'dn': Addduration.objects.all()


        }

    return render(request,'dashboard/adduration.html',context_data)

def durationchange(request, id):
    a = Addduration.objects.get(id=id)
    a.name = request.POST['name']
    a.save()
    return redirect(adduration)

def deleteduration(request,id):
    a = Addduration.objects.get(id=id)
    a.delete()
    return redirect(adduration)
