from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Localidad, Persona
from .form import ClienteForm, LocalidadForm
from django.contrib import messages

# Create your views here.


def pagina_principal(request, template_name='admin_clientes/pagina_principal.html'):
    return render(request, template_name)


def index(request, template_name='admin_clientes/index.html'):
    return render(request, template_name)


def registrate(request, template_name='admin_clientes/registrate.html'):
    if request.method == 'GET':
        dato = {
            'form': UserCreationForm
        }
        return render(request, template_name, dato)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                dato = {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                }
                return render(request, template_name, dato)
        dato = {
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
        }
        return render(request, template_name, dato)


def iniciar_sesion(request, template_name='admin_clientes/iniciar_sesion.html'):
    if request.method == 'GET':
        dato = {
            'form': AuthenticationForm
        }
        return render(request, template_name, dato)
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
            )
        if user is None:
            dato = {
            'form': AuthenticationForm,
            'error': 'Nombre de usuario o contraseña son incorrectos'
        }
            return render(request, template_name, dato)
        else:
            login(request, user)
            return redirect('index')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('pagina_principal')

@login_required
def localidades(request, template_name='admin_clientes/localidades.html'):
    localidades_lista = Localidad.objects.all()
    messages.success(request, "Localidades listado!")
    dato = {
        "localidades": localidades_lista
    }
    return render(request, template_name, dato)

@login_required
def clientes(request, template_name='admin_clientes/clientes.html'):
    clientes_lista = Persona.objects.all()
    messages.success(request, "Clientes listado!")
    dato = {
        "clientes": clientes_lista
    }
    return render(request, template_name, dato)

@login_required
def nueva_localidad(request, template_name='admin_clientes/localidad_form.html'):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "¡Localidad registrada!")
            return redirect('localidades')
    else:
        form = LocalidadForm()
    dato = {
        "form": form
    }
    return render(request, template_name, dato)

@login_required
def modificar_localidad(request, pk, template_name='admin_clientes/localidad_form.html'):
    localidad = Localidad.objects.get(id=pk)
    form = LocalidadForm(request.POST or None, instance=localidad)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "¡Localidad modificada!")
            return redirect('localidades')
    datos = {
        "form": form
    }
    return render(request, template_name, datos)

@login_required
def eliminar_localidad(request, pk):
    localidad = Localidad.objects.get(id=pk)
    localidad.delete()
    messages.success(request, "¡Localidad eliminada!")
    return redirect('localidades')

@login_required
def nuevo_cliente(request, template_name='admin_clientes/cliente_form.html'):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "¡Cliente registrado!")
            return redirect('clientes')
    else:
        form = ClienteForm()
    dato = {
        "form": form
    }
    return render(request, template_name, dato)

@login_required
def modificar_cliente(request, pk, template_name='admin_clientes/cliente_form.html'):
    cliente = Persona.objects.get(id=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "¡Cliente modificado!")
            return redirect('clientes')
    datos = {
        "form": form
    }
    return render(request, template_name, datos)

@login_required
def eliminar_cliente(request, pk):
    cliente = Persona.objects.get(id=pk)
    cliente.delete()
    messages.success(request, "¡Cliente eliminado!")
    return redirect('clientes')
