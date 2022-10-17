from cProfile import label
from django import forms
from django.contrib.auth.models import User
from principal.models import *
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date
import datetime

class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()

class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    vpassword = forms.CharField(widget= forms.PasswordInput())
    email = Lowercase(
        label = 'Correo', min_length=8, max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message= "Ingrese una dirección de correo valida")],
        widget=forms.TextInput(attrs={'placeholder':'ingrese correo'})
    )
    class Meta():
        model = User
        ordering = ['-pk']
        fields = ('username', 'email', 'password')
    def clean(self):
        cleaned_data = super().clean()
        p = cleaned_data['password']
        vp = cleaned_data['vpassword']
        if p != vp:
            raise forms.ValidationError('La constraseña no es igual')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        ordering = ['-pk']
        fields = ('portfolio_site','profile_pic')

class ClienteForm(forms.ModelForm):
    nombre = forms.CharField(
        label= 'Nombre', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="Solo debe ingresar letras")],
        widget=forms.TextInput(attrs={'placeholder':'ingrese nombres'})
    )
    apellido = forms.CharField(
        label= 'apellido', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="Solo debe ingresar letras")],
        widget=forms.TextInput(attrs={'placeholder':'ingrese apellido'})
    )
    
    class Meta:
        model = Cliente
        ordering = ['-pk']
        fields = "__all__"
        
        widgets={
            'numtel': forms.TextInput( 
                attrs={
                    'placeholder':'ingrese número',
                    'data-mask': '0000-0000'
                }
                
            )
        }

#Form de colaborador
class ColaboradorForm(forms.ModelForm):
    DPI = forms.CharField(
        label= 'DPI', min_length=13, max_length=13, 
        validators=[RegexValidator(r'^[0-9]*$',
        message="Solo debe ingresar números")],
        widget=forms.TextInput(attrs={'placeholder':'ingrese DPI'})
    )
    nombre = forms.CharField(
        label= 'Nombre', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="Solo debe ingresar letras")],
        widget=forms.TextInput(attrs={'placeholder':'ingrese nombres'})
    )
    apellido = forms.CharField(
        label= 'Apellido', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="Solo debe ingresar letras")],
        widget=forms.TextInput(attrs={'placeholder':'ingrese apellido'})
    )
    puesto = forms.CharField(
        label= 'Puesto', min_length=10, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="Solo debe ingresar letras")],
        widget=forms.TextInput(attrs={'placeholder':'ingrese puesto'})
    )
    sueldo = forms.CharField(
        label= 'Sueldo', min_length=4, max_length=5, 
        validators=[RegexValidator(r'^[0-9]*$',
        message="Solo debe ingresar números")],
        widget=forms.TextInput(attrs={'placeholder':'ingrese sueldo'})
    )
    
    class Meta:
        model = Colaborador
        ordering = ['-pk']
        fields = "__all__"
        widgets = {
            'numero_de_telefono': forms.TextInput(
                attrs={
                    'placeholder':'ingrese número',
                    'data-mask': '0000-0000',
                }
                
            ),
            'fecha_de_nacimiento':forms.DateInput(
                attrs={
                    'type':'date',
                    'onkeydown':'return false',
                    'min':'1950-01-01',
                    'max':'2030-01-01'
                    
                }
            ),
        }
    def clean_DPI(self):
        dpi = self.cleaned_data.get('DPI')
        pk2 = self.cleaned_data.get('pk')
        for obj in Colaborador.objects.all():
            if (obj.pk == pk2 and obj.DPI == dpi):
                raise forms.ValidationError('Denegado! '+ dpi +' ya existe en los registros')
        return dpi
    
    def clean_numero_de_telefono(self):
        numero_de_telefono = self.cleaned_data.get('numero_de_telefono')
        if len(numero_de_telefono) != 9:
            raise forms.ValidationError('Número de telefono incompleto')
        return numero_de_telefono
    def clean_fecha_de_nacimiento(self):
        fecha_de_nacimiento = self.cleaned_data.get('fecha_de_nacimiento')
        
        f = fecha_de_nacimiento
        a = date.today()
        edad = (a.year - f.year) - ((a.month, a.day) < (f.month, f.day))
        
        if edad < 18 or edad > 65:
            raise forms.ValidationError('Denegado! la edad debe de ser entre 18 a 65 años')
        return fecha_de_nacimiento
#Form de Credito
class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        ordering = ['-pk']
        fields = "__all__"
#Form de Inventario
class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        ordering = ['-pk']
        fields = ('categoria', 'nombre_p', 'cantidad')
#Form de Categoria
class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        ordering = ['-pk']
        fields = "__all__"


#Form de Venta
class SolicitudForm(forms.ModelForm):
    
    class Meta:
        model = Solicitud
        ordering = ['-pk']
        fields = "__all__"
        widgets = {
            'fecha':forms.DateInput(
                attrs={
                    'type':'date',
                    'onkeydown':'return false',
                    'min':'1950-01-01',
                    'max':'2030-01-01'
                    
                }
            ),
        }
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha > datetime.date.today() or fecha < datetime.date.today():
            raise forms.ValidationError('La fecha debe ser de hoy')
        return fecha