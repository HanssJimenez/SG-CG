from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    portfolio_site = models.URLField(blank= True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank= True)

    def __str__(self):
        return self.user.username

class Colaborador(models.Model):
    DPI = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numtel = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    fnaci = models.DateField()
    sueldo = models.IntegerField()
    def __str__(self):
        return(self).nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numtel = models.CharField(max_length=100)

    def __str__(self):
        return(self).nombre

class Credito(models.Model):
    cliente = models.ForeignKey(Cliente)
    total = models.IntegerField()

    def __str__(self):
        return(self).cliente.nombre

class Producto(models.Model):
    idproducto = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.IntegerField()

    def __str__(self):
        return(self).nombre

class Existencia(models.Model):
    nombre = models.ForeignKey(Producto)
    cantidad = models.IntegerField()

    def __str__(self):
        return(self).nombre.nombre

class Solicitud(models.Model):
    cliente = models.ForeignKey(Cliente)
    colaborador = models.ForeignKey(Colaborador)
    pago = models.IntegerField()
    credito = models.BooleanField()

    def __str__(self):
        return(self).cliente.nombre

class Inventario(models.Model):
    categoria = models.CharField(max_length=50, blank=True, null=True)
    nombre_p = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.PositiveIntegerField(default = 0, blank= True, null=True)
    agg_cantidad = models.PositiveIntegerField(default = 0, blank= True, null=True)
    agg_por= models.CharField(max_length=50, blank = True, null =True)
    cantidad_pedido= models.PositiveIntegerField(default= 0, blank = True, null=True)
    pedido_por=models.CharField(max_length=50, blank = True, null =True)
    pedido_a = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    creado_por = models.CharField(max_length=50, blank=True, null=True)
    reganizar_nvl = models.IntegerField(default='0', blank=True, null=True)
    actualizacion_reciente = models.DateTimeField(auto_now_add=False, auto_now=True)
    exportar_a_CSV = models.BooleanField(default=False)

    def __str__(self):
    	return self.nombre_p