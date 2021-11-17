from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import DateInput, Select, TextInput
from .models import Cliente, Empresa, Solicitud, Contenedor, Buque

class CuastomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

class ClienteForm(forms.ModelForm):      
    numero_contrato=forms.CharField(widget=TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=Cliente
        fields='__all__'
class EmpresaForm(forms.ModelForm):
    class Meta:
        model=Empresa
        fields='__all__'

class SolicitudForm(forms.ModelForm):
    class Meta:
        model=Solicitud
        fields='__all__'

class ContenedorForm(forms.ModelForm):
    class Meta:
        model=Contenedor
        fields='__all__'

class BuqueForm(forms.ModelForm):
    class Meta:
        model=Buque
        fields='__all__'