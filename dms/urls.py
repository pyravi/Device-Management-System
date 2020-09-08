from django.urls import path
from .views import (
    HomeView,
    DeviceAllocationView,
    DeviceManagerView,
    AuthView,
    )

app_name='dms'

urlpatterns = [
path('',HomeView.as_view(),name='request-page'),
path('device-assign/',DeviceAllocationView.as_view(),name='device-assign'),
path('device/',DeviceManagerView.as_view(),name='device'),
path('auth/',AuthView.as_view(),name='auth-page')
]