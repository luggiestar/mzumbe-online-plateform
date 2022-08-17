from django.db import models
from django.db.models import Q
import select2.fields
import select2.models
from django.conf import settings
from six import python_2_unicode_compatible




class Category(models.Model):
    CAT = (
        ('Entrepreneurship', 'Entrepreneurship'),
        ('Law & Legal Aid', 'Law & Legal Aid'),
        ('Technology', 'Technology'),
        ('Economics', 'Economics'),
        ('Business', 'Business'),
        ('Others', 'Others'),
    )

    name = models.CharField(max_length=30,choices=CAT, unique=True)
    icon = models.ImageField("Category Icon",upload_to='CategoryIcon/%Y/%m/%d',null=True,blank=True)

    class Meta:
        ordering=('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     active = models.BooleanField()


# class Entry(models.Model):
#     author = select2.fields.ForeignKey(Author,
#                                        limit_choices_to=models.Q(active=True),
#                                        ajax=True,
#                                        search_field='name',
#                                        overlay="Choose an author...",
#                                        js_options={
#                                            'quiet_millis': 20,
#                                        },
#                                        on_delete=models.CASCADE)
