from email.policy import default
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank= True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank= True)

    def __str__(self):
        return self.user.username
    
############################### Inventario

MEDIDA = (
    ('unidad', 'unidad'),
    ('gramos', 'gramos'),
    ('miligramos', 'mililitro')
)

class Categorias(models.Model):
    nombre = models.CharField(max_length=50,blank=False, null=False)
    borrado = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"
    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50, blank=False)
    cantidadmin = models.PositiveIntegerField(default = 0, blank= True, null=True)
    cantidad = models.PositiveIntegerField(default = 0, blank= False, null=True)
    medida = models.CharField(max_length=10, choices=MEDIDA, default='u')
    borrado = models.BooleanField(default = False)
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = "Inventario"
    def __str__(self):
        return self.nombre + " " + self.medida


############################## Compras ##################################


class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField(max_length=254, unique=True)
    gestion = models.CharField(max_length=15, unique=True)
    borrado = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = "Proveedores"
    def __str__(self):
        return self.nombre


#contains the purchase bills made
class ComprobanteCompra(models.Model):
    nocomp = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE, related_name='proveedorcompra')
    class Meta:
        verbose_name = 'Comprobante de compra'
        verbose_name_plural = "Comprobantes de compras"
    def __str__(self):
        return "Comprobante no: " + str(self.nocomp)
    def get_lista_unidad(self):
        return UnidadCompra.objects.filter(nocomp=self)

    def get_total_precio(self):
        unidadcompra = UnidadCompra.objects.filter(nocomp=self)
        total = 0
        for item in unidadcompra:
            total += item.totalprecio
        return total

#contains the purchase stocks made
class UnidadCompra(models.Model):
    nocomp = models.ForeignKey(ComprobanteCompra, on_delete = models.CASCADE, related_name='comprobantecomprano')
    inventario = models.ForeignKey(Inventario, on_delete = models.CASCADE, related_name='unidadcompra')
    cantidad = models.IntegerField(default=1)
    preciouni = models.IntegerField(default=1)
    totalprecio = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Unidad compra'
        verbose_name_plural = "Unidades compradas"
    def __str__(self):
        return "Comprobante no: " + str(self.nocomp.nocomp) + ", Producto = " + self.inventario.nombre 

#contains the other details in the purchases bill
class DetalleComprobanteCompra(models.Model):
    nocomp = models.ForeignKey(ComprobanteCompra, on_delete = models.CASCADE, related_name='detallecomprobantecompra')
    destino = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        verbose_name = 'Detalle de compra'
        verbose_name_plural = "Detalles de compras"
    def __str__(self):
        return "Comprobante no: " + str(self.nocomp.nocomp)
    

##################### Servicios ############################
#contains the sale bills made
class ComprobanteServicio(models.Model):
    nocomp = models.AutoField(primary_key=True)
    fechav = models.DateTimeField(auto_now=True)
    
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=200)
    servicio = models.PositiveIntegerField(max_length=100)
    correo = models.EmailField(max_length=254)
    gestion = models.CharField(max_length=15, blank=True, null=True)
    class Meta:
        verbose_name = 'Comprobante de servicio'
        verbose_name_plural = "Comprobantes de servicios"
    def __str__(self):
        return "No. Comprobante: " + str(self.nocomp)

    def get_lista_unidades(self):
        return UnidadVendida.objects.filter(nocomp=self)
        
    def get_precio_total(self):
        unidadesvendidas = UnidadVendida.objects.filter(nocomp=self)
        subtot = self.servicio
        total = 0
        for item in unidadesvendidas:
            total += item.totalprecio 
        total += subtot
        return total

#contains the sale stocks made
class UnidadVendida(models.Model):
    nocomp = models.ForeignKey(ComprobanteServicio, on_delete = models.CASCADE, related_name='compnoventa')
    inventario = models.ForeignKey(Inventario, on_delete = models.CASCADE, related_name='unidadvendida')
    cantidad = models.IntegerField(default=1)
    preciouni = models.IntegerField(default=1)
    totalprecio = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Unidad Vendida'
        verbose_name_plural = "Unidades Vendidas"
    def __str__(self):
        return "No. Comprobante: " + str(self.nocomp.nocomp) + ", unidad = " + self.inventario.nombre

#contains the other details in the sales bill
class DetalleComprobanteServicio(models.Model):
    nocomp = models.ForeignKey(ComprobanteServicio, on_delete = models.CASCADE, related_name='saledetailsbillno')
    tiposervicio= models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        verbose_name = 'Detalle de servicio'
        verbose_name_plural = "Detalle de servicios"
    def __str__(self):
        return "No. Comprobante: " + str(self.nocomp.nocomp)


class Colaborador(models.Model):
    DPI = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_de_telefono = models.CharField(max_length=100, verbose_name="Número de teléfono")
    puesto = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    sueldo = models.PositiveIntegerField()
    borrado = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = "Colaboradores"
    def clean(self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        self.puesto = self.puesto.capitalize()
    def __str__(self):
        return self.nombre+" "+self.apellido

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numtel = models.CharField(max_length=9, verbose_name="Número de teléfono")
    borrado = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.nombre+" "+self.apellido

class Solicitud(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT, verbose_name='Clientes existentes')
    colaborador = models.ForeignKey(Colaborador,on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=250, blank=True , null=True)
    fecha = models.DateField(blank=True, null=True)
    monto = models.PositiveIntegerField(blank = True, null = True)
    credito = models.BooleanField()
    borrado = models.BooleanField(default=False)
    def __str__(self):
        return(self).cliente.nombre
    
class Credito(models.Model):
    solicitud = models.ForeignKey(Cliente,on_delete=models.PROTECT)
    total = models.IntegerField()
    borrado = models.BooleanField(default=False)
    def __str__(self):
        return(self).solicitud.nombre
    

ESTADOS = (
    ('Pendiente', 'Pendiente'),
    ('Procesando', 'Procesando'),
    ('Entregado', 'Entregado')
)

