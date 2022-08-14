# from django.db import models
# from django.conf import settings
# from .category import *
# from .position import *
# from .institution import *
#
# User = settings.AUTH_USER_MODEL
#
#
# class Staff(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="staff_category")
#     institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
#     position = models.ForeignKey(Position, on_delete=models.CASCADE)
#     is_verified = models.BooleanField(default=False)
#
#     class Meta:
#         unique_together = ('user', 'category', 'institution')
#         verbose_name = "Staff"
#         verbose_name_plural = "Staff"
#
#     def __str__(self):
#         return "{0}-{1}".format(self.user, self.institution)
