from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = [
            "name",
            "surname",
            "email",
            "phone"
        ]
    
    name = forms.CharField(max_length=100, required=True, label='Customer name', help_text='Enter your name')
    surname = forms.CharField(max_length=100, required=True, label='Customer surname', help_text='Enter your surname')
    email = forms.EmailField(max_length=254, required=True, label='Customer email', help_text='Enter your email like test@test.com')    
    phone = forms.CharField(max_length=12, required=True, label='Customer phone', help_text='Enter your phone in the format +00000000000')
    
            
        
