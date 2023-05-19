from django.db import models
from django.utils import timezone
from user import models as user_models

# 题目
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.IntegerField()
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)

# 试卷
class Paper(models.Model):
    id = models.AutoField(primary_key=True)
    question_ids = models.CharField(max_length=512) 
    # 这里使用的是用符号分割开的问题号的列表，如果不方便可以以后优化。eg: [1,2,3]   
    type = models.IntegerField()

# 考试安排
class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    place = models.CharField(max_length=30)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    max_students = models.IntegerField()

# 订单记录
class ExamOrder(models.Model):
    id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(user_models.Student, on_delete=models.CASCADE)
    paid = models.BooleanField()
    payment = models.FloatField()
    pay_time = models.DateField(default=timezone.now)

