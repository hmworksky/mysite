# -*- coding:utf-8 -*-
from django.conf.urls import url
from interface_control import interface
urlpatterns = [
    url(r'create/', interface.interface_create, name ='interface_create'),
    url(r'return/', interface.interface_return, name ='interface_return'),
    url(r'return_new/', interface.interface_return_new, name ='interface_return_new'),
    url(r'list/', interface.interface_list, name ='interface_list'),
    url(r'detail/(\d+)/$', interface.interface_detail, name ='interface_detail'),
    url(r'edit/(\d+)/$', interface.interface_edit, name ='interface_edit'),
    url(r'delete/(\d+)/$', interface.interface_delete, name ='interface_delete'),
    url(r'index/$', interface.index, name ='index'),
    url(r'zf_test/$', interface.zf_test, name ='zf_test'),
    url(r'wucai_test/$', interface.wucai_test, name ='wucai_test'),
    url(r'zc_test/$', interface.zc_test, name ='zc_test'),
    url(r'get/$', interface.test_get, name ='test_get'),
    url(r'post/$', interface.test_post, name ='test_post'),
    url(r'attr/(\d+)/$', interface.interface_attr, name ='interface_attr'),
]
