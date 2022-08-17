
from .institution import *





def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file, make sure the file is in pdf format')


class TeachingRequest(models.Model):
    STATUS = (
        ('ACCEPTED', 'ACCEPTED'),
        ('DENIED', 'DENIED'),
        ('PENDING', 'PENDING'),
    )
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE,  null=True,blank=True)
    letter = models.FileField(upload_to='Requests/%Y/%m/%d', validators=[validate_file_extension])
    status = models.CharField(max_length=100,choices=STATUS, default="PENDING")

    is_verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Teaching Request"
        verbose_name_plural = "Teaching Request"

    def __str__(self):
        return "{0}-{1}".format(self.tutor, self.date)
