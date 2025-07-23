from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def provider_dashboard(request):
    return render(request, 'services/provider_dashboard.html')

@login_required
def client_dashboard(request):
    return render(request, 'services/client_dashboard.html')
