# music/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playlist/', views.playlist, name='playlist'),
]
