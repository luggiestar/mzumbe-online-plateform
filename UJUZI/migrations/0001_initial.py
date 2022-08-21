# Generated by Django 3.2.9 on 2022-08-21 10:10

import UJUZI.models.category
import ckeditor.fields
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Entrepreneurship', 'Entrepreneurship'), ('Law & Legal Aid', 'Law & Legal Aid'), ('Technology', 'Technology'), ('Economics', 'Economics'), ('Business', 'Business'), ('Others', 'Others')], max_length=30, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='CategoryIcon/%Y/%m/%d', verbose_name='Category Icon')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='CourseImages/%Y/%m/%d', verbose_name='Course Image')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('objective', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_category', to='UJUZI.category')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Institution',
                'verbose_name_plural': 'Institutions',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, unique=True)),
                ('content', models.FileField(upload_to='contents/%Y/%m/%d', validators=[UJUZI.models.category.validate_file_extension])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UJUZI.course')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '0.....'. Up to 10 digits allowed.", regex='[6-9][0-9]{8}')])),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_instructor', models.BooleanField(default=False)),
                ('is_verifier', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TotalContentViewers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today, editable=False)),
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UJUZI.module')),
            ],
            options={
                'verbose_name': 'Total Content Viewers',
                'verbose_name_plural': 'Total Content Viewers',
            },
        ),
        migrations.CreateModel(
            name='TeachingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.FileField(upload_to='Requests/%Y/%m/%d', validators=[UJUZI.models.category.validate_file_extension])),
                ('status', models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('DENIED', 'DENIED'), ('PENDING', 'PENDING')], default='PENDING', max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UJUZI.institution')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teaching Request',
                'verbose_name_plural': 'Teaching Request',
            },
        ),
        migrations.AddField(
            model_name='module',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UJUZI.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Enrollment',
                'verbose_name_plural': 'Enrollments',
            },
        ),
        migrations.CreateModel(
            name='CourseSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('enrollments', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today, editable=False)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UJUZI.course')),
            ],
            options={
                'verbose_name': 'Course Summary',
                'verbose_name_plural': 'Course Summary',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ContentViewers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, editable=False)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UJUZI.module')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Content Viewers',
                'verbose_name_plural': 'Content Viewers',
                'unique_together': {('content', 'viewer', 'date')},
            },
        ),
    ]
