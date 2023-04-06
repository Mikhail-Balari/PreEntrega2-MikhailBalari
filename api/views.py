from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, JsonResponse

from .models import Pin, Module, Machine
from . import forms

def machine_list(request):
    return render(request, 'api/machine_list.html', dict(machines=Machine.objects.all()))

def machine(request, id: int):
    return render(request, 'api/machine.html', dict(machine=get_object_or_404(Machine, pk=id)))

def module(request: HttpRequest, id: str):
    module: Module = get_object_or_404(Module, pk=id)
    if request.method == 'POST':
        pin_id = request.POST.get('id')
        pin = Pin.objects.get(pk=pin_id)
        form = forms.PinForm(request.POST, instance=pin)
        form.save()
    return render(request, 'api/module.html', dict(module=module))