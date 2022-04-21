# Generated by Django 4.0.3 on 2022-04-18 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_house_land_alter_land_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='size',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='', validators=[django.core.validators.MinValueValidator(0, 'Минимальное значение 0')], verbose_name='Размер участка в сотках'),
        ),
    ]