from django.contrib import admin

# Register your models here.
# app01/admin.py:
from exam.models import Exam,ExamOrder,Paper,Question
from user.models import Student,Teacher
from marking.models import AnswerRecord,ExamScore
 
# 注册Model类
admin.site.register(Exam)
admin.site.register(ExamOrder)
admin.site.register(Paper)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(AnswerRecord)
admin.site.register(ExamScore)

admin.site.site_header = 'CET管理后台'  # 设置header
admin.site.site_title = 'CET管理后台'   # 设置title
admin.site.index_title = 'CET管理后台'

