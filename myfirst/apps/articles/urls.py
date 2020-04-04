import django
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('events/', views.events, name = 'events'),
    path('devices/<int:device_id>/', views.device, name='device'),
    path('accounts/', include('django.contrib.auth.urls')),
]