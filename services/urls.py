from django.urls import path
from . import views

urlpatterns = [
    path('provider/dashboard/', views.provider_dashboard, name='provider_dashboard'),
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),
]
