from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.CASCADE,null = True,blank=True)
    courses = models.ManyToManyField('Course')
    college = models.ForeignKey('College',on_delete=models.CASCADE,null = True,blank=True)
    def __str__(self):
        return self.name


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    hod_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.course_name
        

class College(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    affilated_by = models.CharField(max_length=100)
    def __str__(self):
        return self.name