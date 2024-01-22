from django.contrib import admin
from blog.models import Category, Post

# Register your models here.


class CategoryAmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update') # campos de solo lectura para el admin

class PostAmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update') # campos de solo lectura para el admin

admin.site.register(Category, CategoryAmin)
admin.site.register(Post, PostAmin)


