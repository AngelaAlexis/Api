from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Comprador, Proveedor
from .forms import CompradorForm, ProveedorForm
# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('lista_compradores')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


def home(request):
    return render(request, 'home.html')


def lista_compradores(request):
    compradores = Comprador.objects.all()
    return render(request, 'list_compradores.html', {'compradores': compradores})


def crear_comprador(request):
    if request.method == 'POST':
        form = CompradorForm(request.POST)
        if form.is_valid():
            # Guardar el comprador en la base de datos
            nuevo_comprador = form.save(commit=False)
            nuevo_comprador.user = request.user  # Asigna el usuario actual
            nuevo_comprador.save()
            # Redirige a donde desees después de guardar el comprador
            return redirect('lista_compradores')
    else:
        form = CompradorForm()

    return render(request, 'crear_comprador.html', {'form': form})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'list_proveedores.html', {'proveedores': proveedores})


def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            # Guardar el comprador en la base de datos
            nuevo_proveedor = form.save(commit=False)
            nuevo_proveedor.user = request.user  # Asigna el usuario actual
            nuevo_proveedor.save()
            # Redirige a donde desees después de guardar el comprador
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()

    return render(request, 'crear_proveedor.html', {'form': form})

\
@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('lista_compradores')
