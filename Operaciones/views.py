from django.shortcuts import render
from django.contrib.auth import forms
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CuastomUserCreationForm,OrdenForm, ClienteForm, EmpresaForm, SolicitudForm, ContenedorForm, BuqueForm, ServicioForm
from .models import Empresa, Solicitud, Cliente,Buque, Contenedor, Persona, Servicios, Orden
from _datetime import datetime, date

# Create your views here.
def inicio(request):
    solicitudes=Solicitud.objects.all()
    clientes=Cliente.objects.all()
    ordenes=Orden.objects.all()
    mixtas=0
    tcp=0
    cna=0
    extranjeras=0
    estatales=0
    contenedores=[]
    buques=[]
    contbuques1=0
    contbuques2=0
    contbuques3=0
    contbuques4=0
    contcont1=0
    contcont2=0
    contcont3=0
    contcont4=0
    for s in solicitudes:
        if(s.medio=="Buques"):
            if(date(2021,1,1)<s.fecha_Inspeccion<date(2021,3,31)):
                contbuques1=contbuques1+1
            elif(date(2021,4,1)<s.fecha_Inspeccion<date(2021,6,30)):
                contbuques2=contbuques2+1
            elif(date(2021,7,1)<s.fecha_Inspeccion<date(2021,9,30)):
                contbuques3=contbuques3+1
            elif(date(2021,10,1)<s.fecha_Inspeccion<date(2021,12,31)):
                contbuques4=contbuques4+1
        if(s.medio=="Contenedores"):
            if(date(2021,1,1)<s.fecha_Inspeccion<date(2021,3,31)):
                contcont1=contcont1+1
            elif(date(2021,4,1)<s.fecha_Inspeccion<date(2021,6,30)):
                contcont2=contcont2+1
            elif(date(2021,7,1)<s.fecha_Inspeccion<date(2021,9,30)):
                contcont3=contcont3+1
            elif(date(2021,10,1)<s.fecha_Inspeccion<date(2021,12,31)):
                contcont4=contcont4+1
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
    ord=ordenes.count()
    context ={
            'Solicitud': soli,
            'Clientes': client,
            'estatales': estatales,
            'mixtas': mixtas,
            'cna': cna,
            'tcp': tcp,
            'extranjeras':extranjeras,
            'Ordenes': ord,
            'contenedores':contenedores,
            'buques':buques,
            'contbuques1':contbuques1,
            'contbuques2':contbuques2,
            'contbuques3':contbuques3,
            'contbuques4':contbuques4,
            'contcont1':contcont1,
            'contcont2':contcont2,
            'contcont3':contcont3,
            'contcont4':contcont4

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
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Se ha creado el cliente correctamente")
            return redirect(to="inicio")
        data={
            "form":formulario,
        }

    return render(request,'operaciones/Clientes/Nuevo_Cliente.html',data)

def listar_cliente(request):
    data={
        "empresas":Empresa.objects.all(),
        "clientes":Cliente.objects.all()
    }
    return render(request,'operaciones/Clientes/Listar_Clientes.html',data)
def listar_buques(request):
    data={
        "buques":Buque.objects.all()
    }
    return render(request,'operaciones/Buques/Listar_Buques.html',data)
def listar_contenedor(request):
    data={
        "contenedores":Contenedor.objects.all()
    }
    return render(request,'operaciones/Contenedores/Listar_Contenedores.html',data)
def listar_personas(request):
    data={
        "personas":Persona.objects.all()
    }
    return render(request,'operaciones/Personas/Listar_Personas.html',data)
def listar_servicios(request):
    data={
        "servicios":Servicios.objects.all()
    }
    return render(request,'operaciones/Servicios/Listar_Servicios.html',data)

def nueva_solicitud(request):
    data={
        'form': SolicitudForm(),
        'formbuque':BuqueForm(),
        'formcontenedor':ContenedorForm()
    }
    if request.method=='POST':
        formulario=SolicitudForm(data=request.POST)
        if formulario.is_valid():
           # medio=request.POST.get('medio')
           # if medio=="Buques":
             #   formulario.cleaned_data['id_contenedor'].null=True
                formulario.save()
                messages.success(request,"Se ha creado el cliente correctamente")
          #  elif medio=="Contenedores":
            #    formulario.cleaned_data['id_buque'].null=True
            #    formulario.save()
           #     messages.success(request,"Se ha creado el cliente correctamente")
    #if request.method=='POST':
     #   formulariobuque=BuqueForm(data=request.POST)
     #   if formulariobuque.is_valid():
     #       formulariobuque.save()
     #       messages.success(request,"Se ha creado el cliente correctamente")
    #if request.method=='POST':
     #   formulariocontenedor=ContenedorForm(data=request.POST)
     #   if formulariocontenedor.is_valid():
      #      formulariocontenedor.save()
       #     messages.success(request,"Se ha creado el cliente correctamente")
        data={
            "form":formulario,
           # "formbuque":formulariobuque,
            #"formcontenedor":formulariocontenedor
        }

    return render(request,'operaciones/Solicitudes/Nueva_Solicitud.html',data)

def nuevo_servicio(request):
    data={
        'form': ServicioForm()
    }
    if request.method=='POST':
        formulario=ServicioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Se ha creado el servicio correctamente")
            return redirect(to="listar_servicios")
        data={
            "form":formulario
        }

    return render(request,'operaciones/Servicios/Nuevo_Servicio.html',data)
def nueva_orden(request):
    data={
        'form': OrdenForm()
    }
    if request.method=='POST':
      formulario=OrdenForm(data=request.POST)
      if formulario.is_valid():
        formulario.save()
        messages.success(request,"Se ha creado la orden correctamente")
        return redirect(to="listar_ordenes")
      data={
            "form":formulario
        }
    return render(request,'operaciones/Ordenes/nueva_orden.html',data)