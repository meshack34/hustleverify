# services/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import ClientProfile, ServiceProviderProfile
from .models import ServiceApplication, Service  # Assuming ServiceApplication model exists
from accounts.models import ServiceProviderProfile

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


from django.shortcuts import render, get_object_or_404
from .models import Service

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services/services_list.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'services/service_detail.html', {'service': service})
from django.shortcuts import render
from accounts.models import ServiceProviderProfile

# services/views.py
from django.shortcuts import render
from accounts.models import ServiceProviderProfile

CATEGORY_DESCRIPTIONS = {
    'Mechanic': 'Expert in vehicle repair and maintenance.',
    'Electrician': 'Certified to handle all your electrical needs.',
    'Cleaner': 'Professional cleaning services for your home or office.',
    'Baker': 'Delicious baked goods for every occasion.',
    # Add more as needed
}

def services_view(request):
    categories = ServiceProviderProfile.objects.values_list('service_category', flat=True).distinct()
    category_data = []

    for cat in categories:
        category_data.append({
            'name': cat,
            'description': CATEGORY_DESCRIPTIONS.get(cat, 'Reliable and trusted service providers.'),
        })

    context = {
        'categories': category_data
    }
    return render(request, 'services/services2.html', context)

def providers_by_category(request, category):
    providers = ServiceProviderProfile.objects.filter(service_category=category, is_verified=True)
    context = {
        'category': category,
        'providers': providers
    }
    return render(request, 'services/providers_by_category.html', context)



def providers_list(request):
    providers = ServiceProviderProfile.objects.select_related('user').all()
    return render(request, 'providers/providers_list.html', {'providers': providers})

def provider_profile(request, provider_id):
    provider = get_object_or_404(ServiceProviderProfile, id=provider_id)
    return render(request, 'providers/provider_profile.html', {'provider': provider})
def about_page(request):
    return render(request, 'core/about.html')

def contact_page(request):
    return render(request, 'core/contact.html')

