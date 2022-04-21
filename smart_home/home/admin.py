from django.contrib import admin
from .models import SmartSystem, Location, Tag, ControlInterface, Land, Building, Room, Equipment
# from device.models import Device, Interface, Pins



@admin.register(SmartSystem)
class SmartSystemAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description',
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(ControlInterface)
class ControlInterfaceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'voltage', 'current', 'start_current',
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'author', 'date_create',
    )
    search_fields = ('name',)
    list_filter = ('name', 'author', 'date_create')
    date_hierarchy = 'date_create'
    ordering = ('date_create',)




@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'land', 'floor',
    )
    search_fields = ('name',)
    ordering = ('name',)



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'building', 'floor',
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'type',  
    )
    search_fields = ('name',)
    list_filter = ('type', 'name', 'specific', 'location', 'interface')
    ordering = ('name',)