from django.http import HttpResponse
import datetime
from django.template import Context, Template


def saludar(request):
    return HttpResponse("Hola mundo!")

def segunda_vista(request):
    return HttpResponse("Ya entendi! Esto es muy simple!!!")

def dia_de_hoy(request):

    dia=datetime.datetime.today()
    cadena="Hoy es: "+str(dia)
    return HttpResponse(cadena)

def saludo_con_nombre(self, nombre):
    return HttpResponse("<h1>Hola mi nombre es: "+nombre+"</h1>")

def calcula_anio_nacimiento(self, edad):
    return HttpResponse("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")

def probandoHtml(self):
    miArchivo=open("F:/Clase17/Proyecto1/Plantillas/template1.html")

    plantilla=Template(miArchivo.read())
    miArchivo.close()
    contexto=Context()
    documento=plantilla.render(contexto)

    return HttpResponse(documento)