from django.urls import path
from beautyapp import views
from django.contrib import admin

from django.conf import settings
admin.site.header = 'Elixir Beauty Spa'

urlpatterns = [
    path('about/',views.about,name='about'),
    path('service/',views.services,name='service'),
    # path('gallery/',views.spa_treatment,name='spa_treatment'),
    # path('blog/',views.blog,name='blog'),
    # path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('appointment/',views.appointment,name='appointment'),
    path('contact/',views.contact,name='contact'),
    path('gift/',views.buygift,name='buygift'),
    path('gallery/',views.gallery,name='gallery'),
    path('espackage/',views.espackage,name='espackage'),
    path('careers/',views.careers,name='careers'),
    path('mens/',views.mens,name='mens'),
    path('footrefl/',views.footrefl,name='footrefl'),
    path('memberplan',views.memberplan,name='memberplan'),
    path('eservice',views.eservice,name='eservice'),
    path('franchisee',views.franchisee,name='franchisee'),




]
