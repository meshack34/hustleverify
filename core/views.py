#core/views.py
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'core/dashboard.html')



@login_required
def provider_dashboard(request):
    return render(request, 'core/provider_dashboard.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import ClientProfile, ServiceProviderProfile
from django.db.models import Q

@login_required
def client_dashboard(request):
    user = request.user
    client = ClientProfile.objects.get(user=user)

    # Filters from query params
    location_filter = request.GET.get('location')
    category_filter = request.GET.get('category')

    # Base queryset for verified providers
    providers = ServiceProviderProfile.objects.filter(is_verified=True)

    # Apply filters if any
    if location_filter:
        providers = providers.filter(location__iexact=location_filter)
    if category_filter:
        providers = providers.filter(service_category__iexact=category_filter)

    # Unique options for filters
    available_locations = ServiceProviderProfile.objects.values_list('location', flat=True).distinct()
    available_categories = ServiceProviderProfile.objects.values_list('service_category', flat=True).distinct()

    return render(request, 'core/client_dashboard.html', {
        'client': client,
        'providers': providers,
        'locations': available_locations,
        'categories': available_categories,
        'selected_location': location_filter,
        'selected_category': category_filter
    })
