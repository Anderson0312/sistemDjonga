from django.db import models

class custommer(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100, null=True)
    sexo = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=50, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"