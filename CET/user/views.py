from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from user import models
from user.models import Student
from user.models import Teacher
import random
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
# 初始页面 表单 http://127.0.0.1:8000/user/index 选择登陆谁
# 学生登陆界面：http://127.0.0.1:8000/user/stu_signin ，输入用户名和密码，正确的话跳转到下一个用户信息页面，不正确的话保持在该页面，但是不知道为啥错误提示不显示
# 教师登陆页面：http://127.0.0.1:8000/user/tea_signin ， 同样，可以正确判断输入是否符合，但是报错信息不知道为啥不显示
# 学生注册：http://127.0.0.1:8000/user/stu_signup，可以判断已存在的用户，密码不一致啥的，还是报错信息不会显示
# 教师注册：http://127.0.0.1:8000/user/tea_signup，同上
# 忘记密码的逻辑还没写，不知道忘记密码之后，要靠啥验证身份信息
# 后边的个人信息页面还没写，明天再写

def index(request):
    return render(request,'index.html')



#选择是教师登录还是学生登陆,接收请求数据
@csrf_protect
def choose_sign(request):
    if request.method == 'POST':
        login_type = request.POST.get('login_type')
        if login_type == 'student':
            return redirect('stu_signin')  # 跳转到学生登录页面的URL名称
            # 跳转过去报错，要设置默认的个人信息吗？
        elif login_type == 'teacher':
            return redirect('tea_signin')  # 跳转到教师登录页面的URL名称

    return render(request, 'index.html')
# Create your views here.
#登录

#教师登录
#不知道为啥不对？
def tea_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 有一个Teacher表，存储教师账户信息
        try:
            t = Teacher.objects.get(name=username)
            if t is None:
                # 报错信息，用户不存在
                messages.info(request, '用户不存在')
                return redirect('tea_signin')
            elif t.password == password:
                # 登录成功，跳转到下一个用户信息页面
                return redirect('tea_info')  # 跳转到用户信息页面的URL名称
            else:
                # 密码错误
                messages.info(request, '密码错误')
        except Teacher.DoesNotExist:
            # 用户不存在
            messages.info(request, '用户不存在')
        # 登录失败，返回教师登录页面并显示错误信息
        return redirect('tea_signin')

    return render(request,'tea_signin.html')



#学生登录
def stu_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 有一个Teacher表，存储教师账户信息
        try:
            t = Student.objects.get(name=username)
            if t is None:
                # 报错信息，用户不存在
                messages.info(request, '用户不存在')
                return redirect('stu_signin')
            elif t.password == password:
                # 登录成功，跳转到下一个用户信息页面
                return redirect('stu_info')  # 跳转到用户信息页面的URL名称
            else:
                # 密码错误
                messages.info(request, '密码错误')
        except Student.DoesNotExist:
            # 用户不存在
            messages.info(request, '用户不存在')
        # 登录失败，返回教师登录页面并显示错误信息
        return redirect('stu_signin')

    return render(request,'stu_signin.html')

#教师注册
def tea_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # 检查用户名是否已存在
        if Teacher.objects.filter(name=username).exists():
            error_message = '用户已存在'
            return render(request, 'tea_signup.html', {'error_message': error_message})

        # 检验密码和确认密码是否一致
        if password != confirm_password:
            error_message = '两次输入的密码不一致'
           # return render(request, 'tea_signup.html', error_message)
            return render(request, 'tea_signup.html', {'error_message': error_message})
            # return HttpResponse(error_message)

        # 创建新教师账户并保存到数据库
        teacher = Teacher(name=username,phone=phone, password=password)
        teacher.save()

        # 注册成功，跳转到用户登录界面
        return redirect('tea_signin')  # 跳转到教师登录页面的URL名称

    return render(request, 'tea_signup.html')

#学生注册

def stu_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        id_number = request.POST.get('id_number')
        # 检查用户名是否已存在
        if Student.objects.filter(name=username).exists():
            error_message = '用户已存在'
            return render(request, 'stu_signup.html', {'error_message': error_message})

        # 检验密码和确认密码是否一致
        if password != confirm_password:
            error_message = '两次输入的密码不一致'
           # return render(request, 'tea_signup.html', error_message)
            return render(request, 'stu_signup.html', {'error_message': error_message})
            # return HttpResponse(error_message)

        # 创建新学生账户并保存到数据库
        student = Student(name=username, exam_number=id_number,phone=phone, password=password)
        student.save()

        # 注册成功，跳转到用户登录界面
        return redirect('stu_signin')  # 跳转到教师登录页面的URL名称

    return render(request, 'stu_signup.html')
