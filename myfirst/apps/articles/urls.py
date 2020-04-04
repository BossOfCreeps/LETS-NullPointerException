import django
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('events/', views.events, name = 'events'),
    path('events/<int:event_id>/', views.event, name='event'),
    path('events/<int:event_id>/add_comment', views.add_comment, name='add_comment'),
    path('profile/', views.profile, name = 'profile'),
    path('reg/', views.reg, name = 'reg'),
    path('accounts/', include('django.contrib.auth.urls')),
]