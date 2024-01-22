from django.contrib import admin
from services.models import Service

# Register your models here.


class ServiceAmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update') # campos de solo lectura para el admin

admin.site.register(Service, ServiceAmin)
