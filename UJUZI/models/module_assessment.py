# from django.db import models
# from django.conf import settings
#
# from .staff import *
# from .question import *
# from .enrollment import *
# from .module import *
#
# User = settings.AUTH_USER_MODEL
#
#
# class ModuleAssessment(models.Model):
#     enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.TextField(max_length=500)
#     assessor = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)
#     grade = models.IntegerField(null=True, blank=True)
#
#     class Meta:
#         verbose_name = "Module Assessment"
#         verbose_name_plural = "Module Assessment"
#
#     def __str__(self):
#         return "{0}-{1}".format(self.enrollment, self.module)
