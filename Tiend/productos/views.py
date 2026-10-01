from urllib import request

from django.shortcuts import render
from .models import Producto

# Create your views here.
def crear(request):
    if request.method=="POST":
        productos=Producto(
            nombre=request.POST["nombre"],
            categoria=request.POST["categoria"],
            precio=request.POST["precio"],
            stock=request.POST["stock"],
            estado=request.POST["estado"]
        )
        productos.save()

    return render(request, "productos/formulario.html")


def listar(request):
    productos=Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})

def detalle(request,id):
    productos = Producto.objects.get(id=id)#SELECT * FROM Contacto WHERE id=7
    return render(request, "productos/detalle.html",{"productos": productos})

def editar(request,id):
    
    productos=Producto.objects.get(id=id)

    if request.method=="POST":

        productos.nombre=request.POST["nombre"]
        productos.categoria=request.POST["categoria"]
        productos.precio=request.POST["precio"]
        productos.stock=request.POST["stock"]
        productos.estado=request.POST["estado"]

        productos.save()
        return render(
            request,
            "productos/detalle.html",
            {"productos": productos}
        )
    
    return render(
        request,
        "productos/formulario.html",
        {"productos": productos}
    )

def eliminar(request, id):
    productos = Producto.objects.get(id=id)
    productos.delete()
    return render(request, "productos/detalle.html", {"productos": productos})