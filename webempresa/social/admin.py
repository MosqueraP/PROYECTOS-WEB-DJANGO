from django.contrib import admin
from social.models import Link

# Register your models here.

class LinkAmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update') # campos de solo lectura para el admin

admin.site.register(Link, LinkAmin)
