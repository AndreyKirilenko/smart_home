from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Device, QuantityOutput, QuantityInput
from django.views.generic import CreateView, ListView


class DeviceListView(ListView):
    """Выводит список смет"""
    queryset = Device.objects.all()
    context_object_name = 'devices'
    
    template_name = 'device/device_list.html'


def device_view(request, device_id):
    """Просмотр карточки прибора"""
    device = get_object_or_404(Device, id=device_id)
    outputs = QuantityOutput.objects.filter(device=device)
    inputs = QuantityInput.objects.filter(device=device)

    # import ipdb; ipdb.set_trace()
    return render(
        request, 'device/device_detail.html', {
            'device': device,
            'outputs' : outputs,
            'inputs': inputs,
        }
    )