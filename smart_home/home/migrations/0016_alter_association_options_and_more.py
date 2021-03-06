# Generated by Django 4.0.3 on 2022-05-01 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_association'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='association',
            options={'verbose_name': 'Ассоциация интерфейсов', 'verbose_name_plural': 'Ассоциации интерфейсов'},
        ),
        migrations.AlterField(
            model_name='association',
            name='equipment_interface',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='associstions', to='home.controlinterface', verbose_name='Интерфейс оборудования'),
        ),
        migrations.AddConstraint(
            model_name='association',
            constraint=models.UniqueConstraint(fields=('equipment_interface', 'device_input', 'device_output', 'device_interface'), name='add_favorite'),
        ),
    ]
