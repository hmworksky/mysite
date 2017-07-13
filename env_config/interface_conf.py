# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response



def conf_create(request):
    return render_to_response('env_config/interface_conf.html')