from django.contrib import admin
from pages.models import Page

# Register your models here.

class PageAmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update') # campos de solo lectura para el admin

admin.site.register(Page, PageAmin)
