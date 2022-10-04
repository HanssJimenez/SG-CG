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
    url(r'^lista_producto/', views.lista_inventario,name='lista_producto'),
    url(r'^agregar_producto/', views.agregar_producto_inventario,name='agregar_producto'),
    url(r'^cuadros/', views.cuadros, name='cuadros'),
    
]

handler404 = 'principal.views.error_404_view'
