from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    exam_number = models.IntegerField()
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=30)