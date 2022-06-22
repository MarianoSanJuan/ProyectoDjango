from django.urls import path
from .views import inicio, ver_fecha, saludo, mi_template


urlpatterns = [
    path('', inicio),
    path('fecha/', ver_fecha),
    path('saludo/<nombre>/<apellido>',saludo),
    path('mi-template/',mi_template)
] 