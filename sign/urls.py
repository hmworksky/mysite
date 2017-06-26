from django.conf.urls import url,include
from sign  import views

urlpatterns = [
    url(r'register', views.register, name='register'),
    url(r'index',views.index,name='index'),
    url(r'login',views.login,name = 'login'),
    url(r'reset',views.resetlogin,name = 'resetlogin'),
]
