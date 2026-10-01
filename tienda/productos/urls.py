from django.urls import path
from . import views

urlpatterns = [
    path("crear/", views.crear),
    path("listar/", views.listar),
    path("editar/<int:producto_id>/", views.editar),
    path("detalle/<int:producto_id>/", views.detalle),
    path("eliminar/<int:producto_id>/", views.eliminar)
]