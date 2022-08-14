from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Institution(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"

    def __str__(self):
        return self.name
