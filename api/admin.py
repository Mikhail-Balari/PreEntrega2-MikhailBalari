from django.contrib import admin

from .models import Pin, Module, Machine


class PinInline(admin.TabularInline):
    model = Pin

class ModuleInline(admin.TabularInline):
    model = Module
    inlines = [PinInline]



@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]

@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    pass
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [PinInline]