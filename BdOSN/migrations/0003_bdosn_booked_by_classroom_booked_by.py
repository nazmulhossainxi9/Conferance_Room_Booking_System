# Generated by Django 4.1.7 on 2024-10-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BdOSN', '0002_maslab_booked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='bdosn',
            name='booked_by',
            field=models.CharField(default='not specified', max_length=100),
        ),
        migrations.AddField(
            model_name='classroom',
            name='booked_by',
            field=models.CharField(default='not specified', max_length=100),
        ),
    ]