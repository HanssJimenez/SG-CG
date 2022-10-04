from django.conf.urls import url,include
from principal import views


nombre_app = 'principal'

urlpatterns =[
    url(r'^lista_inventario/$',views.InventarioListView.as_view(),name='lista'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^user_login/$',views.user_login, name='user_login'),
    
    
]
