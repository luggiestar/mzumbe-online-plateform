# Generated by Django 3.2.9 on 2022-08-17 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UJUZI', '0003_auto_20220817_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_tutor',
        ),
    ]