# Generated by Django 4.0.3 on 2022-04-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0014_alter_output_type_quantityoutput_unicue_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='type',
            field=models.CharField(choices=[('Реле (NO C)', 'Реле NO/C'), ('Реле (NC C)', 'Реле NC/C'), ('Реле (NC C NO)', 'Реле NC/C/NO'), ('ШИМ выход', 'ШИМ'), ('Неизвестно', 'ХЗ')], default='Неизвестно', max_length=50),
        ),
    ]
