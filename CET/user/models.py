from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True) # 考号
    self_number = models.IntegerField() # 身份证
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=30,unique=True,null=False)
    email = models.CharField(max_length=20)

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30,unique=True,null=False)
    password = models.CharField(max_length=30)