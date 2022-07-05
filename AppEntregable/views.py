from django.shortcuts import render
from django.http import HttpResponse
from AppEntregable.models import Familia
from django.template import Template, Context, loader


# Create your views here.

def padre(self):
    padre = Familia(nombre="Carlos Saul", edad=60, nac="1962-5-25")
    padre.save()
    texto=f"Mi padre es: {padre.nombre}, tiene {padre.edad} años y nacio en {padre.nac}"

    return HttpResponse(texto)

def madre(self):
    madre = Familia(nombre="Teresa De Calculta", edad=50, nac="1972-5-25")
    madre.save()
    texto=f"Mi madre es: {madre.nombre}, tiene {madre.edad} años y nacio en {madre.nac}"

    return HttpResponse(texto)


def hermano(self):
    hermano = Familia(nombre="Duki", edad=20, nac="2002-5-25")
    hermano.save()
    texto=f"Mi hermano es: {hermano.nombre}, tiene {hermano.edad} años y nacio en {hermano.nac}"

    return HttpResponse(texto)



def template1(self):
    nombre="Carlitos"
    apellido="Menem"

    diccionario = {"Nombre":nombre, "Apellido":apellido}

    #mihtml=open('C:/Users/Sergio/Documents/Curso_python/Entregable1/Entregable/Plantillas/template.html')
    #mihtml.close()
    #micontexto=Context(diccionario)
    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)
    
    return HttpResponse (documento)


def templateHermano(self):
    nombre="Duki"
    edad=22
    nacimiento="25-5-2000"

    diccionario = {"Nombre":nombre, "Edad":edad, "Nacimiento":nacimiento}

    #mihtml=open('C:/Users/Sergio/Documents/Curso_python/Entregable1/Entregable/Plantillas/template.html')
    #mihtml.close()
    #micontexto=Context(diccionario)
    plantilla = loader.get_template('Hermano.html') 
    documento = plantilla.render(diccionario)
    
    return HttpResponse (documento)


def templateMadre(self):
    nombre="Teresa De Calcuta"
    edad=50
    nacimiento="20-6-1972"

    diccionario = {"Nombre":nombre, "Edad":edad, "Nacimiento":nacimiento}

    #mihtml=open('C:/Users/Sergio/Documents/Curso_python/Entregable1/Entregable/Plantillas/template.html')
    #mihtml.close()
    #micontexto=Context(diccionario)
    plantilla = loader.get_template('Madre.html') 
    documento = plantilla.render(diccionario)
    
    return HttpResponse (documento)


def templatePadre(self):
    nombre="Carlos Saul"
    edad=60
    nacimiento="20-6-1962"

    diccionario = {"Nombre":nombre, "Edad":edad, "Nacimiento":nacimiento}

    #mihtml=open('C:/Users/Sergio/Documents/Curso_python/Entregable1/Entregable/Plantillas/template.html')
    #mihtml.close()
    #micontexto=Context(diccionario)
    plantilla = loader.get_template('Padre.html') 
    documento = plantilla.render(diccionario)
    
    return HttpResponse (documento)