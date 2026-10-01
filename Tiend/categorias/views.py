from django.shortcuts import render
from .models import Categoria


# CREAR
def crear(request):

    if request.method=="POST":

        categoria=Categoria(
            nombre=request.POST["nombre"],
            observaciones=request.POST["observaciones"],
            estado=request.POST["estado"]
        )

        categoria.save()

    return render(request, "categorias/formulario.html")


# LISTAR
def listar(request):

    categorias = Categoria.objects.all()

    return render(
        request,
        "categorias/lista.html",
        {"categorias": categorias}
    )


# VER
def detalle(request, id):

    categoria = Categoria.objects.get(id=id)

    return render(
        request,
        "categorias/detalle.html",
        {"categoria": categoria}
    )


# EDITAR
def editar(request, id):

    categoria = Categoria.objects.get(id=id)

    if request.method == "POST":

        categoria.nombre=request.POST["nombre"]
        categoria.observaciones=request.POST["observaciones"]
        categoria.estado=request.POST["estado"]

        categoria.save()

        return render(
            request,
            "categorias/detalle.html",
            {"categoria": categoria}
        )

    return render(
        request,
        "categorias/formulario.html",
        {"categoria": categoria}
    )

# ELIMINAR
def eliminar(request, id):

    categoria = Categoria.objects.get(id=id)

    categoria.delete()

    return render(
        request,
        "categorias/lista.html",
        {"categorias": Categoria.objects.all()}
    )