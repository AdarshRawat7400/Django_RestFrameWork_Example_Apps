from operator import ge
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import re
from .models import Student,Teacher,Book
from .serializers import BookSerializer, StudentSerializer,TeacherSerializer,BookSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import (SessionAuthentication,
                                           BasicAuthentication, 
                                           TokenAuthentication)

from rest_framework.permissions import (IsAuthenticated,
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly,
                                        DjangoModelPermissions,
                                        DjangoModelPermissionsOrAnonReadOnly)
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .custom_permissions import MyPermission
from .custom_auth import CustomAuthentication
# Create your views here.




############ Class Based APIViews ##############
class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailAPIView(APIView):
    
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student ,request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


########## ViewSets  #########################

class TeacherViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication]
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]
    # permission_classes = [AllowAny]
    def list(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        queryset = Teacher.objects.all()
        teachers  = get_object_or_404(queryset,pk=pk)
        serializer = TeacherSerializer(teachers)
        return Response(serializer.data)

    def update(self, request, pk = None):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors(status=status.HTTP_400_BAD_REQUEST))
    
    def destroy(self,request, pk = None):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



################## Model ViewSet ###################33

class BookViewSet(viewsets.ModelViewSet):
    serializer_class  = BookSerializer
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [TokenAuthentication]
    # authentication_classes = [CustomAuthentication] # Custom Authentication 
    permission_classes = [IsAuthenticated]
    # permission_classes = [MyPermission]  # custom permission
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]
    # permission_classes = [AllowAny]


    queryset = Book.objects.all()


################## Generic Viewset ########################

class StudentViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    serializer_class  = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [AllowAny]

    queryset = Student.objects.all()




######### Generic Class Based APIViews ####################
class StudentGenericAPIView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class  = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request,id=None):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)

# -------------------------------------------------------------------------#


