from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear, name='crear'),
    path('listar/', views.listar, name='listar'),
    path('editar/<int:producto_id>/', views.editar, name='editar'),
    path('eliminar/<int:producto_id>/', views.eliminar, name='eliminar'),
]