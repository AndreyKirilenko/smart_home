from django.shortcuts import get_object_or_404, render
from .models import Land
from django.views.generic import CreateView, ListView


class LandListView(ListView):
    """Выводит список участков"""
    # queryset = House.objects.all()
    context_object_name = 'lands'
    template_name = 'home/land_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Land.objects.filter(author=user)
        return queryset


def land_detail(request, house_id):
    """Просмотр карточки обьекта"""
    land = get_object_or_404(Land, id=house_id)
    return render(
        request, 'home/land_detail.html', {
            'land': land,
        }
    )

def viewIndex(request):
    """"Главная"""
    data ={'header':'Главная страница', 'message': 'Вы на главной'}
    return render(
        request, 'home/index_page.html', context=data
    )