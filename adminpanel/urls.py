#adminpanel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('verify-provider/<int:provider_id>/', views.verify_provider, name='verify_provider'),
]
