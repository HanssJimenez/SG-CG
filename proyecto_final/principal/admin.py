from django.contrib import admin
from principal.models import Colaborador, Cliente,Credito, Producto, Existencia,Solicitud, UserProfileInfo
# Register your models here.
admin.site.register(Colaborador)
admin.site.register(Cliente)
admin.site.register(Credito)
admin.site.register(Producto)
admin.site.register(Existencia)
admin.site.register(Solicitud)
admin.site.register(UserProfileInfo)
