
from .models import User
from django.contrib import admin
from .models import User, ServiceProviderProfile

admin.site.register(User)
admin.site.register(ServiceProviderProfile)

