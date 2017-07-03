# -*- coding:utf-8 -*-
from django.conf.urls import url

from interface_control import interface
urlpatterns = [
    url(r'create/', interface.interface_create, name ='interface_create'),
    url(r'return/', interface.interface_return, name ='interface_return'),
    url(r'list/', interface.interface_list, name ='interface_list'),
]
