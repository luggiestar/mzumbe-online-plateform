# from django.db import models
# from django.conf import settings
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# class Institution(models.Model):
#     name = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(max_length=50, unique=True)
#
#     class Meta:
#         verbose_name = "Institution"
#         verbose_name_plural = "Institutions"
#
#     def __str__(self):
#         return self.name
