from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profissao = models.CharField(max_length=100)
    namecomplte = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    pais = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Creating profile for user {instance.username}")
        print(f"password profile for user {instance.password}")
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(f"Saving profile for user {instance.username}")
    instance.userprofile.save()