from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank= True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank= True)

    def __str__(self):
        return self.user.username

class Colaborador(models.Model):
    DPI = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_de_telefono = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()
    sueldo = models.PositiveIntegerField()
    def __str__(self):
        return self.nombre+" "+self.apellido


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numtel = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre+" "+self.apellido

class Credito(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    
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
    nombre = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return(self).nombre.nombre

class Solicitud(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250, blank=True , null=True)
    fecha = models.DateField(blank=True, null=True)
    pago = models.PositiveIntegerField()
    credito = models.BooleanField()

    def __str__(self):
        return(self).cliente.nombre



class Categorias(models.Model):
    nombre = models.CharField(max_length=50,blank=False, null=False)
    
    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre_p = models.CharField(max_length=50, blank=False)
    cantidad = models.PositiveIntegerField(default = 0, blank= False, null=True)
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


