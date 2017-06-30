from django.conf.urls import url,include
from sign  import login

urlpatterns = [
    url(r'register', login.register, name='register'),
    url(r'index',login.index,name='index'),
    url(r'login',login.login,name = 'login'),
    url(r'reset',login.resetlogin,name = 'resetlogin'),
    url(r'interface/create/',interface.interface_create,name = 'interface_create'),
    url(r'interface/return/',interface.interface_return,name = 'interface_return'),
    url(r'interface/list/',interface.interface_list,name = 'interface_list'),
]
