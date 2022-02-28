from itertools import count
from pkgutil import read_code
from rest_framework import serializers
from .models import Department,Student,Course,College



class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer): 
    # department = DepartmentSerializer()
    # courses = CourseSerializer(many=True)
    # college = CollegeSerializer()
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['department'] = DepartmentSerializer(instance.department).data
        rep['courses'] = CourseSerializer(instance.courses.all(),many=True,).data
        rep['college'] = CollegeSerializer(instance.college).data
        return rep
    depth = 1


    class Meta:
        model = Student
        fields = '__all__'

