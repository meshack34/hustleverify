from django.contrib import admin
from .models import City, Location, Service

admin.site.register(City)
admin.site.register(Location)
admin.site.register(Service)
from django.contrib import admin
from .models import ServiceApplication

admin.site.register(ServiceApplication)

