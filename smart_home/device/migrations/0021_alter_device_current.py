# Generated by Django 4.0.3 on 2022-05-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0020_alter_device_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='current',
            field=models.FloatField(default=0, verbose_name='Потребление тока Вт'),
        ),
    ]