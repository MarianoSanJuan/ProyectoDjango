from contextvars import Context
from multiprocessing import context
from pipes import Template
from re import template
from unittest import loader
from django.http import HttpResponse
from datetime import datetime

from django.template import Template, Context, loader

def inicio(request):
    return HttpResponse("hola soy mi primer vista en django")

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"fecha actual:{fecha_actual}" )

def saludo(request, nombre, apellido):
    return HttpResponse(f"Hola {nombre} {apellido}" )


# Versión 1 para levantar un template    
# def mi_template(request):
#     archivo = open(r"/Users/MarianSanJuan/Desktop/Coderhouse/Python/Django/template/prueba.html","r")
#     template1 = Template(archivo.read())
#     archivo.close()
#     contexto1 = Context()
#     render1 = template1.render(contexto1)
#     return HttpResponse(render1)


# Versión 2 para levantar un template  
# Acá acorta la URL agregandole el path en setting.py, en la parte de DIR  

# def mi_template(request):

#     template1 = loader.get_template("prueba.html")
#     render1 = template1.render({})
#     return HttpResponse(render1)
    
    
# Versión 2 pero con un diccionario dentro del contexto 

def mi_template(request):

    template1 = loader.get_template("prueba.html")
    nombre = "Momia"
    apellido = "Blanca"
    render1 = template1.render({"nombre":nombre, "apellido":apellido,"edad": 2000})
    return HttpResponse(render1)