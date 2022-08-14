# from django.db import models
# from django.conf import settings
#
# User = settings.AUTH_USER_MODEL
#
#
# class Status(models.Model):
#
#     name = models.CharField(max_length=30, unique=True)
#     code = models.CharField(max_length=5, unique=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "Status"
#         verbose_name_plural = "Status"
#
#     def __str__(self):
#         return self.name
