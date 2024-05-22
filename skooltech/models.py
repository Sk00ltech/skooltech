from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=200)

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    dream = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=200)
    _class = models.CharField(max_length=200)
    shift = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)