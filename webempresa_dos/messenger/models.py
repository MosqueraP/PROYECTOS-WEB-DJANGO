from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['created']



class Thread(models.Model):
    '''
     Señal que nadies tenga externo se filtre en 
     la conversacion de dos persosonas, een un hilo
    '''
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)

def messages_chasged(sender, **kwargs):    
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    pk_set =  kwargs.pop('pk_set', None)
    print(instance, action, pk_set) 

    false_pk_set = set()
    if action is 'pre_add':
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print(f'Ups, ({msg.user}) no forma parte del hilo')
                false_pk_set.add(msg_pk) #almacena mensaje fraudulentps

    # Bsucar los enmsaje de false_pk_set que no estan y borralos
    pk_set.difference_update(false_pk_set)

m2m_changed.connect(messages_chasged, sender=Thread.messages.through)