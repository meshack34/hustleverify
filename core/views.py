#core/views.py
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'core/dashboard.html')


@login_required
def client_dashboard(request):
    return render(request, 'core/client_dashboard.html')

@login_required
def provider_dashboard(request):
    return render(request, 'core/provider_dashboard.html')
