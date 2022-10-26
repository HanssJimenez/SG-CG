from django.contrib import admin
from principal.models import *

class InventarioAdmin(admin.ModelAdmin):
    list_display = ['id','categoria','nombre', 'cantidad', 'medida','borrado']
    readonly_fields = ['id','categoria','nombre', 'cantidad', 'medida']
    search_fields = ['id','categoria__nombre','nombre','medida']
    list_filter = ['nombre','categoria','medida']
    list_per_page = 10
    
        
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ['nombre','borrado']
    readonly_fields = ['nombre']
    search_fields = ['nombre']
    list_filter = ['nombre']
    list_per_page = 10
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','numtel', 'borrado']
    readonly_fields = ['nombre','apellido','numtel']
    search_fields = ['nombre','apellido','numtel']
    list_filter = ['nombre', 'apellido']
    list_per_page = 10
    
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['DPI','nombre','apellido', 'numero_de_telefono','puesto','fecha_de_nacimiento','sueldo','borrado']
    readonly_fields = ['DPI','nombre','apellido', 'numero_de_telefono','puesto','fecha_de_nacimiento','sueldo']
    search_fields = ['nombre','apellido','puesto', 'sueldo']
    list_filter = ['nombre', 'apellido', 'puesto']
    list_per_page = 10
    
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','telefono', 'direccion', 'correo','gestion', 'borrado']
    readonly_fields = ['id','nombre','telefono', 'direccion', 'correo','gestion']
    search_fields = ['nombre','correo','gestion']
    list_filter = ['nombre', 'correo']
    list_per_page = 10
    
class ComprobanteCompraAdmin(admin.ModelAdmin):
    list_display = ['nocomp','fecha','proveedor']
    readonly_fields = ['nocomp','fecha','proveedor']
    search_fields = ['nocomp','fecha','proveedor']
    list_filter = ['proveedor', 'fecha']
    list_per_page = 10

class UnidadCompraAdmin(admin.ModelAdmin):
    list_display = ['nocomp','inventario','cantidad', 'preciouni','totalprecio']
    readonly_fields = ['nocomp','inventario','cantidad', 'preciouni','totalprecio']
    search_fields = ['nocomp','inventario__nombre','totalprecio']
    list_filter = ['inventario__nombre']
    list_per_page = 10
    
        
class DetalleComprobanteCompraAdmin(admin.ModelAdmin):
    list_display = ['nocomp','destino','total']
    readonly_fields = ['nocomp','destino','total']
    list_per_page = 10

class ComprobanteServicioAdmin(admin.ModelAdmin):
    list_display = ['nocomp','fechav','nombre','telefono','direccion','servicio','correo']
    readonly_fields = ['nocomp','fechav','nombre','telefono','direccion','servicio','correo']
    search_fields = ['nocomp','nombre','fechav']
    list_filter = ['nombre', 'fechav']
    list_per_page = 10

class UnidadVendidaAdmin(admin.ModelAdmin):
    list_display = ['nocomp','inventario','cantidad', 'preciouni','totalprecio']
    readonly_fields = ['nocomp','inventario','cantidad', 'preciouni','totalprecio']
    search_fields = ['nocomp','inventario__nombre','totalprecio']
    list_filter = ['inventario__nombre']
    list_per_page = 10

class DetalleComprobanteServicioAdmin(admin.ModelAdmin):
    list_display = ['nocomp','tiposervicio','descripcion','total']
    readonly_fields = ['nocomp','tiposervicio','descripcion','total']
    list_per_page = 10
            
# Register your models here.
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Categorias,CategoriasAdmin)
admin.site.register(Colaborador,ColaboradorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(ComprobanteCompra,ComprobanteCompraAdmin)
admin.site.register(UnidadCompra,UnidadCompraAdmin)
admin.site.register(DetalleComprobanteCompra,DetalleComprobanteCompraAdmin)
admin.site.register(ComprobanteServicio,ComprobanteServicioAdmin)
admin.site.register(UnidadVendida,UnidadVendidaAdmin)
admin.site.register(DetalleComprobanteServicio,DetalleComprobanteServicioAdmin)

