from django.contrib import admin
from django.urls import path , re_path
from exam import views

urlpatterns = [
    path('exam/',views.exam_info,name='exam_info'),
    path('exam/d/',views.exam_detail,name='exam_detail'),
    path('exam/<int:exam_id>/submit/',views.exam_submit,name='exam_submit'),
]