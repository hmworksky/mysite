# -*- coding:utf-8 -*-
from django.conf.urls import url

from interface_control import interface
urlpatterns = [
    url(r'create/', interface.interface_create, name ='interface_create'),
    url(r'return/', interface.interface_return, name ='interface_return'),
    url(r'list/', interface.interface_list, name ='interface_list'),
    url(r'detail/(\d+)/$', interface.interface_detail, name ='interface_detail'),
    url(r'edit/(\d+)/$', interface.interface_edit, name ='interface_edit'),
    url(r'delete/(\d+)/$', interface.interface_delete, name ='interface_delete'),
    url(r'index/$', interface.index, name ='index'),
    url(r'zf/$', interface.zfv2_touzhu, name ='zfv2_touzhu'),
    # url(r'start/(\d+)/(\d+)/$', interface.interface_delete, name ='interface_start'),
]
