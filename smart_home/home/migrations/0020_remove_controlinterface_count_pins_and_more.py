# Generated by Django 4.0.3 on 2022-05-03 19:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_quantityinterface_unicue_equipment_interface'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlinterface',
            name='count_pins',
        ),
        migrations.AlterField(
            model_name='quantityinterface',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1, 'Минимальное значение 1')], verbose_name='Количество'),
        ),
    ]
