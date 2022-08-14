# from django.db import models
# from django.conf import settings
# from .enrollment import *
# from .module import *
#
# User = settings.AUTH_USER_MODEL
#
#
# class ModuleTracking(models.Model):
#     enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)
#     start = models.DateTimeField(auto_now_add=True)
#     end = models.DateTimeField(blank=True)
#     is_complete = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name = "Module Tracking"
#         verbose_name_plural = "Module Tracking"
#
#     def __str__(self):
#         return "{0}-{1}".format(self.enrollment, self.module)
