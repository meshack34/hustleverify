from django.urls import path
from . import views

urlpatterns = [
    path('provider/dashboard/', views.provider_dashboard, name='provider_dashboard'),
    # path('service/edit/<int:pk>/', views.edit_service, name='edit_service'),
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),
]