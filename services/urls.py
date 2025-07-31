from django.urls import path
from . import views
from django.urls import path
from services import views as service_views
from django.urls import path
from .views import find_service_provider

urlpatterns = [
    path('provider/dashboard/', views.provider_dashboard, name='provider_dashboard'),
    # path('service/edit/<int:pk>/', views.edit_service, name='edit_service'),
    # path('client/dashboard/', views.client_dashboard, name='client_dashboard'),
    path('client/dashboard/', service_views.client_dashboard, name='client_dashboard'),
    # services/urls.py
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),
    path('client/find-providers/', views.find_service_provider, name='find_service_provider'),
    path('find/', find_service_provider, name='find_service_provider'),
    path('apply/<int:provider_id>/', views.apply_for_service, name='apply_for_service'),
    
    path('services/', views.services_view, name='services'),
    path('providers/<str:category>/', views.providers_by_category, name='providers_by_category'),
    
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('providers/', views.providers_list, name='providers'),
    path('providers/<int:provider_id>/', views.provider_profile, name='provider_profile'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
]

