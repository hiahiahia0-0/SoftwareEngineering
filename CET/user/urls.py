from django.urls import path, re_path
# 从自己的 app 目录引入 views
from user import views

urlpatterns = [
    # 初始界面，选择谁登录

    # 用正则表达式设置，默认界面和index都可以登录
    re_path(r'^$|index', views.index, name='index'),

    path('tea_signin', views.tea_signin, name='tea_signin'),
    path('stu_signin', views.stu_signin, name='stu_signin'),
    path('tea_signup', views.tea_signup, name='tea_signup'),
    path('stu_signup', views.stu_signup, name='stu_signup'),

]

