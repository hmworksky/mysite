# -*- coding:utf-8 -*-

from django.conf.urls import url,include
from env_config import interface_conf,env_branch,property_conf
urlpatterns = [
    url(r'^interface_conf/',interface_conf.conf_create,name='conf_create'),
    url(r'^branch/',env_branch.branch_list,name='branch_list'),
    url(r'^property/create/',property_conf.property_create,name='property_create'),
    url(r'^property/edit/(\d+)/',property_conf.property_edit,name='property_edit'),
    url(r'^property/list/',property_conf.property_list,name='property_list'),
    url(r'^property/delete/(\d+)/',property_conf.property_delete,name='property_delete'),
    url(r'^property/update/',property_conf.property_update,name='property_update'),
  ]

