from django.urls import path
from UserRegis import views
urlpatterns = [
path('registration/', views.StudentRegistrationView.as_view(), name='stu_registration'),
path('all_tags/', views.ShowAllMessageView.as_view(), name='all_msg_tags'),

]
    

