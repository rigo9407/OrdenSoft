from django.urls import path
from .views import registro,nueva_solicitud,listar_ordenes, nueva_orden, nuevo_servicio, inicio, nuevo_cliente,\
    listar_cliente,modificar_servicio,eliminar_servicio, listar_buques, listar_personas, listar_contenedor,\
    listar_servicios, listar_empresas, subir_imagenes,modificar_buque, eliminar_buque,nuevo_buque,\
    eliminar_cliente, modificar_cliente, modificar_contenedor, eliminar_contenedor, nuevo_contenedor,\
    modificar_orden, eliminar_orden, modificar_empresa, modificar_persona, modificar_solicitud,eliminar_empresa, \
    eliminar_persona, eliminar_solicitud, nueva_persona, nuevo_vendedor, nueva_empresa, nuevo_receptor, \
    nuevo_comprador, listar_solicitud, ver_imagenes, parte

urlpatterns = [
    path('registro/', registro,name="registro"),
    path('', inicio,name="inicio"),

    path('nuevo_cliente/', nuevo_cliente, name="nuevo_cliente"),
    path('listar_cliente/', listar_cliente, name="listar_cliente"),
    path('eliminar_cliente/<id>/',eliminar_cliente,name='eliminar_cliente'),
    path('modificar_cliente/<id>/',modificar_cliente,name='modificar_cliente'),

    path('listar_personas/', listar_personas, name="listar_personas"),
    path('eliminar_persona/<id>/', eliminar_persona, name='eliminar_persona'),
    path('modificar_persona/<id>/', modificar_persona, name='modificar_persona'),
    path('nueva_persona/', nueva_persona, name='nueva_persona'),

    path('listar_contenedor/', listar_contenedor, name="listar_contenedor"),
    path('eliminar_contenedor/<id>/', eliminar_contenedor, name='eliminar_contenedor'),
    path('modificar_contenedor/<id>/', modificar_contenedor, name='modificar_contenedor'),
    path('nuevo_contenedor/', nuevo_contenedor, name='nuevo_contenedor'),

    path('listar_servicios/', listar_servicios, name="listar_servicios"),
    path('nuevo_servicio/', nuevo_servicio, name="nuevo_servicio"),
    path('modificar_servicio/<id>/',modificar_servicio,name='modificar_servicio'),
    path('eliminar_servicio/<id>/', eliminar_servicio, name='eliminar_servicio'),

    path('listar_ordenes/', listar_ordenes, name="listar_ordenes"),
    path('nueva_orden/', nueva_orden, name="nueva_orden"),
    path('modificar_orden/<id>/',modificar_orden,name='modificar_orden'),
    path('eliminar_orden/<id>/', eliminar_orden, name='eliminar_orden'),

    path('listar_empresas/', listar_empresas, name="listar_empresas"),
    path('nueva_empresa/', nueva_empresa, name="nueva_empresa"),
    path('modificar_empresa/<id>/',modificar_empresa,name='modificar_empresa'),
    path('eliminar_empresa/<id>/', eliminar_empresa, name='eliminar_empresa'),

    path('listar_solicitud/', listar_solicitud, name="listar_solicitud"),
    path('nueva_solicitud/', nueva_solicitud, name="nueva_solicitud"),
    path('modificar_solicitud/<id>/',modificar_solicitud,name='modificar_solicitud'),
    path('eliminar_solicitud/<id>/', eliminar_solicitud, name='eliminar_solicitud'),

    path('listar_buques/', listar_buques, name="listar_buques"),
    path('modificar_buque/<id>/',modificar_buque,name='modificar_buque'),
    path('eliminar_buque/<id>/',eliminar_buque,name='eliminar_buque'),
    path('nuevo_buque/',nuevo_buque,name='nuevo_buque'),

    path('subir_imagenes/',subir_imagenes, name='subir_imagenes'),
    path('ver_imagenes/<str:no_orden>/', ver_imagenes, name='ver_imagenes'),

    path('nuevo_comprador/', nuevo_comprador, name="nuevo_comprador"),
    path('nuevo_vendedor/', nuevo_vendedor, name="nuevo_vendedor"),
    path('nuevo_receptor/', nuevo_receptor, name="nuevo_receptor"),

    path('parte/', parte, name='parte')


]