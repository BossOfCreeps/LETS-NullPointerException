import django
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('events/add', views.add_event, name='add_event'),
    path('events/remove', views.remove_event, name='remove_event'),
    path('events/<int:event_id>/', views.event, name='event'),
    path('events/<int:event_id>/add_comment', views.add_comment, name='add_comment'),
    path('events/<int:event_id>/remove_comment', views.remove_comment, name='remove_comment'),
    path('events/<int:event_id>/invite', views.invite, name='invite'),
    path('profile/', views.profile, name='profile'),
    path('profile/call/', views.call, name='call'),
    path('profile/submit_invite/', views.submit_invite, name='submit_invite'),
    path('profile/test/', views.test, name='test'),
    path('reg/', views.reg, name='reg'),
    path('accounts/', include('django.contrib.auth.urls')),
]
