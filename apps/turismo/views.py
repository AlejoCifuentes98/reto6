from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Categoria, Sitio
from .forms import categoria_agregar_form, sitio_agregar_form, login_form, registro_form

def inicio_view(request):
    sitios = Sitio.objects.filter()
    return render(request, 'turismo/inicio.html', locals())

def login_view(request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario =authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/mis_sitios/')
            else:
                msj = 'Sus credenciales son incorrectas, por favor verifique e intente nuevamente.'    
    formulario = login_form()
    return render(request, 'turismo/login.html', locals())

def registro_view(request):
    if request.method == 'POST':
        form_registro = registro_form(request.POST)
        if form_registro.is_valid():
            nombres = form_registro.cleaned_data['nombres']
            apellidos = form_registro.cleaned_data['apellidos']
            correo = form_registro.cleaned_data['correo']
            calve_1 = form_registro.cleaned_data['calve_1']
            clave_2 = form_registro.cleaned_data['clave_2']
            u = User.objects.create_user(first_name=nombres,last_name=apellidos, username=correo, password=clave_2, is_superuser=False, is_staff=True)
            u.save()
    else:
        form_registro = registro_form()
        return render(request, 'turismo/registro.html', locals())        
    return render(request, 'turismo/registro.html', locals())

def logout_view(request):
    logout(request)
    return redirect('/login/')
    

@login_required
def categorias_view(request):
    categorias = Categoria.objects.filter()
    return render(request, 'turismo/categorias.html', locals())

@login_required
def categoria_agregar_view(request):
    if request.method == 'POST':
        categoria_agregar = categoria_agregar_form(request.POST)
        if categoria_agregar.is_valid():
            categoria_agregar.save()
            return redirect('/categorias/')
    else:
        categoria_agregar = categoria_agregar_form()        
    return render(request, 'turismo/categoria_agregar.html', locals())

@login_required
def categoria_editar_view(request, id_categoria):
    categoria=Categoria.objects.get(id=id_categoria)
    if request.method == 'GET': 
        editar_categoria = categoria_agregar_form(instance=categoria)
    else:
        editar_categoria = categoria_agregar_form(request.POST, instance=categoria)
        if editar_categoria.is_valid():
            editar_categoria.save()
            return redirect('/categorias/')    
    return render(request, 'turismo/categoria_editar.html', locals())

@login_required
def categoria_eliminar_view(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method == 'POST':
        categoria.delete()
        return redirect('/categorias/')
    return render(request, 'turismo/categoria_eliminar.html', locals())


@login_required
def mis_sitios_view(request):
    usuario = User.objects.get(id = request.user.id)
    lista = Categoria.objects.filter(usuario = usuario)
    return render(request, 'turismo/mis_sitios.html', locals())

@login_required
def sitio_agregar_view(request):
    usuario = User.objects.get(id= request.user.id)
    if request.method == 'POST':
        sitio_agregar = sitio_agregar_form(request.POST)
        if sitio_agregar.is_valid():
            c = sitio_agregar.save(commit=False)
            c.usuario=usuario
            c.save()
            return redirect('/mis_sitios/')
    else:
        sitio_agregar = sitio_agregar_form() 
    return render(request, 'turismo/sitio_agregar.html', locals())

@login_required
def sitio_editar_view(request, id_sitio):
    sitio=Sitio.objects.get(id=id_sitio)
    if request.method == 'GET': 
        editar_sitio = sitio_agregar_form(instance=sitio)
    else:
        editar_sitio = sitio_agregar_form(request.POST, instance=sitio)
        if editar_sitio.is_valid():
            editar_sitio.save()
            return redirect('/mis_sitios/')    
    return render(request, 'turismo/sitio_editar.html', locals())

@login_required
def sitio_eliminar_view(request, id_sitio):
    sitio = Sitio.objects.get(id=id_sitio)
    if request.method == 'POST':
        sitio.delete()
        return redirect('/mis_sitios/')
    return render(request, 'turismo/sitio_eliminar.html', locals())

def reportes_view(request):
    return render(request, 'turismo/reportes.html', locals())
