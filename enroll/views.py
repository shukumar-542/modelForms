from django.shortcuts import render
from .forms import studentRegistration


# Create your views here.


def showform(request):
      if request.method == 'POST':
            fm = studentRegistration(request.POST)
            if fm.is_valid():
                  nm =fm.cleaned_data['name']
                  em=fm.cleaned_data['email']
                  pas =fm.cleaned_data['password']
                  print(nm)
                  print(em)
                  print(pas)


                
             
                 
                  return render(request, 'enroll/registration.html',{'form':fm})

      else:
            fm = studentRegistration()
            print('request method')
     
      return render(request, 'enroll/registration.html',{'form':fm})