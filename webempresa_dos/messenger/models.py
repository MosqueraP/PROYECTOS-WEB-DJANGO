from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['created']



class Thread(models.Model):
    '''
     Thread hilo a los que pertenece, almacena los ususarios y 
     mensajes enviados de los usuarios 
    '''
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)