from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from principal.forms import (UserForm, UserProfileInfoForm)
from principal.models import *


# Create your views here.

# Vistas inicio
def index(request):
    return render(request, 'principal/index.html')

# ClassBaseViews Colaborador Crear/Modificar/Eliminar/Leer
#Crear
class CrearColaborador(CreateView):
    model = Colaborador
    fields = '__all__'
    success_url = reverse_lazy('lista_colaborador')
#Modificar
class ModificarColaborador(UpdateView):
    model = Colaborador
    fields = '__all__'
    success_url = reverse_lazy('lista_colaborador')
#Eliminar
class EliminarColaborador(DeleteView):
    queryset = Colaborador.objects.all()
    success_url = reverse_lazy('lista_colaborador')
#Leer
class LeerColaborador(ListView):
    model = Colaborador
    queryset = Colaborador.objects.all()

# ClassBaseViews Credito Crear/Modificar/Eliminar/Leer
#Crear
class CrearCredito(CreateView):
    model = Credito
    fields = '__all__'
    success_url = reverse_lazy('lista_credito')
#Modificar
class ModificarCredito(UpdateView):
    model = Credito
    fields = '__all__'
    success_url = reverse_lazy('lista_credito')
#Eliminar
class EliminarCredito(DeleteView):
    queryset = Credito.objects.all()
    success_url = reverse_lazy('lista_credito')
#Leer
class LeerCredito(ListView):
    model = Credito
    queryset = Credito.objects.all()

# ClassBaseViews Clientes Crear/Modificar/Eliminar/Leer
#Crear
class CrearCliente(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('lista_cliente')
#Modificar
class ModificarCliente(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('lista_cliente')

#Eliminar
class EliminarCliente(DeleteView):
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('lista_cliente')
    
#Leer
class LeerCliente(ListView):
    model = Cliente
    queryset = Cliente.objects.all()

# ClassBaseViews Inventario Crear/Modificar/Eliminar/Leer
#Crear
class CrearInventario(CreateView):
    model = Inventario
    fields = ('categoria', 'nombre_p', 'cantidad')
    success_url = reverse_lazy('lista_inventario')
#Modificar
class ModificarInventario(UpdateView):
    model = Inventario
    fields = ('categoria', 'nombre_p', 'cantidad')
    success_url = reverse_lazy('lista_inventario')
#Eliminar
class EliminarInventario(DeleteView):
    queryset = Inventario.objects.all()
    success_url = reverse_lazy('lista_inventario')
#Leer
class LeerInventario(ListView):
    model = Inventario
    queryset = Inventario.objects.all()

# ClassBaseViews Inventario Crear/Modificar/Eliminar/Leer
#Crear
class CrearCategorias(CreateView):
    model = Categorias
    fields = '__all__'
    success_url = reverse_lazy('lista_categorias')
#Modificar
class ModificarCategorias(UpdateView):
    model = Categorias
    fields = '__all__'
    success_url = reverse_lazy('lista_categorias')
#Eliminar
class EliminarCategorias(DeleteView):
    queryset = Categorias.objects.all()
    success_url = reverse_lazy('lista_categorias')
#Leer
class LeerCategorias(ListView):
    model = Categorias
    queryset = Categorias.objects.all()

# ClassBaseViews Solicitud Crear/Modificar/Eliminar/Leer
#Crear
class CrearSolicitud(CreateView):
    model = Solicitud
    fields = '__all__'
    success_url = reverse_lazy('lista_solicitud')
#Modificar
class ModificarSolicitud(UpdateView):
    model = Solicitud
    fields = '__all__'
    success_url = reverse_lazy('lista_solicitud')
#Eliminar
class EliminarSolicitud(DeleteView):
    queryset = Solicitud.objects.all()
    success_url = reverse_lazy('lista_solicitud')
#Leer
class LeerSolicitud(ListView):
    model = Solicitud
    queryset = Solicitud.objects.all()

# Views de inventario / agregar / actualizar/ eliminar
# @login_required
# def agregar_producto_inventario(request):
#     form_agpr = AgreProdForm(data=request.POST)
#     if form_agpr.is_valid():
#         form_agpr.save()
#         return redirect('/lista_producto')
        
#     context = {
#         "form_agpr": form_agpr,
#         "title": "Añadir producto",
#     }
#     return render(request, "principal/añadir_producto_inventario.html", context)

# @login_required
# def modificar_producto_inventario(request, pk):
#     queryset = Inventario.objects.get(id=pk)
#     form = ModInvForm(instance=queryset)
#     if request.method == 'POST':
#         form = ModInvForm(request.POST, instance=queryset)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('lista_producto'))

#     context = {
# 		'form':form
# 	}
#     return render(request, 'principal/añadir_producto_inventario.html', context)

# def borrar_producto_inventario(request, pk):
# 	queryset = Inventario.objects.get(id=pk)
# 	if request.method == 'POST':
# 		queryset.delete()
# 		return HttpResponseRedirect(reverse('lista_producto'))
		
# 	return render(request, 'principal/borrar_producto_inventario.html')

# # Vistas para tablas

# @login_required
# def lista_inventario(request):
# 	title = 'Lista inventario'
# 	form = BusquedProductoForm(request.POST)
# 	queryset = Inventario.objects.all()
# 	context = {
# 		"title": title,
# 		"queryset": queryset,
# 	}
# 	if request.method == 'POST':
# 		queryset = Inventario.objects.filter(categoria__icontains=form['categoria'].value(),
# 									nombre_p__icontains=form['nombre_p'].value()
# 									)
# 		context = {
# 		"form": form,
# 		"queryset": queryset,
# 	}
# 	return render(request, "principal/lista_producto.html", context)
	

@login_required
def special(request):
    return HttpResponse('Iniciaste sesión!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registrado = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registrado = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'principal/register.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registrado':registrado})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('La Cuenta no esta activa')
        else:
            print('Alguien intento entrar')
            print('Username:{} and password {}'.format(username, password))
            return HttpResponse('datos de login invalidos')
    else:
        return render(request,'principal/login.html',{})

def cuadros (request):
    return render(request, 'principal/charts.html')

def error_404_view(request, exception):
    return render(request, 'principal/404.html')


