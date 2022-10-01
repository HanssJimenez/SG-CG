from django.shortcuts import render, redirect
from principal.forms import CrearInventarioForm, UserForm, UserProfileInfoForm
from principal.models import Inventario
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'principal/index.html')

@login_required
def agregar_producto_inventario(request):
    form_agpr = CrearInventarioForm(data=request.POST)
    if form_agpr.is_valid():
        form_agpr.save()
        return redirect('/lista_producto')
        
    context = {
        "form_agpr": form_agpr,
	    "title": "Añadir producto",
    }
    return render(request, "principal/añadir_producto_inventario.html", context)

@login_required
def lista_inventario(request):
	title = 'Lista inventario'
	queryset = Inventario.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "principal/lista_producto.html", context)

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

    return render(request, 'principal/registration.html',
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

