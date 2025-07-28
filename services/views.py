#services/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import ServiceProviderProfile
from .models import Service
from accounts.models import ClientProfile
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




# services/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import ServiceProviderProfile
from .forms import ServiceFilterForm
# services/views.py
from django.shortcuts import render
from accounts.models import ServiceProviderProfile
from django.contrib.auth.decorators import login_required
from accounts.models import ServiceProviderProfile

# Get the specific provider


from django.shortcuts import render
from accounts.models import ClientProfile, ServiceProviderProfile
from django.contrib.auth.decorators import login_required

@login_required
def client_dashboard(request):
    client_profile = ClientProfile.objects.get(user=request.user)
    providers = None
    selected_service = None

    if request.method == 'POST':
        selected_service = request.POST.get('service')
        providers = ServiceProviderProfile.objects.filter(service_category__icontains=selected_service, is_verified=True)

    all_services = ServiceProviderProfile.objects.values_list('service_category', flat=True).distinct()

    return render(request, 'services/client_dashboard.html', {
        'client': client_profile,
        'providers': providers,
        'services': all_services,
        'selected_service': selected_service,
    })

# services/views.py
from django.shortcuts import render
from accounts.models import ServiceProviderProfile
from django.contrib.auth.decorators import login_required

@login_required
def find_service_provider(request):
    query = request.GET.get('service_type')  # From form input
    provider = ServiceProviderProfile.objects.get(service_category__icontains='mechanic')
    # Mark as verified
    provider.is_verified = True
    provider.save()


    providers = None

    if query:
        providers = ServiceProviderProfile.objects.filter(
            service_category__icontains=query,
            is_verified=True  # Only verified providers
        )

    return render(request, 'services/find_service_provider.html', {
        'providers': providers,
        'query': query
    })





# @login_required
# def client_dashboard(request):
#     form = ServiceFilterForm(request.GET or None)
#     providers = []

#     if form.is_valid():
#         service = form.cleaned_data.get('service_category')
#         if service:
#             providers = ServiceProviderProfile.objects.filter(service_category__iexact=service, is_verified=True)

#     client_profile = request.user.clientprofile

#     return render(request, 'core/client_dashboard.html', {
#         'form': form,
#         'providers': providers,
#         'client_profile': client_profile
#     })

# from django import forms
# from .models import Service, Location

# class ServiceFilterForm(forms.Form):
#     service_type = forms.ChoiceField(
#         choices=[('', 'All Services')] + list(Service._meta.get_field('service_type').choices),
#         required=False,
#         label="Service Type"
#     )
#     location = forms.ModelChoiceField(
#         queryset=Location.objects.all(),
#         required=False,
#         label="Location"
#     )


# from .forms import ServiceFilterForm

# def client_dashboard(request):
#     client_profile = ClientProfile.objects.get(user=request.user)
#     services = Service.objects.filter(available=True)
#     form = ServiceFilterForm(request.GET or None)

#     if form.is_valid():
#         service_type = form.cleaned_data.get('service_type')
#         location = form.cleaned_data.get('location')

#         if service_type:
#             services = services.filter(service_type=service_type)
#         if location:
#             services = services.filter(location=location)

#     context = {
#         'client_profile': client_profile,
#         'services': services,
#         'form': form,
#     }
#     return render(request, 'client_dashboard.html', context)


# services/views.py
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from accounts.models import ServiceProviderProfile, ClientProfile
# from .models import Service
# from .forms import ServiceFilterForm

# @login_required
# def client_dashboard(request):
#     user = request.user

#     # Ensure it's a client
#     if user.role != 'client':
#         return render(request, '403.html')

#     try:
#         profile = ClientProfile.objects.get(user=user)
#     except ClientProfile.DoesNotExist:
#         profile = None

#     form = ServiceFilterForm(request.GET or None)
#     filtered_services = None

#     if form.is_valid():
#         service_type = form.cleaned_data.get('service_type')
#         city = form.cleaned_data.get('city')
#         location = form.cleaned_data.get('location')

#         filtered_services = Service.objects.filter(
#             service_type=service_type,
#             city=city
#         )
#         if location:
#             filtered_services = filtered_services.filter(location=location)

#     return render(request, 'services/client_dashboard.html', {
#         'profile': profile,
#         'form': form,
#         'services': filtered_services
#     })


# @login_required
# def client_dashboard(request):
#     user = request.user
#     if user.role != 'client':
#         return render(request, '403.html')

#     profile = ClientProfile.objects.filter(user=user).first()
#     form = ServiceFilterForm(request.GET or None)

#     services = Service.objects.filter(available=True)
#     if form.is_valid() and form.cleaned_data.get('service_type'):
#         services = services.filter(service_type=form.cleaned_data['service_type'])

#     return render(request, 'core/client_dashboard.html', {
#         'profile': profile,
#         'services': services,
#         'form': form
#     })





# services/views.py
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from accounts.models import ServiceProviderProfile, ClientProfile
# from .models import Service
# from .forms import ServiceFilterForm

# @login_required
# def client_dashboard(request):
#     user = request.user

#     # Ensure it's a client
#     if user.role != 'client':
#         return render(request, '403.html')

#     try:
#         profile = ClientProfile.objects.get(user=user)
#     except ClientProfile.DoesNotExist:
#         profile = None

#     form = ServiceFilterForm(request.GET or None)
#     filtered_services = None

#     if form.is_valid():
#         service_type = form.cleaned_data.get('service_type')
#         city = form.cleaned_data.get('city')
#         location = form.cleaned_data.get('location')

#         filtered_services = Service.objects.filter(
#             service_type=service_type,
#             city=city
#         )
#         if location:
#             filtered_services = filtered_services.filter(location=location)

#     return render(request, 'services/client_dashboard.html', {
#         'profile': profile,
#         'form': form,
#         'services': filtered_services
#     })
