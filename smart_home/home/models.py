import imp
from django.db import models
from django.contrib.auth import get_user_model
from device.models import SmartSystem
from django.core.validators import MinValueValidator
from device.models import Input, Output, Interface

User = get_user_model()



class Location(models.Model):
    """Место установки"""
    name = models.CharField(max_length=100, verbose_name='Наименование места устанвки', unique=True)
    description = models.TextField(max_length=200, verbose_name='Описание места устанвки', null=True, blank=True)

    class Meta:
        verbose_name = 'Место установки'
        verbose_name_plural = 'Места установки'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Какой то тег"""
    name = models.CharField(max_length=100, verbose_name='Тег', unique=True)
    color = models.CharField(max_length=7, verbose_name='Цвет в HEX')
    slug = models.SlugField(max_length=200, verbose_name='Уникальный слаг', unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name




class Land(models.Model):
    """Дом на участке"""
    image = models.ImageField(verbose_name='Изображение', upload_to='home/image/', help_text='Изображение для участка (Необязательно)', default='home/image/2270995_2x.jpg', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Название', unique=True, help_text='Обязательно',)
    description = models.TextField(max_length=200, verbose_name='Описание', null=True, blank=True, help_text='Не обязательно')
    size = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        validators=[MinValueValidator(0, 'Минимальное значение 0')],
        verbose_name='Размер участка в сотках',
        help_text='Не обязательно'
    )
    address = models.CharField(max_length=150, help_text='Укажите местонахождение земельного уастка', verbose_name='Место нахождения', default="Местонахождение не указано")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='houses',  help_text='Обязательно')
    date_create = models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата создания',)
    
    class Meta:
        verbose_name = 'Земельный уасток'
        verbose_name_plural = 'Земельные уастки'
        ordering = ['name']

    def __str__(self):
        return self.name


class Building(models.Model):
    """Сооружение"""
    image = models.ImageField(verbose_name='Изображение', upload_to='home/image/', help_text='Изображение для дома (Необязательно)', default='home/image/smart_home.jpg')
    name = models.CharField(max_length=100, verbose_name='Название сооружения')
    description = models.TextField(max_length=200, verbose_name='Описание сооружения',  null=True, blank=True, help_text='Не обязательно')
    floor = models.IntegerField(default=1, verbose_name='Количество этажей включая подвал')
    land = models.ForeignKey(Land, on_delete=models.CASCADE, verbose_name='Земельный участок', related_name='buildings')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='buildings')
    
    class Meta:
        verbose_name = 'Сооружение'
        verbose_name_plural = 'Сооружения'
        ordering = ['name']

    def __str__(self):
        return self.name


class Room(models.Model):
    """Помещение"""
    name = models.CharField(max_length=100, verbose_name='Название комнаты')
    description = models.TextField(max_length=200, verbose_name='Описание комнаты',  null=True, blank=True, help_text='Не обязательно')
    floor = models.IntegerField(default=1, verbose_name='На каком этаже находится')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='Строение', related_name='rooms')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')


    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
        ordering = ['name']

    def __str__(self):
        return self.name

class ControlInterface(models.Model):
    """Что нужно для управления"""
    name = models.CharField(max_length=100, verbose_name='Наименование входа/выхода/интерфейса', unique=True)
    description = models.TextField(max_length=200, verbose_name='Описание входа/выхода/интерфейса', null=True, blank=True)
    voltage = models.IntegerField(default=0, verbose_name='Управляющее напряжение.', help_text='Если для управления не требуется подавать напряжение - оставте 0')
    # current = models.IntegerField(default=0, verbose_name='Мощность Вт')
    start_current = models.IntegerField(
        default=0,
        verbose_name='Множитель стартового тока',
        help_text=(
            'Зависит от типа устройства Iстартовый=Iноминал*Множитель, \
            </br> Лампы накаливания I=Inom * 10, \
            </br> Светодиодные "хорошие" I=Inom * 20, \
            </br> Светодиодные "плохие" I=Inom * 200, \
            </br> Электродвигатели I=Inom * 5, \
            </br> Импульсные блоки питания  I=Inom * 600,'
            )
        )
    image = models.ImageField(verbose_name='Изображение', upload_to='home/image/', help_text='Схема (Необязательно)', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='control_interfaces')

    class Meta:
        verbose_name = 'Интерфейс ОБОРУДОВАНИЯ'
        verbose_name_plural = 'Интерфейсы ОБОРУДОВАНИЯ'
        ordering = ['name']

    def __str__(self):
        return self.name


class Equipment(models.Model):
    """Оборудование которое нужно автоматизировать"""
    SENSOR = 'Сенсор/датчик'
    SEN_PARAMETER = 'Контролируемый параметр'
    EQUIPMENT = 'Управляемое устройство'
    S_EQUIPMENT = 'Управляемое устройство с обратной связью'

    TYPE_OF_EQUIPMENT = [
        (SENSOR, 'Сенсор/датчик'),
        (SEN_PARAMETER, 'Контролируемый параметр'),
        (EQUIPMENT, 'Управляемое устройство'),
        (S_EQUIPMENT, 'Управляемое устройство с обратной связью'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_OF_EQUIPMENT, default=EQUIPMENT)
    name = models.CharField(max_length=100, verbose_name='Общее название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug URL")
    model = models.CharField(max_length=150, verbose_name='Марка и модель оборудования', null=True, blank=True)
    description = models.TextField(max_length=200, verbose_name='Подраобное описание', null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='equipments', verbose_name='Помещение в котором установлено')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True, related_name='equipments', verbose_name='Здание в котором установлено')
    land = models.ForeignKey(Land, on_delete=models.CASCADE, null=True, blank=True, related_name='equipments', verbose_name='Земельный уасток где установлено')
    specific = models.ManyToManyField(SmartSystem, blank=True, related_name='equipments', verbose_name='К какой системе относится')
    location = models.ManyToManyField(Location, blank=True, related_name='equipments', verbose_name='Места возможной установки')
    tag = models.ManyToManyField(Tag, blank=True, related_name='equipments', verbose_name='Теги')
    voltage = models.IntegerField(default=0, verbose_name='Напряжение питания.')
    current = models.IntegerField(default=0, verbose_name='Потребление тока Вт', help_text='Если группа потребителей - указать общее потребление </br> Например группа ламп освещения каждая по 95Вт, 5 шт, = 475Вт' )
    # start_current = models.IntegerField(default=0, null=True, blank=True, verbose_name='Стартовый ток', help_text='Зависит от типа устройства </br> Лампы накаливания I=Inom*10, </br> Светодиодные "хорошие" I=Inom*20',)
    control = models.ManyToManyField(
        ControlInterface,
        blank=True,
        related_name='equipments',
        verbose_name='Интерфейс управления',
        through='QuantityInterface',
        through_fields=('equipment', 'interface',)
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='equipments')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ['name']

    def __str__(self):
        return self.name


class  QuantityInterface(models.Model):
    interface = models.ForeignKey(ControlInterface, on_delete=models.CASCADE, related_name='quantity_interfaces')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='quantity_interfaces')
    quantity = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        validators=[MinValueValidator(1, 'Минимальное значение 1')],
        verbose_name='Количество'
    )
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['interface', 'equipment'], name='unicue_equipment_interface'
    #         ),
    #     ]



class Association(models.Model):
    equipment_interface = models.ForeignKey(ControlInterface, on_delete=models.CASCADE, verbose_name='Интерфейс оборудования', null=True, blank=True, related_name='associstions')
    device_input = models.ManyToManyField(Input, verbose_name='Вход прибора УД', blank=True, related_name='associstions')
    device_output = models.ManyToManyField(Output, verbose_name='Выход прибора УД', blank=True, related_name='associstions')
    device_interface = models.ForeignKey(Interface, on_delete=models.SET_NULL, verbose_name='Интерфейс прибора УД', null=True, blank=True, related_name='associstions')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='associstions')

    class Meta:
        verbose_name = 'Ассоциация интерфейсов'
        verbose_name_plural = 'Ассоциации интерфейсов'
        constraints = [
            models.UniqueConstraint(
                fields=['equipment_interface', 'device_interface'], name='add_favorite'
            ),
        ]















