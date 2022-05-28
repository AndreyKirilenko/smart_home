from django.contrib import admin
from .models import SmartSystem, Location, Tag, ControlInterface, Land, Building, Room, Equipment, Association
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
        'name', 'description', 'voltage', 'start_current',
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


class InterfaceInline(admin.TabularInline):
    model = Equipment.control.through
    extra = 1

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'model', 'type', 'author'  
    )
    inlines = [InterfaceInline]
    search_fields = ('name', 'model')
    list_filter = ('type', 'name', 'specific', 'location', 'control', 'author')
    ordering = ('name',)
    prepopulated_fields = {"slug": ("name", "model", )}


@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    list_display = (
        'equipment_interface', 'device_interface'  
    )
    # search_fields = ('name', 'model')
    # list_filter = ('type', 'name', 'specific', 'location', 'interface', 'author')
    # ordering = ('name',)