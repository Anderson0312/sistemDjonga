from django.utils import timezone
from django.db import models

class partners(models.Model):
    name_empresa = models.CharField(max_length=100)
    pathbase = models.CharField(max_length=200)
    is_active = models.BooleanField(
        ("active"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_cadastro = models.DateTimeField(("date joined"), default=timezone.now)