from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('index', views.index, name='index'),
    path('registrate', views.registrate, name='signup'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('clientes', views.clientes, name='clientes'),
    path('localidades', views.localidades, name='localidades'),
    path('nueva_localidad', views.nueva_localidad, name='nueva_localidad'),
    path('nuevo_cliente', views.nuevo_cliente, name='nuevo_cliente'),
    path('modificar_localidad/<int:pk>', views.modificar_localidad, name='modificar_localidad'),
    path('eliminar_localidad/<int:pk>', views.eliminar_localidad, name='eliminar_localidad'),
    path('modificar_cliente/<int:pk>', views.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:pk>', views.eliminar_cliente, name='eliminar_cliente')
]
