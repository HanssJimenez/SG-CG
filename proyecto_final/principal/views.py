from django.shortcuts import render
from principal.forms import UserForm, UserProfileInfoForm
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'principal/index.html')

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
