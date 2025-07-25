# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ClientRegisterForm, ProviderRegisterForm
from .models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from .models import User

def client_register(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'client'
            user.save()
            return redirect('login')
    else:
        form = ClientRegisterForm()
    return render(request, 'accounts/register_client.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import ProviderRegisterForm

def provider_register(request):
    if request.method == 'POST':
        form = ProviderRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)  # for debugging
    else:
        form = ProviderRegisterForm()
    return render(request, 'accounts/register_provider.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
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




def is_admin(user):
    return user.is_authenticated and user.is_admin()

@login_required
@user_passes_test(is_admin)
def provider_list(request):
    providers = User.objects.filter(role='provider')
    return render(request, 'admin_provider_list.html', {'providers': providers})

@login_required
@user_passes_test(is_admin)
def verify_provider(request, provider_id):
    provider = get_object_or_404(User, id=provider_id, role='provider')
    provider.is_verified = True
    provider.save()
    return redirect('provider_list')

@login_required
@user_passes_test(is_admin)
def block_provider(request, provider_id):
    provider = get_object_or_404(User, id=provider_id, role='provider')
    provider.is_blocked = True
    provider.save()
    return redirect('provider_list')