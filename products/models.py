from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    valor = models.EmailField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
