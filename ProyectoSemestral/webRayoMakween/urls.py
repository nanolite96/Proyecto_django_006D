from django.contrib import admin
from django.urls import path
from .views import login, eliminar, ficha, atencion, index, inicio, registro, trabajo, validar, regitra, regico, buscar_modificar, cerrar_sesion, listado,modificar

urlpatterns = [
    path('',index,name='INDEX'),
    path('atencion/',atencion,name='ATENCION'),
    path('contacto/',regico,name='CONTACTO'),
    path('registro/',registro,name='REGISTRO'),
    path('trabajo',trabajo,name='TRABAJO'),
    path('validar/',validar,name='VALIDAR'),
    path('inicio/',inicio,name='INICIO'),
    path('registro_trabajos/',regitra,name='REGITRA'),
    path('eliminar/<id>/',eliminar,name="ELIMINAR"),
    path('buscar_modificar/<id>/',buscar_modificar,name="BUSMOD"),
    path('cerrar/',cerrar_sesion,name='CERRAR'),
    path('login/',login,name='LOGIN'),
    path('ficha/<id>',ficha,name='FICHA'),
    path('listado/',listado,name="LISTADO"),
    path('listado/modificar/<id>',modificar,name="MODIFICAR"),
]
