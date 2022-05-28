# Generated by Django 4.0.3 on 2022-05-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0019_device_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='slug URL'),
        ),
    ]
