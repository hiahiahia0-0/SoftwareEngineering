from django.contrib import admin
from django.urls import path , re_path
from reg import views

urlpatterns = [
<<<<<<< HEAD
        path("reg_view/", views.index),
    path("reg_template_test/", views.template_test),
    path("reg_main/", views.reg_main),
    path('ConfirmRegState/', views.ConfirmRegState, name='ConfirmRegState'),
    path('SelectSite/', views.SelectSite, name='SelectSite'),
    path('TakeAnPosition/', views.TakeAnPosition, name='TakeAnPosition'),
    path('PayOrder/', views.PayOrder, name='PayOrder'),
    path('CheckOrder/', views.CheckOrder, name='CheckOrder'),
=======
>>>>>>> 48b74f5179aa582ffcf10e77a1531744ad15fcc4
]