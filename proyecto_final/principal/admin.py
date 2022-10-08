from django.contrib import admin
from principal.models import *
from principal.forms import  AgreProdForm

class AgreProdForm(admin.ModelAdmin):
   list_display = ['categoria', 'nombre_p', 'cantidad']
   form = AgreProdForm
   list_filter = ['categoria']
   search_fields = ['categoria', 'nombre_p']

class ClienteAdmin(admin.ModelAdmin):
   list_display = ['nombre','apellido','numtel']
   search_fields = ['nombre','apellido','numtel']
   list_filter = ['nombre']
   list_per_page = 10
      
# Register your models here.
admin.site.register(Inventario, AgreProdForm)
admin.site.register(Categorias)
admin.site.register(Colaborador)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Credito)
admin.site.register(Producto)
admin.site.register(Existencia)
admin.site.register(Solicitud)
admin.site.register(UserProfileInfo)
