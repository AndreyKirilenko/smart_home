from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.forms import SlugField
User = get_user_model()


class SmartSystem(models.Model):
    """Системы умного дома"""
    name = models.CharField(max_length=100, verbose_name='Имя системы УД', unique=True)
    description = models.TextField(max_length=200, verbose_name='Описание системы УД')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='smart_sustems')

    class Meta:
        verbose_name = 'Система УД'
        verbose_name_plural = 'Системы УД'
        ordering = ['name']

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование производителя', unique=True)
    description = models.TextField(max_length=500, verbose_name='Описание')
    site = models.URLField(max_length=100, verbose_name='Сайт компании')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ['title']
    
    def __str__(self):
        return self.title

class Output(models.Model):
    """Параметры выхода"""
    RELAY_NOC = 'Реле (NO C)'
    RELAY_NCC = 'Реле (NC C)'
    RELAY_NCCNO = 'Реле (NC C NO)'
    PWM = 'ШИМ выход'
    HZ = 'Неизвестно'

    TYPE_OUTPUT = [
        (RELAY_NOC, 'Реле NO/C'),
        (RELAY_NCC, 'Реле NC/C'),
        (RELAY_NCCNO, 'Реле NC/C/NO'),
        (PWM, 'ШИМ'),
        (HZ, 'ХЗ'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Наименование выхода', unique=True)
    type = models.CharField(max_length=50, choices=TYPE_OUTPUT, default=HZ)
    description = models.TextField(max_length=200, verbose_name='Описание выхода')
    voltage_ac = models.IntegerField(default=0, blank=True, null=True, verbose_name='Коммутируемое переменное напряжение')
    voltage_dc = models.IntegerField(default=0, blank=True, null=True, verbose_name='Коммутируемое постоянное напряжение')
    nominal_current = models.IntegerField(default=0, blank=True, null=True, verbose_name='Номинальный коммутируемый ток')
    maximal_current = models.IntegerField(default=0, blank=True, null=True, verbose_name='Максимальный коммутируемый ток')
    starting_current = models.IntegerField(default=0, blank=True, null=True, verbose_name='Пусковой ток')
    pwm_frequency = models.IntegerField(default=0, blank=True, null=True, verbose_name='Частота ШИМ')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='outputs')

    class Meta:
        verbose_name = 'Выход'
        verbose_name_plural = 'Выходы'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.voltage_ac}В {self.nominal_current}А(ном) {self.starting_current}А(старт)'


class Input(models.Model):
    """Параметры входа"""
    name = models.CharField(max_length=100, verbose_name='Наименование входа', unique=True)
    description = models.TextField(max_length=200, verbose_name='Описание входа')
    purpose = models.TextField(max_length=500, verbose_name='Назначение входа', null=True, blank=True)
    general_purpose = models.BooleanField(default=False, verbose_name='Вход общего назначения')
    counting_signals = models.BooleanField(default=False, verbose_name='Счет сигналов')
    frequency_measurement = models.BooleanField(default=False, verbose_name='Измерение частоты')
    direct_control = models.BooleanField(default=False, verbose_name='Прямое управление реле')
    mapping_matrix = models.BooleanField(default=False, verbose_name='Настройка с помощью mapping-матрицы')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='inputs')


    class Meta:
        verbose_name = 'Вход'
        verbose_name_plural = 'Входы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Interface(models.Model):
    """Интерфейс"""
    name = models.CharField(max_length=100, verbose_name='Название интерфейса', unique=True)
    description = models.TextField(max_length=200, verbose_name='Описание интерфейса')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='interfaces')

    class Meta:
        verbose_name = 'Интерфейс'
        verbose_name_plural = 'Интерфейсы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Device(models.Model):
    """SmartHome устройство"""
    image = models.ImageField(verbose_name='Изображение', upload_to='device/image/', default='device/image/default_device.jpg', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Название устрройства', unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug URL")
    short_description = models.TextField(max_length=200, verbose_name='Краткое описание')
    description = models.TextField(max_length=500, verbose_name='Полное описание')
    specific = models.ManyToManyField(SmartSystem, blank=True,  related_name='devices', verbose_name='К какой системе относится')
    input = models.ManyToManyField(
        Input,
        blank=True,
        verbose_name='Входы',
        related_name='devices_in',
        through='QuantityInput',
        through_fields=('device', 'pin',)
    )
    output = models.ManyToManyField(
        Output,
        blank=True,
        verbose_name='Выходы',
        related_name='devices_out',
        through='QuantityOutput',
        through_fields=('device', 'pin',)
    )
    interface = models.ManyToManyField(Interface, blank=True, verbose_name='Интерфейс', related_name='devices')
    unit = models.IntegerField(default=0, verbose_name='Количество юнитов занимаемое устройством')
    voltage = models.IntegerField(default=0, verbose_name='Напряжение питания В')
    current = models.FloatField(default=0, verbose_name='Потребление тока Вт')
    price = models.IntegerField(default=0, verbose_name='Цена Р')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='devices')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, related_name='devices')

    
    class Meta:
        verbose_name = 'Smart Home Устройство'
        verbose_name_plural = 'Smart Home Устройства'
        ordering = ['name']

    def __str__(self):
        return self.name


class  QuantityOutput(models.Model):
    pin = models.ForeignKey(Output, on_delete=models.CASCADE, related_name='quantity_outputs')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='quantity_outputs')
    quantity = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        validators=[MinValueValidator(0, 'Минимальное значение 0')],
        verbose_name='Количество выходов'
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pin', 'device'], name='unicue_ingredient'
            ),
        ]


class  QuantityInput(models.Model):
    pin = models.ForeignKey(Input, on_delete=models.CASCADE, related_name='quantity_inputs')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='quantity_inputs')
    quantity = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        validators=[MinValueValidator(0, 'Минимальное значение 0')],
        verbose_name='Количество входов'
    )
