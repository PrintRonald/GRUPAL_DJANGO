from django.contrib.auth import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver # decorador que manda una señal por parte del usuario
# esta porción de código permite que cuando un nusuario se registre se cree un perfil para el
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwards):
    if created:
        Profile.objects.create(user=instance)