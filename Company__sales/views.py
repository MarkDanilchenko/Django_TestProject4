from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from . import forms


def registration(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'registration/registration.html', {'form': form})
