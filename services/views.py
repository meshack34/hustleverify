# services/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import ClientProfile, ServiceProviderProfile
from .models import ServiceApplication, Service  # Assuming ServiceApplication model exists

# -------------------------------
# Provider Dashboard
# -------------------------------
@login_required
def provider_dashboard(request):
    if request.user.role != 'provider':
        return render(request, '403.html')

    try:
        profile = ServiceProviderProfile.objects.get(user=request.user)
    except ServiceProviderProfile.DoesNotExist:
        profile = None

    services = Service.objects.filter(provider=request.user)

    return render(request, 'services/provider_dashboard.html', {
        'profile': profile,
        'services': services
    })


# -------------------------------
# Client Dashboard
# -------------------------------
@login_required
def client_dashboard(request):
    client_profile = ClientProfile.objects.get(user=request.user)
    providers = None
    selected_service = None

    if request.method == 'POST':
        selected_service = request.POST.get('service')
        providers = ServiceProviderProfile.objects.filter(
            service_category__icontains=selected_service,
            is_verified=True
        )

    all_services = ServiceProviderProfile.objects.values_list('service_category', flat=True).distinct()

    return render(request, 'services/client_dashboard.html', {
        'client': client_profile,
        'providers': providers,
        'services': all_services,
        'selected_service': selected_service,
    })


# -------------------------------
# Apply for Service
# -------------------------------
@login_required
def apply_for_service(request, provider_id):
    if request.user.role != 'client':
        messages.error(request, "Only clients can apply for services.")
        return redirect('home')

    provider = get_object_or_404(ServiceProviderProfile, id=provider_id)

    if request.method == 'POST':
        message = request.POST.get('message')

        # Prevent duplicate applications
        if ServiceApplication.objects.filter(client=request.user, provider=provider).exists():
            messages.warning(request, "You have already applied for this service.")
            return redirect('client_dashboard')

        ServiceApplication.objects.create(
            client=request.user,
            provider=provider,
            message=message
        )
        messages.success(request, f"You have successfully applied for service from {provider.full_name}.")
        return redirect('client_dashboard')

    return render(request, 'services/apply_form.html', {'provider': provider})


# -------------------------------
# (Optional) Search Provider View
# -------------------------------
@login_required
def find_service_provider(request):
    query = request.GET.get('service_type')
    providers = None

    if query:
        providers = ServiceProviderProfile.objects.filter(
            service_category__icontains=query,
            is_verified=True
        )

    return render(request, 'services/find_service_provider.html', {
        'providers': providers,
        'query': query
    })
