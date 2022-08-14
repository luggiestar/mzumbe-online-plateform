# from django.db import models
# from django.conf import settings
#
# User = settings.AUTH_USER_MODEL
#
#
# class Position(models.Model):
#     name = models.CharField(max_length=30, unique=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "Position"
#         verbose_name_plural = "Positions"
#
#     def __str__(self):
#         return self.name
