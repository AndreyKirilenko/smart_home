# Generated by Django 4.0.3 on 2022-04-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='image',
            field=models.ImageField(default='default_device.jpg', upload_to='device/image/', verbose_name='Изображение'),
        ),
    ]
