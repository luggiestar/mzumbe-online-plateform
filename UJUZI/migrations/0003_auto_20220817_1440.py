# Generated by Django 3.2.9 on 2022-08-17 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UJUZI', '0002_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachingrequest',
            name='status',
            field=models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('DENIED', 'DENIED'), ('PENDING', 'PENDING')], default='PENDING', max_length=100),
        ),
        migrations.AlterField(
            model_name='teachingrequest',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UJUZI.institution'),
        ),
    ]