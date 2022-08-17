import datetime
from django.db import models
from django.conf import settings

from ..models import Module

User = settings.AUTH_USER_MODEL


class ContentViewers(models.Model):
    content = models.ForeignKey(Module, on_delete=models.CASCADE)
    viewer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today, editable=False)

    class Meta:
        unique_together = ('content', 'viewer', 'date')
        verbose_name = "Content Viewers"
        verbose_name_plural = "Content Viewers"

    def __str__(self):
        return self.content


class TotalContentViewers(models.Model):
    content = models.ForeignKey(Module, on_delete=models.CASCADE, unique=True)
    total = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today, editable=False)

    class Meta:
        unique_together = ('content', 'viewer', 'date')
        verbose_name = "Total Content Viewers"
        verbose_name_plural = "Total Content Viewers"

    def __str__(self):
        return self.content
