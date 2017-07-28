# -*- coding:utf-8 -*-

from django.conf.urls import url,include
from env_config import interface_conf,env_branch
urlpatterns = [
    url(r'^interface_conf/',interface_conf.conf_create,name='conf_create'),
    url(r'^branch/',env_branch.get_branch,name='get_branch'),
  ]

