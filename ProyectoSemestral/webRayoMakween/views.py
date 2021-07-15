from typing import ContextManager
from django.contrib import auth
from django.db import models
from django.http import request, response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib.auth.decorators import login_required, permission_required
from .models import Trabajos,mecanico,contacto
from .filters import FiltroTrabajos
from django.contrib import messages
import requests

#importa el modelo de la tabla user

# Create your views here.

def index(request):
    meca = mecanico.objects.all()
    trabajos = Trabajos.objects.filter(publicar=True)
    contactos = contacto.objects.all()
    cant = Trabajos.objects.all().count()
    contexto = {"contactos":contactos,"trabajos":trabajos,"meca":meca,"cant":cant}
    response = requests.get("http://127.0.0.1:8000/api/trabajos/")
    contexto["trabajos_api"] = response.json()
    response = requests.get("http://127.0.0.1:8000/api/contactos/")
    contexto["contactos_api"] = response.json()
    return render(request,"index.html",contexto)

def listado(request):
    listado_trabajo = Trabajos.objects.all()

    miFiltro = FiltroTrabajos(request.POST, queryset=listado_trabajo)
    listado_Trabajos = miFiltro.qs

    data = { "lista" : listado_Trabajos,"filtro" : miFiltro }

    return render(request, 'listrado.html', data)

def atencion(request):
    return render(request,"Atencion.html")

def registro(request):
    mensaje=""
    if request.POST:
        usuario = request.POST.get("txtusuario")
        nombre = request.POST.get("txtnombre")
        correo = request.POST.get("txtcorreo")
        pass1 = request.POST.get("txtPass1")

        usu = User()
        usu.username = usuario
        usu.first_name = nombre
        usu.email = correo
        usu.set_password(pass1)
        usu.save()

        mensaje="Usuario Grabado"

    contexto = {"mensaje":mensaje}
    return render(request,"registro.html",contexto)

def trabajo(request):
    meca = mecanico.objects.all()
    trabajos = Trabajos.objects.filter(publicar=True)
    contactos = contacto.objects.all()
    contexto = {"contactos":contactos,"trabajos":trabajos,"meca":meca}
    return render(request, "trabajos.html",contexto)
@login_required(login_url='/login/')
def validar(request):
    trabajos = Trabajos.objects.all()
    contexto = {"Trabajos":trabajos}
    return render(request,"validar_post.html",contexto)

def regitra(request):
    mensaje = ""
    Mecanicos = mecanico.objects.all()
    trabajos = Trabajos.objects.all()
    if request.POST:
        diagnostico = request.POST.get("txtdiag")
        fecha = request.POST.get("txtfecha")
        materiales = request.POST.get("txtmate")
        descripcion = request.POST.get("txtdescripcion")
        imagen= request.FILES.get("txtimagen")
        nombre = request.POST.get("cbonombre")
        obj_nombre = mecanico.objects.get(nombre_mec=nombre)
        
        # trabajos = Trabajos()
        # trabajos.diagnostico=diagnostico
        # trabajos.nombre=obj_nombre
        # trabajos.fecha=fecha
        # trabajos.materiales=materiales
        # trabajos.descripcion=descripcion
        # trabajos.imagen=imagen
        # trabajos.save()
        datos_json={"diagnostico":diagnostico,
                    "nombre":obj_nombre,
                    "fecha":fecha,
                    "materiales":materiales,
                    "descripcion":descripcion
        }
        if imagen is not None:
            datos_json["imagen"]=imagen
        response = request.post("http://127.0.0.1:8000/api/trabajo_crear/",data=datos_json)
        mensaje="Trabajo registrado"
    contexto = {"mensaje":mensaje,"Trabajos":trabajos,"Mecanicos":Mecanicos}
    return render(request,"registro_trabajo.html",contexto)

def regico(request):
    mensaje = ""
    comentarios = contacto.objects.all()
    contexto = {"comentarios":comentarios}
    if request.POST:
        nombre_cl=request.POST.get("txtnombre")
        correo=request.POST.get("txtcorreo")
        asunto=request.POST.get("txtasunt")
        sugerencia=request.POST.get("txtsuge")
        con = contacto()
        con.nombre_cl=nombre_cl,
        con.correo=correo,
        con.asunto=asunto,
        con.sugerencia=sugerencia
        con.save()
        mensaje="Trabajo registrado"

    contexto = {"mensaje":mensaje}
    return render(request,"Formulario_contacto.html",contexto)

def inicio(request):
    mensaje=" "
    if request.POST:
        nombre = request.POST.get("txtusuario")
        contra = request.POST.get("txtcontra")
        us = authenticate(request,username=nombre,password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            return render(request,"login.html")
        else:
            mensaje="no existe usuario o contraseña incorrecta"
    contexto={"mensaje":mensaje}
    return render(request,"login.html",contexto)
@login_required(login_url='/login/')
@permission_required('webRayoMakween.delete_trabajos',login_url='/login/')
def eliminar(request, id):
    tra = Trabajos.objects.get(codigo=id)
    try:
        tra.delete()
        mensaje = "Trabajo rechazado"
    except:
        mensaje = ""

    contexto = {"mensaje":mensaje}
    return redirect("listrado.html")
@login_required(login_url='/login/')
def buscar_modificar(request, id):
    try:
        tra = Trabajos.objects.get(diagnostico=id)
        cant = Trabajos.objects.all().count()
        contexto = {"tra":tra,
                    "cant":cant}
        return render(request,"modificar.html",contexto)
    except:
        mensaje = "No existe trabajo"

    contexto = {"mensaje":mensaje}
    return render(request,"validar_post.html",contexto)

def modificar(request,id):
    trabajos=Trabajos.objects.get(codigo=id)
    Mecanicos = mecanico.objects.all()
    mensaje=""
    if request.POST:
        diagnostico = request.POST.get("txtdiag")
        fecha = request.POST.get("txtfecha")
        materiales = request.POST.get("txtmate")
        descripcion = request.POST.get("txtdescripcion")
        imagen= request.FILES.get("txtimagen")
        nombre = request.POST.get("cbonombre")
        obj_nombre = mecanico.objects.get(nombre_mec=nombre)

        try:
            tra = Trabajos.objects.get(diagnostico=diagnostico)
            tra.diagnostico=diagnostico,
            tra.nombre=obj_nombre,
            tra.fecha=fecha,
            tra.materiales=materiales,
            tra.descripcion=descripcion,
            if imagen is not None:
                imagen=imagen
            tra.comentario= '//'
            tra.save()
            mensaje="Datos modificados"
        except:
            mensaje="No se ha modificado datos"

    contexto = {"mensaje":mensaje,"trabajos":trabajos,"Mecanicos":Mecanicos}
    return render(request,"modificar.html",contexto)

def cerrar_sesion(request):
    logout(request)
    return render(request,"index.html")

def ficha(request,id):
    trabajo=Trabajos.objects.get(codigo=id)
    trabajos=Trabajos.objects.all()
    trabajos = Trabajos.objects.filter(publicar=True,codigo=id)
    contexto = {"trabajos":trabajos,"trabajo":trabajo}
    return render(request,'ficha.html',contexto)

def login(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=nombre,password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            meca = mecanico.objects.all()
            contexto={"meca":meca}
            return render(request,"index.html",contexto)
        else:
            mensaje="no existe usuario o contraseña incorrecta"
            contexto={"mensaje":mensaje}
    return render(request,"login.html",contexto)
    