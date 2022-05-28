from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Land
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

User = get_user_model()



@method_decorator(login_required, name='dispatch')
class LandListView(ListView):
    """Выводит список участков"""
    # queryset = House.objects.all()
    context_object_name = 'lands'
    template_name = 'home/land_list.html'

    
    def get_queryset(self):
        user = self.request.user
        queryset = Land.objects.filter(author=user)
        return queryset


@login_required
def land_detail(request, username, house_id):
    """Просмотр карточки обьекта"""
    user = get_object_or_404(User, username=username)
    land = get_object_or_404(Land, id=house_id, author=user)
    # import ipdb; ipdb.set_trace()
    interfaces = {}
    for building in land.buildings.all():
        for room in building.rooms.all():
            for equipment in room.equipments.all():
                for quantity in equipment.quantity_interfaces.all():
                    
                    # for association in quantity.interface.associstions.all():
                    #     for output in association.device_output.all():
                    #         print(output.devices_out.all())
                    #         for device in output.devices_out.all():
                    #             print(device)

                    if quantity.interface.name not in interfaces:
                        interfaces[quantity.interface.name] = quantity.quantity
                    else:
                        interfaces[quantity.interface.name] += quantity.quantity
    return render(
        request, 'home/land_detail.html', {
            'land': land,
            'interfaces': interfaces,
        }
        
    )


def viewIndex(request):
    """"Главная"""
    data ={'header':'Главная страница', 'message': 'Вы на главной'}
    return render(
        request, 'home/index_page.html', context=data
    )