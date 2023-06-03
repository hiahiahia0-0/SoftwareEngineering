from django.contrib import admin
from django.urls import path , re_path
from marking import views
 
urlpatterns = [
    re_path(r'^$|index|marking',views.mark,name='mark'),
    path('finish/', views.finish),
]