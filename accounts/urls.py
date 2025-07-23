from django.urls import path
from . import views

urlpatterns = [
    path('register/client/', views.client_register, name='client_register'),
    path('register/provider/', views.provider_register, name='provider_register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
