from contextvars import Context
from multiprocessing import context
from pipes import Template
from re import template
from django.http import HttpResponse
from datetime import datetime

def inicio(request):
    return HttpResponse("hola soy mi primer vista en django")

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"fecha actual:{fecha_actual}" )

def saludo(request, nombre, apellido):
    return HttpResponse(f"Hola {nombre} {apellido}" )
    
def mi_template(request):
    archivo = open(r"/Users/MarianSanJuan/Desktop/Coderhouse/Python/Django/template/prueba.html","r")
    template1 = Template(archivo.read())
    archivo.close()
    contexto1 = Context()
    render1 = template1.render(contexto1)
    return HttpResponse(render1)

    
    