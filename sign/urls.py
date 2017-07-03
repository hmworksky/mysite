from django.conf.urls import url
from sign  import login

urlpatterns = [
    url(r'register', login.register, name='register'),
    url(r'index',login.index,name='index'),
    url(r'login',login.login,name = 'login'),
    url(r'reset',login.resetlogin,name = 'resetlogin'),
]
