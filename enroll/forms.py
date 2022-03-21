from dataclasses import fields
from logging import PlaceHolder
from tkinter import Widget
from django.core import validators
from django import forms
from .models import User

class studentRegistration(forms.ModelForm):
      class Meta:
            model = User
            fields = [ 'name','email','password']

            labels ={'name': 'Enter Your Name', 'email':'Enter Your Email','password':'Enter Your password'}

            error_messages ={'name':{'required':'Name must be required'},
            'email':{'required':'email must be required'}
            }
            widgets = {'password':forms.PasswordInput(attrs={'placeholder':'Password'}),
            'name': forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Your name'})
            }

    

     
   