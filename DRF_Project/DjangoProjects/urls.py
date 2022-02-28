"""DjangoProjects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
from asynchat import simple_producer
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
                                             TokenObtainPairView,
                                             TokenRefreshView,
                                             TokenVerifyView)
from LibraryApp.views import ( SuccessfullyDeletedView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('collegeapi/',include('DRFCollegeApp.urls')),
    path('drf_apis/',include('DRFApp.urls')),
    path('CBV_apis/',include('LibraryApp.urls')),
    path('user_regis/',include('UserRegis.urls')),

    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verifytoken'),
    path('auth',include('rest_framework.urls'), name='rest_framework'),
    path('successfully_deleted/',SuccessfullyDeletedView.as_view(),name='successfully_deleted'),


]
