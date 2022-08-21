import datetime
import os

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.encoding import force_text
from django.contrib.auth import get_user_model

User = get_user_model()


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.mkv', '.pdf', '.mp3']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. please upload the video file')


class Category(models.Model):
    CAT = (
        ('Entrepreneurship', 'Entrepreneurship'),
        ('Law & Legal Aid', 'Law & Legal Aid'),
        ('Technology', 'Technology'),
        ('Economics', 'Economics'),
        ('Business', 'Business'),
        ('Others', 'Others'),
    )

    name = models.CharField(max_length=30, choices=CAT, unique=True)
    icon = models.ImageField("Category Icon", upload_to='CategoryIcon/%Y/%m/%d', null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField("Course Image", upload_to='CourseImages/%Y/%m/%d')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="course_category")
    name = models.CharField(max_length=60, unique=True)
    objective = RichTextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return "{0}-{1}".format(self.name, self.category)


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


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return "{0}-{1}".format(self.student, self.course)


class ContentViewers(models.Model):
    content = models.ForeignKey(Module, on_delete=models.CASCADE)
    viewer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today, editable=False)

    class Meta:
        unique_together = ('content', 'viewer', 'date')
        verbose_name = "Content Viewers"
        verbose_name_plural = "Content Viewers"

    def __str__(self):
        return "{0}".format(self.content)


class TotalContentViewers(models.Model):
    content = models.OneToOneField(Module, on_delete=models.CASCADE, )
    total = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today, editable=False)

    class Meta:
        verbose_name = "Total Content Viewers"
        verbose_name_plural = "Total Content Viewers"

    def __str__(self):
        return "{0}".format(self.content)


class CourseSummary(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, )
    views = models.IntegerField(default=0)
    enrollments = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today, editable=False)

    class Meta:
        verbose_name = "Course Summary"
        verbose_name_plural = "Course Summary"

    def __str__(self):
        return "{0}-{1}".format(self.course,self.enrollments)


class Institution(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"

    def __str__(self):
        return self.name


class TeachingRequest(models.Model):
    STATUS = (
        ('ACCEPTED', 'ACCEPTED'),
        ('DENIED', 'DENIED'),
        ('PENDING', 'PENDING'),
    )
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)
    letter = models.FileField(upload_to='Requests/%Y/%m/%d', validators=[validate_file_extension])
    status = models.CharField(max_length=100, choices=STATUS, default="PENDING")

    is_verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Teaching Request"
        verbose_name_plural = "Teaching Request"

    def __str__(self):
        return "{0}-{1}".format(self.tutor, self.date)
