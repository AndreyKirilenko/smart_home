# Generated by Django 4.0.3 on 2022-04-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0013_alter_output_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='type',
            field=models.CharField(choices=[('Реле двухпозиционное, нормально открытое (NO C)', 'Реле NO/C'), ('Реле двухпозиционное, нормально закрытое (NC C)', 'Реле NC/C'), ('Реле трехпозиционное (NC C NO)', 'Реле NC/C/NO'), ('Широтно Импульсная Модуляция (ШИМ)', 'ШИМ'), ('Неизвестно', 'ХЗ')], default='Неизвестно', max_length=50),
        ),
        migrations.AddConstraint(
            model_name='quantityoutput',
            constraint=models.UniqueConstraint(fields=('pin', 'device'), name='unicue_ingredient'),
        ),
    ]
