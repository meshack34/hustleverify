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
]

