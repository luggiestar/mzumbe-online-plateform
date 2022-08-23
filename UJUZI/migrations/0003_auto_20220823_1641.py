# Generated by Django 3.2.9 on 2022-08-23 13:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UJUZI', '0002_alter_module_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='uploaded_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 8, 23, 13, 41, 16, 281846, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='uploaded_time',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2022, 8, 23, 13, 41, 30, 805516, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
