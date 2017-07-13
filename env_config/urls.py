# -*- coding:utf-8 -*-

from django.conf.urls import url,include
from env_config import interface_conf
urlpatterns = [
    url(r'^interface_conf/',interface_conf.conf_create,name='conf_create'),
  ]

