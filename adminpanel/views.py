#adminpanel/views.py

from django.shortcuts import render
from accounts.models import User, ServiceProviderProfile
from services.models import ServiceApplication
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from accounts.models import User, ServiceProviderProfile
from services.models import ServiceApplication


def is_admin(user):
    return user.is_authenticated and user.is_staff  # Restrict to staff/admin


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
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

# Existing imports...

@login_required
@user_passes_test(is_admin)
def verify_provider(request, provider_id):
    provider = get_object_or_404(ServiceProviderProfile, id=provider_id)

    if request.method == 'POST':
        provider.is_verified = True
        provider.save()
        messages.success(request, f"{provider.full_name} has been verified.")
    
    return redirect('admin_dashboard')
