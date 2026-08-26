from django.urls import path #quiere decir rutas de django import path
from . import views #importa las vistas del archivo views.py

urlpatterns = [
    path('', views.home),
]