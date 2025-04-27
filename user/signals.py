from django.contrib.auth.models import User
from .models import Perfil
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User) 
def nuevo_perfil(sender, instance, created, **kwargs): 
    if created:
        Perfil.objects.create(staff=instance)
        
@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()