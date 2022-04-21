from django.urls import path
from .views import DeviceListView, device_view


urlpatterns = [
    path('', DeviceListView.as_view(), name='device_list'),
    path('device_detail/<int:device_id>/', device_view, name='device_detail'),
] 