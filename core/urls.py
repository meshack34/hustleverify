#core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),
    path('provider/dashboard/', views.provider_dashboard, name='provider_dashboard'),
]
