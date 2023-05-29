from django.contrib import admin
from django.urls import path , re_path
from exam import views

urlpatterns = [
    re_path(r'^$',views.exam_info,name='exam_info'),
    # path('online/<int:exam_id>',views.exam_detail,name='exam_detail'),
    # path('online/submitted/<int:exam_id>/<int:use_time>',views.exam_submit,name='exam_submitted'),
    path('online/',views.exam_d,name='exam_detail'),
    path('online/submit',views.exam_s,name='exam_detail'),
]