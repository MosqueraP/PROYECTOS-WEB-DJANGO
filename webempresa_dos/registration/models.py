from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
RELACION ENTRE MODELOS EN DJANGO:
1. OneToOneField (1:1)  -> un usuarios puede tener un solo peril y un persil puede estar en un solo ususario

2. ForeignKeyField (1:N) 1 autor - N entradas -> un ator puede realizar muchas entradas

3. ManyToManyField (N:M) 1 entradas <-> N entradas -> M muchas categorias -> muchas categorias

'''
class Profile(models.Model):
    '''Relacion de un peril por cada ususario
    ni distintos ususarios para un mismo permil
    relacion uno a ano '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', blank=True, null=True)
    bio = models.TextField(blank=True, null=True, verbose_name= 'Bibiografia')
    link = models.URLField(blank=True, null=True)
    

    class Meta:
        verbose_name = ("perfil")
        verbose_name_plural = ("perfil")

    def __str__(self):
        return self.user
