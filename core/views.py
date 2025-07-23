from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'core/home.html')

# core/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})


def login_view(request):
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
