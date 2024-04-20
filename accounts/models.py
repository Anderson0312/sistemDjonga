from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    profissao = models.CharField(max_length=100, null=True)
    namecomplte = models.CharField(max_length=100, null=True)
    sexo = models.CharField(max_length=10, null=True)
    pais = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Creating profile for user {instance.username}")
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(f"Saving profile for user {instance.username}")
    instance.userprofile.save()