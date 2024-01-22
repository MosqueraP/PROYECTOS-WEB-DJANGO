from django.contrib import admin
from blog.models import Category, Post

# Register your models here.


class CategoryAmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update') # campos de solo lectura para el admin

class PostAmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update') # campos de solo lectura para el admin
    list_display = ('title', 'author', 'published', 'post_categories', ) 
    ordering=('author', 'published',)
    # campo de busquedas por titulos o contenido, por usuario etc
    search_fields = ('title', 'content', 'author__username', 'categories__name') 
    date_hierarchy = 'published' # filtro de fecha
    # filtra campos en relaciones -> nombre autor, nombre de la categoria
    list_filter = ('author__username', 'categories__name') 

    # funcion encargada de mostras los campos de ralciones en columnas
    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
     # renombrar el cammpo de CATEGORIAS para el ADMIN
    post_categories.short_description = 'Categorias'

admin.site.register(Category, CategoryAmin)
admin.site.register(Post, PostAmin)


