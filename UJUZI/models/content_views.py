import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from ..models import Module

User = get_user_model()


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
