from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student,Department,Course,College
from .serializers import (StudentSerializer,DepartmentSerializer,
                          CourseSerializer,CollegeSerializer)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

                          

# Create your views here.

class CollegeStudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()


class DepartmentViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    serializer_class = DepartmentSerializer
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    serializer_class = CourseSerializer
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [SessionAuthentication]

    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()


class CollegeViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    serializer_class = CollegeSerializer
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = College.objects.all()
