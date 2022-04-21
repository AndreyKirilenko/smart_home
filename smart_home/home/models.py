from django.db import models
from django.contrib.auth import get_user_model
from device.models import SmartSystem
from django.core.validators import MinValueValidator

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
    voltage = models.IntegerField(default=0, verbose_name='Напряжение. Если есть на выходе')
    current = models.IntegerField(default=0, verbose_name='Потребление тока')
    start_current = models.IntegerField(default=0, verbose_name='Стартовый ток')
    count_pins = models.IntegerField(default=0, verbose_name='Количество входов/выходов')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='control_interfaces')

    class Meta:
        verbose_name = 'Интерфейс ОБОРУДОВАНИЯ'
        verbose_name_plural = 'Интерфейсы ОБОРУДОВАНИЯ'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.count_pins}'


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
    name = models.CharField(max_length=100, verbose_name='Наименование оборудования')
    description = models.TextField(max_length=200, verbose_name='Описание оборудования', null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='equipments', verbose_name='Помещение в котором установлено')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True, related_name='equipments', verbose_name='Здание в котором установлено')
    land = models.ForeignKey(Land, on_delete=models.CASCADE, null=True, blank=True, related_name='equipments', verbose_name='Земельный уасток где установлено')
    specific = models.ManyToManyField(SmartSystem, blank=True, related_name='equipments', verbose_name='К какой системе относится')
    location = models.ManyToManyField(Location, blank=True, related_name='equipments', verbose_name='Где может быть установлен')
    tag = models.ManyToManyField(Tag, blank=True, related_name='equipments', verbose_name='Теги')
    voltage = models.IntegerField(default=0, verbose_name='Вольтаж. Без учета управляющего напряжения')
    current = models.IntegerField(default=0, verbose_name='Потребление тока')
    start_current = models.IntegerField(default=0, null=True, blank=True, verbose_name='Ствртовый ток')
    interface = models.ManyToManyField(ControlInterface, blank=True, related_name='equipments', verbose_name='Интерфейс управления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='equipments')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ['name']

    def __str__(self):
        return self.name

















