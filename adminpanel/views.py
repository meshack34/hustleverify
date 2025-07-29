#adminpanel/views.py

from django.shortcuts import render
from accounts.models import User, ServiceProviderProfile
from services.models import ServiceApplication

def admin_dashboard(request):
    providers = ServiceProviderProfile.objects.all()
    clients = User.objects.filter(role='client')  # FIXED line
    applications = ServiceApplication.objects.all()
    
    context = {
        'providers': providers,
        'clients': clients,
        'applications': applications,
    }
    return render(request, 'adminpanel/dashboard.html', context)
