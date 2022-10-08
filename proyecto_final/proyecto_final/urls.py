"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from principal import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^principal/', include('principal.urls', namespace='principal')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/', views.special,name='special'),
    #urls cliente
    url(r'^lista_cliente/', views.LeerCliente.as_view(),name='lista_cliente'),
    url(r'^crear_cliente/', views.CrearCliente.as_view(),name='crear_cliente'),
    url(r'^modificar_cliente/(?P<pk>\d+)/$', views.ModificarCliente.as_view(), name = 'modificar_cliente'),
    url(r'^borrar_cliente/(?P<pk>\d+)/$', views.EliminarCliente.as_view(), name = 'borrar_cliente'),
    #urls credito
    url(r'^lista_credito/', views.LeerCredito.as_view(),name='lista_credito'),
    url(r'^crear_credito/', views.CrearCredito.as_view(),name='crear_credito'),
    url(r'^modificar_credito/(?P<pk>\d+)/$', views.ModificarCredito.as_view(), name = 'modificar_credito'),
    url(r'^borrar_credito/(?P<pk>\d+)/$', views.EliminarCredito.as_view(), name = 'borrar_credito'),
    #urls colaborador
    url(r'^lista_colaborador/', views.LeerColaborador.as_view(),name='lista_colaborador'),
    url(r'^crear_colaborador/', views.CrearColaborador.as_view(),name='crear_colaborador'),
    url(r'^modificar_colaborador/(?P<pk>\d+)/$', views.ModificarColaborador.as_view(), name = 'modificar_colaborador'),
    url(r'^borrar_colaborador/(?P<pk>\d+)/$', views.EliminarColaborador.as_view(), name = 'borrar_colaborador'),
    #urls inventario
    url(r'^lista_inventario/', views.LeerInventario.as_view(),name='lista_inventario'),
    url(r'^crear_inventario/', views.CrearInventario.as_view(),name='crear_inventario'),
    url(r'^modificar_inventario/(?P<pk>\d+)/$', views.ModificarInventario.as_view(), name = 'modificar_inventario'),
    url(r'^borrar_inventario/(?P<pk>\d+)/$', views.EliminarInventario.as_view(), name = 'borrar_inventario'),
    #urls categorias
    url(r'^lista_categorias/', views.LeerCategorias.as_view(),name='lista_categorias'),
    url(r'^crear_categorias/', views.CrearCategorias.as_view(),name='crear_categorias'),
    url(r'^modificar_categorias/(?P<pk>\d+)/$', views.ModificarCategorias.as_view(), name = 'modificar_categorias'),
    url(r'^borrar_categorias/(?P<pk>\d+)/$', views.EliminarCategorias.as_view(), name = 'borrar_categorias'),
    #urls solicitud
    url(r'^lista_solicitud/', views.LeerSolicitud.as_view(),name='lista_solicitud'),
    url(r'^crear_solicitud/', views.CrearSolicitud.as_view(),name='crear_solicitud'),
    url(r'^modificar_solicitud/(?P<pk>\d+)/$', views.ModificarSolicitud.as_view(), name = 'modificar_solicitud'),
    url(r'^borrar_solicitud/(?P<pk>\d+)/$', views.EliminarSolicitud.as_view(), name = 'borrar_solicitud'),
    #urls inventario
    # url(r'^lista_producto/', views.lista_inventario,name='lista_producto'),
    # url(r'^agregar_producto/', views.agregar_producto_inventario,name='agregar_producto'),
    # url(r'^modificar_producto/(?P<pk>\d+)/$', views.modificar_producto_inventario, name = 'modificar_producto'),
    # url(r'^borrar_producto/(?P<pk>\d+)/$', views.borrar_producto_inventario, name = 'borrar_producto'),
]

handler404 = 'principal.views.error_404_view'
