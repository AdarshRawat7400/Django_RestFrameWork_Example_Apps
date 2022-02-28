from django.shortcuts import render
from django.views import View
from .models import Student
from .forms import StudentForm
from django.contrib import messages
# Create your views here.

class StudentRegistrationView(View):
    def get(self,request):
        form = StudentForm()
        return render(request,'userRegis/user_registration.html',{'form':form})

    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Student Registration Successful')
            # messages.success(request,'Student Registration Successful') shortcut way 

            messages.info(request,'Now you can login')
            
            print(messages.get_level(request))
            messages.debug(request,'Debugging message') # will not be shown
            
            messages.set_level(request,messages.DEBUG) # setting the level of messages
            messages.debug(request,'Debugging message') # will  be shown


            return render(request,'userRegis/user_registration.html',{'form':form})
        return render(request,'userRegis/user_registration.html',{'form':form})



class ShowAllMessageView(View):
    def get(self,request):
        messages.set_level(request,messages.DEBUG)
        messages.info(request, "This is a Info message")
        messages.success(request, "This is a Success message")
        messages.warning(request, "This is a Warning message")
        messages.error(request, "This is a Error message")
        messages.debug(request, "This is a Debug message")
        return render(request,'userRegis/test.html')
