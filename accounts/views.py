#accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ClientRegisterForm, ProviderRegisterForm
from .models import User

def client_register(request):
    form = ClientRegisterForm()
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'client'
            user.save()
            return redirect('login')
    return render(request, 'accounts/register_client.html', {'form': form})

def provider_register(request):
    form = ProviderRegisterForm()
    if request.method == 'POST':
        form = ProviderRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'provider'
            user.save()
            return redirect('login')
    return render(request, 'accounts/register_provider.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'provider':
                return redirect('provider_dashboard')
            else:
                return redirect('client_dashboard')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
