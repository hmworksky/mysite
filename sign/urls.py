from django.conf.urls import url,include
from sign  import views

urlpatterns = [
    url(r'register', views.register, name='register'),
    url(r'index',views.index,name='index'),
    url(r'login',views.login,name = 'login'),
    url(r'reset',views.resetlogin,name = 'resetlogin'),
    url(r'interface/create/',views.interface_create,name = 'interface_create'),
    url(r'interface/return/',views.interface_return,name = 'interface_return'),
]
