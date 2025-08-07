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

CATEGORY_DATA = {
    'Mechanic': {
        'description': 'Get access to skilled mechanics for car and motorbike repair, routine maintenance, engine diagnostics, battery checks, oil changes, brake systems, and emergency roadside assistance — wherever you are.',
        'icon': 'fa-solid fa-screwdriver-wrench',
        'image': '/static/images/mechanic1.jpeg',
    },
    'Plumber': {
        'description': 'We connect you with reliable plumbers to fix leaking pipes, install taps, unblock drainage systems, repair toilets, and handle all water-related issues — for homes, businesses, or construction sites.',
        'icon': 'fa-solid fa-faucet-drip',
        'image': '/static/images/repair.jpeg',
    },
    'Electrician': {
        'description': 'Hire certified electricians for wiring, socket installations, lighting repairs, power outages, appliance connections, and electrical safety inspections — delivered with expertise and safety compliance.',
        'icon': 'fa-solid fa-bolt',
        'image': '/static/images/Electrician.jpeg',
    },
    'Cleaner': {
        'description': 'Professional cleaners for residential, commercial, and post-construction cleaning. Services include vacuuming, mopping, dusting, deep cleaning, and sanitization — all handled by trusted, background-checked staff.',
        'icon': 'fa-solid fa-broom',
        'image': '/static/images/clenear.jpeg',
    },
    'Baker': {
        'description': 'Order custom cakes, pastries, cookies, and full dessert platters for birthdays, weddings, office events, or everyday cravings — all prepared by certified local bakers using quality ingredients.',
        'icon': 'fa-solid fa-bread-slice',
        'image': '/static/images/Baker.jpeg',
    },
    'Gardener': {
        'description': 'Find experienced gardeners for lawn mowing, landscaping, planting, pruning, pest control, irrigation, and garden maintenance — ideal for homes, offices, and estates of all sizes.',
        'icon': 'fa-solid fa-seedling',
        'image': '/static/images/home.jpeg',
    },
    'Painter': {
        'description': 'Skilled painters for interior and exterior wall painting, wallpaper installation, decorative finishes, and touch-ups. We match you with detail-oriented professionals for both residential and commercial projects.',
        'icon': 'fa-solid fa-paint-roller',
        'image': '/static/images/painter.jpeg',
    },
    'Carpenter': {
        'description': 'Hire expert carpenters for furniture making, custom cabinetry, door/window installations, repairs, and wood finishing. Perfect for home improvement, office upgrades, and construction needs.',
        'icon': 'fa-solid fa-hammer',
        'image': '/static/images/carpenter.jpeg',
    },
    'Tailor': {
        'description': 'Custom tailoring for men, women, and children. Services include alterations, suit/dress making, fittings, curtain stitching, and more — for weddings, workwear, casual, or traditional wear.',
        'icon': 'fa-solid fa-scissors',
        'image': '/static/images/Tailor.jpeg',
    },
    'Mamafua': {
        'description': 'Book experienced mamafua for professional laundry services — washing, ironing, and folding of clothes, bedding, and curtains. Services are available for daily, weekly, or special occasion needs.',
        'icon': 'fa-solid fa-shirt',
        'image': '/static/images/mamafua.jpeg',
    },
    'Mason': {
        'description': 'Certified masons for bricklaying, concrete work, tiling, foundation laying, plastering, and full structural builds. Ideal for both residential and commercial construction projects.',
        'icon': 'fa-solid fa-toolbox',
        'image': '/static/images/mason.jpeg',
    },
    'Chef': {
        'description': 'Hire personal or event chefs for home meals, corporate catering, event menus, and private dinners. From gourmet dishes to local cuisine, our chefs deliver culinary excellence.',
        'icon': 'fa-solid fa-utensils',
        'image': '/static/images/chef.jpeg',
    },
    'Hairdresser': {
        'description': 'Experienced hairdressers for all hair types — offering braiding, cutting, styling, coloring, relaxing, and treatments. Home or salon-based appointments available for men, women, and kids.',
        'icon': 'fa-solid fa-scissors',
        'image': '/static/images/hairdresser.jpeg',
    },
    'Photographer': {
        'description': 'Professional photographers for weddings, birthdays, corporate events, studio shoots, portraits, and branding. Services include editing and delivery of high-resolution, print-ready images.',
        'icon': 'fa-solid fa-camera-retro',
        'image': '/static/images/photographer.jpeg',
    },
    'Tutor': {
        'description': 'Hire qualified tutors for all subjects — from early education to high school and adult learning. Available for in-person or online sessions, including exam prep, homework help, and skill development.',
        'icon': 'fa-solid fa-book-open-reader',
        'image': '/static/images/tutor.jpeg',
    },
    'Home Repairs & Maintenance': {
        'description': 'A wide range of repair services including electrical fixes, plumbing issues, door/window adjustments, appliance installations, and general handyman tasks — all done reliably and safely.',
        'icon': 'fa-solid fa-house-circle-check',
        'image': '/static/images/home_repairs.jpeg',
    },
}


def services_view(request):
    categories = ServiceProviderProfile.objects.values_list('service_category', flat=True).distinct()
    category_data = []

    for cat in categories:
        data = CATEGORY_DATA.get(cat, {})
        category_data.append({
            'name': cat,
            'description': data.get('description', 'Reliable and trusted service providers.'),
            'icon': data.get('icon', 'fa-solid fa-briefcase'),
            'image': data.get('image', '/static/images/default.jpg'),
        })

    context = {
        'categories': category_data
    }
    return render(request, 'services/services.html', context)

from django.shortcuts import render
from accounts.models import ServiceProviderProfile

def providers_by_category(request, category):
    raw_providers = ServiceProviderProfile.objects.filter(service_category=category)
    providers = []

    for provider in raw_providers:
        providers.append({
            'full_name': provider.full_name,
            'email': provider.email,
            'location': provider.location,
            'experience_years': provider.experience_years,
            'availability_days': provider.availability_days.split(',') if provider.availability_days else [],
            'availability_start_time': provider.availability_start_time,
            'availability_end_time': provider.availability_end_time,
            'ratings': provider.ratings,
            'profile_picture': provider.profile_picture,
        })

    return render(request, 'services/providers_by_category.html', {
        'category': category,
        'providers': providers
    })



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

