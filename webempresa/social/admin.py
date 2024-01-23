from django.contrib import admin
from social.models import Link

# Register your models here.

class LinkAmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update') # campos de solo lectura para el admin

    # proteccion de campos
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():

            # return ('created', 'update', 'key', 'name') 
            # no mostrar los campos de fecha de creacion ni actualizacion a los
            # usuarios del grupo Personal
            return ('key', 'name')
        else:
            return('created', 'update')

admin.site.register(Link, LinkAmin)
