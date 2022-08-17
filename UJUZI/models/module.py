import os

from django.db import models
from django.conf import settings

from .course import *



def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.mkv', '.pdf', '.mp3']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. please upload the video file')


class Module(models.Model):
    title = models.CharField(max_length=90, unique=True)
    content = models.FileField(upload_to='contents/%Y/%m/%d', validators=[validate_file_extension])

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def delete(self, using=None, keep_parents=False):
        self.content.storage.delete(self.content.name)
        super().delete()

    def extension(self):
        name, extension = os.path.splitext(self.content.name)
        return extension

    def __str__(self):
        return self.title
