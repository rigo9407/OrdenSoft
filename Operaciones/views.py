from django.shortcuts import render
from django.contrib.auth import forms
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CuastomUserCreationForm, ClienteForm, EmpresaForm, SolicitudForm, ContenedorForm, BuqueForm
from .models import Empresa, Solicitud, Cliente,Buque, Contenedor, Persona, Servicios

# Create your views here.
def inicio(request):
    solicitudes=Solicitud.objects.all()
    clientes=Cliente.objects.all()
    mixtas=0
    tcp=0
    cna=0
    extranjeras=0
    estatales=0
    for c in Cliente.objects.all():
        if(c.tipo_empresa=='Empresas Mixtas'):
            mixtas=mixtas+1
        elif(c.tipo_empresa=='TCP'):
            tcp=tcp+1
        elif(c.tipo_empresa=='CNA'):
            cna=cna+1
        elif(c.tipo_empresa=='Empresas 100% Cubanas'):
            estatales=estatales+1
        elif(c.tipo_empresa=='Empresa Extranjera'):
            extranjeras=extranjeras+1
    client=clientes.count()
    soli=solicitudes.count()
    context ={
              'Solicitud': soli,
              'Clientes': client,
              'estatales': estatales,
              'mixtas': mixtas,
              'cna': cna,
              'tcp': tcp,
              'extranjeras':extranjeras
     }
    return render(request,"operaciones/inicio.html", context)
def registro(request):
    data={
        'form':CuastomUserCreationForm()
    }
    if request.method=='POST':
        formulario=CuastomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Se ha creado el usuario correctamente")
            return redirect(to="inicio")
        data["form"]=formulario

    return render(request,'registration/registro.html',data)

def nuevo_cliente(request):
    data={
        'form': ClienteForm()
    }
    if request.method=='POST':
        formulario=ClienteForm(data=request.POST)
        formularioempresa=EmpresaForm(data=request.POST)
        if formulario.is_valid()&formularioempresa.is_valid():
            formulario.save()
            formularioempresa.save()
            messages.success(request,"Se ha creado el cliente correctamente")
            return redirect(to="inicio")
        data={
            "form":formulario,
            "formempresa":formularioempresa
        }

    return render(request,'operaciones/Nuevo_Cliente.html',data)

def listar_cliente(request):
    data={
        "empresas":Empresa.objects.all(),
        "clientes":Cliente.objects.all()
    }
    return render(request,'operaciones/Listar_Clientes.html',data)
def listar_buques(request):
    data={
        "buques":Buque.objects.all()
    }
    return render(request,'operaciones/Listar_Buques.html',data)
def listar_contenedor(request):
    data={
        "contenedores":Contenedor.objects.all()
    }
    return render(request,'operaciones/Listar_Contenedores.html',data)
def listar_personas(request):
    data={
        "personas":Persona.objects.all()
    }
    return render(request,'operaciones/Listar_Personas.html',data)
def listar_servicios(request):
    data={
        "servicios":Servicios.objects.all()
    }
    return render(request,'operaciones/Listar_Servicios.html',data)

def nueva_solicitud(request):
    data={
        'form': SolicitudForm(),
        'formbuque':BuqueForm(),
        'formcontenedor':ContenedorForm()
    }
    if request.method=='POST':
        formulario=SolicitudForm(data=request.POST)
        formulariocontenedor=ContenedorForm(data=request.POST)
        formulariobuque=BuqueForm(data=request.POST)

        if formulario.is_valid()&formulariocontenedor.is_valid()&formulariobuque.is_valid():
            formulario.save()
            formulariocontenedor.save()
            formulariobuque.save()
            messages.success(request,"Se ha creado el cliente correctamente")
        data={
            "form":formulario,
            "formbuque":formulariobuque,
            "formcontenedor":formulariocontenedor
        }

    return render(request,'operaciones/nueva_solicitud.html',data)


