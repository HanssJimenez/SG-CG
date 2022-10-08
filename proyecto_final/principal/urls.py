from django.conf.urls import url,include
from principal import views


app_name = 'principal'

urlpatterns =[
    url(r'^register/$', views.register, name = 'register'),
    url(r'^user_login/$',views.user_login, name='user_login'),
    
    
]
