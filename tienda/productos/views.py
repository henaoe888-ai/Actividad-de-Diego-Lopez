from urllib import request

from django.shortcuts import render
from .models import Producto

# Create your views here.
def crear(request):
    if request.method == "POST":
        producto = Producto(
            nombre=request.POST["nombre"],
            categoria=request.POST["categoria"],
            precio=request.POST["precio"],
            stock=request.POST["stock"]
        )
        producto.save()

    return render(request, "productos/formulario.html")


def listar(request):
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})

def editar(request, producto_id):
    
    producto = Producto.objects.get(id=producto_id)

    if request.method == "POST":

        producto.nombre = request.POST["nombre"]
        producto.categoria = request.POST["categoria"]
        producto.precio = request.POST["precio"]
        producto.stock = request.POST["stock"]

        producto.save()

    return render(request, "productos/detalle.html", {"producto": producto})

def eliminar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return render(request, "productos/detalle.html", {"producto": producto})