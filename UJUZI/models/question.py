# from django.db import models
# from django.conf import settings
#
# from .course import *
# from .module import *
#
# User = settings.AUTH_USER_MODEL
#
#
# class Question(models.Model):
#     name = models.FileField(max_length=90, unique=True)
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)
#     weight = models.IntegerField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "Question"
#         verbose_name_plural = "Questions"
#
#     def __str__(self):
#         return "{0}".format(self.module)
