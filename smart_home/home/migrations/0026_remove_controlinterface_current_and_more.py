# Generated by Django 4.0.3 on 2022-05-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_remove_equipment_start_current_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlinterface',
            name='current',
        ),
        migrations.AlterField(
            model_name='controlinterface',
            name='start_current',
            field=models.IntegerField(default=0, help_text='Зависит от типа устройства Iстартовый=Iноминал*Множитель,             </br> Лампы накаливания I=Inom * 10,             </br> Светодиодные "хорошие" I=Inom * 20,             </br> Светодиодные "плохие" I=Inom * 200,             </br> Электродвигатели I=Inom * 5,             </br> Импульсные блоки питания  I=Inom * 600,', verbose_name='Множитель стартового тока'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='voltage',
            field=models.IntegerField(default=0, verbose_name='Напряжение питания.'),
        ),
    ]
