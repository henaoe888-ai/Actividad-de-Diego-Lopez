from django.http import HttpResponse #libreria para dar respuesta http

def home(request):
    return HttpResponse("Hello, World!")