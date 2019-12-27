from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('addcity/',views.addcity,name='addcity'),
    path('gifts/',views.gifts,name='gifts'),
    path('addstaff/',views.addstaff,name='addstaff'),
    path('addstaff/delete_staff/<int:id>',views.delete_staff,name='delete_staff'),
    path('addstaff/update_staff/<int:id>',views.update_staff,name='updates'),

    path('addmanager/',views.addmanager,name='addmanager'),
    path('addmanager/update_manager/<int:id>',views.update_manager,name='update_manager'),
    path('addmanager/delete_manager/<int:id>',views.delete_manager,name='delete_manager'),

    path('gifts/deletgift/<int:id>',views.deletgift,name='deletgift'),
    path('carriers/jobdelete/<int:id>',views.jobdelete,name='jobdelete'),

    # path('price/',views.price,name='price'),

    path('carriers/',views.carriers,name='carriers'),
    path('addcity/update/<int:id>',views.update,name='update'),
    path('clientupdate/<int:id>',views.clientupdate,name="updateguest"),

    path('appointment',views.appointment,name='adminappointment'),
    path('confirm/<int:id>',views.confirm_appointment,name='confirm_appointment'),
    path('addcity/delete/<int:id>',views.delete,name='delete'),
    path('appointment/deleted/<int:id>',views.deleted,name='deleted'),
    path('addservice/',views.addservice,name='addservice'),
    path('addservice/modify/<int:id>',views.modify,name='modify'),
    path('addservice/deletes/<int:id>',views.deletes,name='deletes'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('guest/',views.guest,name='guest'),
    # path('guest_list/',views.guest_list,name='guest_list'),
    path('guest/gdel/<int:id>',views.gdel,name='gdel'),
    path('franch/',views.franch,name='franch'),

    path('franch/deletefranch/<int:id>',views.deletefranch,name='deletefranch'),
    # path('report/',views.html_to_pdf_view,name='report'),
    path('test/',views.report,name='test'),
    path('timein/',views.timein,name='timein'),
    path('timeout/',views.timeout,name='timeout'),
    path('attendence/',views.attendence,name='attendence'),
    path('attendence/delete_atten/<int:id>',views.delete_atten,name='delete_atten'),
    path('expenses/',views.expenses,name='expenses'),
    path('paymentmod/',views.paymentmod,name='paymentmod'),
    path('paymentmodchange/<int:id>',views.paymentmodchange,name='paymentmodchange'),
    path('paymentmod/deletepaymentmod/<int:id>',views.deletepaymentmod,name='deletepaymentmod'),
    path('adduration/',views.adduration,name='adduration'),
    path('adduration/durationchange/<int:id>',views.durationchange,name='durationchange'),
    path('adduration/deleteduration/<int:id>',views.deleteduration,name='deleteduration'),











    # path('edit/<int:city_id>',views.edit,name='edit')

]
