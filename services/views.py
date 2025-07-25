#services/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import ServiceProviderProfile
from .models import Service

@login_required
def provider_dashboard(request):
    user = request.user

    # Ensure only providers can access this
    if user.role != 'provider':
        return render(request, '403.html')  # or redirect to a different dashboard

    try:
        profile = ServiceProviderProfile.objects.get(user=user)
    except ServiceProviderProfile.DoesNotExist:
        profile = None

    services = Service.objects.filter(provider=user)

    return render(request, 'services/provider_dashboard.html', {
        'profile': profile,
        'services': services
    })


@login_required
def client_dashboard(request):
    return render(request, 'services/client_dashboard.html')
