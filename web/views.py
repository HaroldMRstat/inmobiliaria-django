from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Propiedad
from .decoradores import solo_trabajadores  # Importamos el decorador

def agentes(request):
    return render(request, 'web/agentes.html')

def testimonios(request):
    return render(request, 'web/testimonios.html')

def lista_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'web/lista_propiedades.html', {'propiedades': propiedades})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        
        if not username or not password:
            messages.error(request, "Por favor, completa todos los campos.")
            return render(request, 'web/login.html')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            
            # Redirigir según el tipo de usuario
            if user.is_staff:
                return redirect('lista_propiedades')  # Dashboard de trabajadores
            else:
                return redirect('index')  # Página principal para clientes

        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, 'web/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Cerraste sesión correctamente.")
    return redirect('login')

def formulario_contacto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        celular = request.POST.get('celular')
        dni = request.POST.get('dni')
        return render(request, 'web/gracias.html', {'nombre': nombre})
    return render(request, 'web/index.html')

def index(request):
    return render(request, 'web/index.html')

@login_required
@solo_trabajadores
def subir_propiedad(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        imagen = request.FILES.get("imagen")  # Si suben imágenes
        
        Propiedad.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            precio=precio,
            imagen=imagen
        )
        messages.success(request, "Propiedad subida con éxito.")
        return redirect('lista_propiedades')

    return render(request, 'web/subir_propiedad.html')
