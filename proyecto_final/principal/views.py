from urllib import request
from django.db.models import Q # Required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from principal.forms import (UserForm, UserProfileInfoForm)
from principal.models import *


# Create your views here.

class AccesoUsuarioColaborador(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),
                                    self.get_login_url(),self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/no_posee_permisos/')
        return super(AccesoUsuarioColaborador, self).dispatch(request, *args, **kwargs)

# Vistas inicio
def index(request):
    return render(request, 'principal/index.html')

def no_permisos(request):
    return render(request, 'principal/no_posee_permisos.html')

# ClassBaseViews Colaborador Crear/Modificar/Eliminar/Leer
#Crear

class CrearColaborador(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_colaborador')
    model = Colaborador
    fields = '__all__'
    success_url = reverse_lazy('lista_colaborador')
#Modificar
class ModificarColaborador(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_colaborador')
    model = Colaborador
    fields = '__all__'
    success_url = reverse_lazy('lista_colaborador')
#Eliminar
class EliminarColaborador(AccesoUsuarioColaborador,DeleteView):
    permission_required = ('principal.delete_colaborador')
    queryset = Colaborador.objects.all()
    success_url = reverse_lazy('lista_colaborador')
#Leer
class LeerColaborador(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_colaborador')
    model = Colaborador
    queryset = Colaborador.objects.all()
    paginate_by = 5
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(
                Q(DPI__icontains=q) | Q(nombre__icontains=q) | Q(apellido__icontains=q)
                | Q(numero_de_telefono__icontains=q) | Q(puesto__icontains=q) | Q(fecha_de_nacimiento__icontains=q)
                | Q(sueldo__icontains=q)
            )
        else:
            object_list = self.model.objects.all()
        return object_list
    
    
# ClassBaseViews Credito Crear/Modificar/Eliminar/Leer
#Crear
class CrearCredito(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_credito')
    model = Credito
    fields = '__all__'
    success_url = reverse_lazy('lista_credito')
#Modificar
class ModificarCredito(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_credito')
    model = Credito
    fields = '__all__'
    success_url = reverse_lazy('lista_credito')
#Eliminar
class EliminarCredito(AccesoUsuarioColaborador,DeleteView):
    permission_required = ('principal.delete_credito')
    queryset = Credito.objects.all()
    success_url = reverse_lazy('lista_credito')
#Leer
class LeerCredito(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_credito')
    model = Credito
    queryset = Credito.objects.all()
    paginate_by = 10
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(
                Q(cliente__nombre__icontains=q) | Q(total__icontains=q) 
            )
        else:
            object_list = self.model.objects.all()
        return object_list
# ClassBaseViews Clientes Crear/Modificar/Eliminar/Leer
#Crear
class CrearCliente(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_cliente')
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('lista_cliente')
#Modificar
class ModificarCliente(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_cliente')
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('lista_cliente')

#Eliminar
class EliminarCliente(AccesoUsuarioColaborador,DeleteView):
    permission_required = ('principal.delete_cliente')
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('lista_cliente')
    
#Leer
class LeerCliente(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_cliente')
    model = Cliente
    queryset = Cliente.objects.all()
    paginate_by = 10
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(
                Q(nombre__icontains=q) | Q(apellido__icontains=q) | Q(numtel__icontains=q) 
            )
        else:
            object_list = self.model.objects.all()
        return object_list

# ClassBaseViews Inventario Crear/Modificar/Eliminar/Leer
#Crear
class CrearInventario(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_inventario')
    model = Inventario
    fields = ('categoria', 'nombre_p', 'cantidad')
    success_url = reverse_lazy('lista_inventario')
#Modificar
class ModificarInventario(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_inventario')
    model = Inventario
    fields = ('categoria', 'nombre_p', 'cantidad')
    success_url = reverse_lazy('lista_inventario')
#Eliminar
class EliminarInventario(AccesoUsuarioColaborador,DeleteView):
    permission_required = ('principal.delete_inventario')
    queryset = Inventario.objects.all()
    success_url = reverse_lazy('lista_inventario')
#Leer
class LeerInventario(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_inventario')
    model = Inventario
    queryset = Inventario.objects.all()
    paginate_by = 10
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(
                Q(nombre_p__icontains=q) | Q(categoria__nombre__icontains=q) | Q(cantidad__icontains=q) 
            )
        else:
            object_list = self.model.objects.all()
        return object_list

# ClassBaseViews Inventario Crear/Modificar/Eliminar/Leer
#Crear
class CrearCategorias(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_categorias')
    model = Categorias
    fields = '__all__'
    success_url = reverse_lazy('lista_categorias')
#Modificar
class ModificarCategorias(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_categorias')
    model = Categorias
    fields = '__all__'
    success_url = reverse_lazy('lista_categorias')
#Eliminar
class EliminarCategorias(AccesoUsuarioColaborador,DeleteView):
    permission_required = ('principal.delete_categorias')
    queryset = Categorias.objects.all()
    success_url = reverse_lazy('lista_categorias')
#Leer
class LeerCategorias(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_categorias')
    model = Categorias
    queryset = Categorias.objects.all()
    paginate_by = 10
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(
                Q(nombre__icontains=q) 
            )
        else:
            object_list = self.model.objects.all()
        return object_list

# ClassBaseViews Solicitud Crear/Modificar/Eliminar/Leer
#Crear
class CrearSolicitud(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_solicitud')
    model = Solicitud
    fields = '__all__'
    success_url = reverse_lazy('lista_solicitud')
#Modificar
class ModificarSolicitud(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_solicitud')
    model = Solicitud
    fields = '__all__'
    success_url = reverse_lazy('lista_solicitud')
#Eliminar
class EliminarSolicitud(AccesoUsuarioColaborador,DeleteView):
    permission_required = ('principal.delete_solicitud')
    queryset = Solicitud.objects.all()
    success_url = reverse_lazy('lista_solicitud')
#Leer
class LeerSolicitud(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_solicitud')
    model = Solicitud
    queryset = Solicitud.objects.all()
    paginate_by = 10
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(
                Q(cliente__nombre__icontains=q) | Q(colaborador__nombre__icontains=q) | Q(descripcion__icontains=q) 
                | Q(fecha__icontains=q) | Q(pago__icontains=q)
            )
        else:
            object_list = self.model.objects.all()
        return object_list

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


