from django.http import HttpResponse 
from django.shortcuts import render
from django.template import context,Template, loader


def saludo(request):
    return HttpResponse("Hola perritos")

def template(self):
    miArchivo= open('C:/Users/Sergio/Documents/Curso_python/Entregable1/Entregable/Plantillas/template.html')
    plantilla=Template(miArchivo.read())
    miArchivo.close()
    contexto= context()
    documento= plantilla.render(contexto)
    return HttpResponse(documento)
