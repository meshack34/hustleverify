# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('provider', 'Service Provider'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class ServiceProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Basic Info
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=50)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # ID Verification
    id_number = models.CharField(max_length=20)
    id_image = models.ImageField(upload_to='id_images/', null=True, blank=True)

    # Service Details
    service_category = models.CharField(max_length=100)
    availability_days = models.CharField(max_length=200)  # e.g., "Monday,Wednesday,Friday"
    availability_start_time = models.TimeField()
    availability_end_time = models.TimeField()
    experience_years = models.IntegerField()
    certifications = models.FileField(upload_to='certifications/', null=True, blank=True)

    # Next of Kin
    next_of_kin_full_name = models.CharField(max_length=100)
    next_of_kin_relationship = models.CharField(max_length=50)
    next_of_kin_phone = models.CharField(max_length=15)
    
    

    # Status
    ratings = models.FloatField(default=0.0)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
