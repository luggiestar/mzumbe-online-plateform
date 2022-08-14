# import random
# import string
#
# from django.db import models
# from django.conf import settings
#
# User = settings.AUTH_USER_MODEL
#
#
# def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
#
#
# class Student(models.Model):
#     code = models.CharField(max_length=8, blank=False, null=False, unique=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def save(self, *args, **kwargs):
#         self.code = id_generator()
#
#         return super(Student, self).save(*args, **kwargs)
#
#     class Meta:
#         verbose_name = "Student"
#         verbose_name_plural = "Students"
#
#     def __str__(self):
#         return self.code
