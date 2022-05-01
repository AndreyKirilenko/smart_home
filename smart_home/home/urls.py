from django.urls import path
from .views import land_detail, LandListView, viewIndex

urlpatterns = [
    path('', viewIndex, name='index'),
    path('home/', LandListView.as_view(), name='list_home'),
    path('land_detales/<int:house_id>/', land_detail, name='land_detail'),
]