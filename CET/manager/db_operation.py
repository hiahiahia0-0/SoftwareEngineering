from user import models as user_m
import time
from typing import Optional,Tuple


'''
本文件：
    封装数据库操作
    日志记录
    返回值代表不同信息
'''

NOT_EXIST = -1
DUPLICATE = -2
FAIL = 0
SUCCESS = 1

def sys_log(msg):
    # 绿色高亮打印当前时间和信息
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("\033[1;32m LOG:" + now + ": " + msg + "\033[0m")


def db_get_stu_by_id(id) -> tuple[Optional[user_m.Student] , int]:
    try:
        try :
            stu =  user_m.Student.objects.get(id=id)
        except user_m.Student.DoesNotExist:
            sys_log('学生查询不存在')
            return None ,NOT_EXIST
        else:
            sys_log('学生查询成功')
            return stu , SUCCESS
    except:
        sys_log('学生查询失败')
        return None,FAIL

def db_get_tea_by_id(id) -> Tuple[Optional[user_m.Teacher], int]:
    try:
        try :
            tea =  user_m.Teacher.objects.get(id=id)
        except user_m.Teacher.DoesNotExist:
            sys_log('教师查询不存在')
            return None,NOT_EXIST
        else:
            sys_log('教师查询成功')
            return tea ,SUCCESS
    except:
        sys_log('教师查询失败')
        return None, FAIL

def db_add_stu(self_num, name, school, password, phone, email): # id是自增的，不用管
    try:
        stu = user_m.Student(self_number=self_num, name=name, school=school, password=password, phone=phone, email=email)
        stu.save()
        sys_log('学生添加成功')
        return SUCCESS
    except:
        return FAIL

def db_add_tea(name, phone, password): # id自增
    try:
        tea = user_m.Teacher(name=name, phone=phone, password=password)
        tea.save()
        sys_log('教师添加成功')
        return SUCCESS
    except:
        return FAIL