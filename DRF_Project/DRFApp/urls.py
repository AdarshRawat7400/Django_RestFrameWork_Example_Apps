from django.urls import path,include
from  .views import StudentAPIView,StudentDetailAPIView, StudentGenericAPIView,TeacherViewSet
from DRFApp.routers import router
from rest_framework.authtoken.views import obtain_auth_token
from .auth import CustomAuthToken
urlpatterns = [

    ## Using APIView class based views
    path('student/',StudentAPIView.as_view(),name='student'),
    path('detail/<int:pk>/',StudentDetailAPIView.as_view(),name='student-detail'),    
    path('genericstudent/',StudentGenericAPIView.as_view(),name='student-generic'),
    

    # # Using viewset with routers
    path('viewset/',include(router.urls),name='viewset'),
    path('viewset/<int:pk>/',include(router.urls),name='viewset'),
    # path('gettoken/',obtain_auth_token,name='gettoken'),
    path('gettoken/',CustomAuthToken.as_view(),name='gettoken'),

]