from django.db import models

# Create your models here.


class Machine(models.Model):
    name = models.CharField(max_length=128)


class Module(models.Model):
    name = models.CharField(max_length=128)
    machine = models.ForeignKey(Machine, models.CASCADE, related_name='modules')
    pins: 'models.Manager[Pin]'

class Pin(models.Model):
    pin_number = models.PositiveIntegerField()
    is_used = models.BooleanField()

    module: Module = models.ForeignKey(Module, models.CASCADE, related_name='pins')
    