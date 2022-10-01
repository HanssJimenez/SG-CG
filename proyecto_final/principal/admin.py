from django.contrib import admin
from principal.models import (Colaborador, Cliente,Credito, Producto, 
                              Existencia,Solicitud,UserProfileInfo, Inventario)
from principal.forms import  CrearInventarioForm

class CrearInventarioForm(admin.ModelAdmin):
   list_display = ['categoria', 'nombre_p', 'cantidad']
   form = CrearInventarioForm
   list_filter = ['categoria']
   search_fields = ['categoria', 'nombre_p']
   
# Register your models here.
admin.site.register(Inventario, CrearInventarioForm)
admin.site.register(Colaborador)
admin.site.register(Cliente)
admin.site.register(Credito)
admin.site.register(Producto)
admin.site.register(Existencia)
admin.site.register(Solicitud)
admin.site.register(UserProfileInfo)
