from django.contrib import admin
from .models import Device, Interface, Output, Input, Manufacturer


class InputInline(admin.TabularInline):
    model = Device.input.through
    extra = 1

class OutputInline(admin.TabularInline):
    model = Device.output.through
    extra = 1



@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'short_description', 'unit',
    )
    inlines = [InputInline, OutputInline]
    search_fields = ('name',)
    list_filter = ('name', 'specific',)
    ordering = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description',
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'type', 'voltage_ac', 'nominal_current', 'author'
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'purpose', 'author'
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    search_fields = ('title',)
    ordering = ('title',)