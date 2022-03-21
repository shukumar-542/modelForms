from django.shortcuts import render
from .forms import studentRegistration
from .models import User


# Create your views here.


def showform(request):
      if request.method == 'POST':
            fm = studentRegistration(request.POST)
            if fm.is_valid():
                  nm =fm.cleaned_data['name']
                  em=fm.cleaned_data['email']
                  pas =fm.cleaned_data['password']
                  reg = User(name=nm,email=em, password=pas)
                  reg.save()



                
             
                 
                  return render(request, 'enroll/registration.html',{'form':fm})

      else:
            fm = studentRegistration()
            print('request method')
     
      return render(request, 'enroll/registration.html',{'form':fm})