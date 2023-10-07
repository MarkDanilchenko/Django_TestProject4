from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
