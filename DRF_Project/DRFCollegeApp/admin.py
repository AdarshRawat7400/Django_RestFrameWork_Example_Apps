from django.contrib import admin
from .models import Student,Department,Course,College
# Register your models here.

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(College)

