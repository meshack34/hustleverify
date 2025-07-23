#accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class ClientRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProviderRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
