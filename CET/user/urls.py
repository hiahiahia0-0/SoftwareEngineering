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
    path('logout', views.logout, name='logout'),
    path('stu_all', views.stu_all, name='stu_all'),
    path('stu_info', views.stu_info, name='stu_info'),
    path('mod_info_stu', views.mod_info_stu, name='mod_info_stu'),
    path('go_to_exam', views.go_to_exam, name='go_to_exam'),
    path('go_to_mark', views.go_to_mark, name='go_to_mark'),
    path('stu_exam_grade', views.get_stu_exam_grade, name='stu_exam_grade'),
    path('tea_info', views.tea_info, name='tea_info'),
    path('logout_tea', views.logout, name='logout_tea'),
    path('mod_info_tea', views.mod_info_tea, name='mod_info_tea'),
    path('mod_password_stu', views.mod_password_stu, name='mod_password_stu'),
    path('mod_password_tea', views.mod_password_tea, name='mod_password_tea'),

]

