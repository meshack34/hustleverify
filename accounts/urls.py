from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from adminpanel.views import admin_dashboard


urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('register/client/', views.client_register, name='client_register'),

    path('register/provider/', views.provider_register, name='provider_register'),
    path('admin/providers/', views.provider_list, name='provider_list'),
    path('admin/providers/verify/<int:provider_id>/', views.verify_provider, name='verify_provider'),
    path('admin/providers/block/<int:provider_id>/', views.block_provider, name='block_provider'),
    

    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
