# services/models.py
from django.db import models
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.city.name}"

from accounts.models import User

SERVICE_CHOICES = [
    ('plumber', 'Plumber'),
    ('electrician', 'Electrician'),
    ('baker', 'Baker'),
    ('cleaner', 'Cleaner'),
]

class Service(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'provider'})
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_service_type_display()} by {self.provider.username} in {self.location}"
from django.db import models
from accounts.models import User, ServiceProviderProfile

class ServiceApplication(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'client'})
    provider = models.ForeignKey(ServiceProviderProfile, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.username} -> {self.provider.full_name}"
