from django.contrib import admin
from principal.models import *


# class AgreProdForm(admin.ModelAdmin):
#    list_display = ['categoria', 'nombre_p', 'cantidad']
#    form = AgreProdForm
#    list_filter = ['categoria']
#    search_fields = ['categoria', 'nombre_p']

# class ClienteAdmin(admin.ModelAdmin):
#    list_display = ['nombre','apellido','numtel']
#    search_fields = ['nombre','apellido','numtel']
#    list_filter = ['nombre']
#    list_per_page = 10
      
# Register your models here.
admin.site.register(Inventario)
admin.site.register(Categorias)
admin.site.register(Colaborador)
admin.site.register(Cliente)
admin.site.register(Credito)
admin.site.register(Solicitud)
admin.site.register(UserProfileInfo)
admin.site.register(Proveedor)
admin.site.register(ComprobanteCompra)
admin.site.register(UnidadCompra)
admin.site.register(DetalleComprobanteCompra)
admin.site.register(ComprobanteServicio)
admin.site.register(UnidadVendida)
admin.site.register(DetalleComprobanteServicio)

