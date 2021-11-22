from django.urls import path
from .views import registro,nueva_solicitud,nueva_orden, nuevo_servicio, inicio, nuevo_cliente,listar_cliente, listar_buques, listar_personas, listar_contenedor, listar_servicios

urlpatterns = [
    path('registro/', registro,name="registro"),
    path('', inicio,name="inicio"),
    path('nuevo_cliente/', nuevo_cliente, name="nuevo_cliente"),
    path('listar_cliente/', listar_cliente, name="listar_cliente"),
    path('listar_buques/', listar_buques, name="listar_buques"),
    path('listar_personas/', listar_personas, name="listar_personas"),
    path('listar_contenedor/', listar_contenedor, name="listar_contenedor"),
    path('listar_servicios/', listar_servicios, name="listar_servicios"),
    path('nueva_solicitud/', nueva_solicitud, name="nueva_solicitud"),
    path('nuevo_servicio/', nuevo_servicio, name="nuevo_servicio"),
    path('nueva_orden/', nueva_orden, name="nueva_orden"),
]