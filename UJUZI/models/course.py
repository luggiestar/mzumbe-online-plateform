import datetime

from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.utils.encoding import force_text

from .staff import *
from .category import *
from .institution import *



#
class CourseManager(models.Manager):
    def as_choices(self):
        for course in self.all():
            yield course.pk, force_text(course)


class Course(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField("Course Image",upload_to='CourseImages/%Y/%m/%d')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="course_category")
    name = models.CharField(max_length=60, unique=True)
    objective = RichTextField(null=True, blank=True)

    objects = CourseManager()

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return "{0}-{1}".format(self.name, self.category)



class TotalContentViewers(models.Model):
    content = models.OneToOneField('Module', on_delete=models.CASCADE,)
    total = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today, editable=False)

    class Meta:
        verbose_name = "Total Content Viewers"
        verbose_name_plural = "Total Content Viewers"

    def __str__(self):
        return self.content