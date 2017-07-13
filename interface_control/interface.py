# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect,
from django.shortcuts import render,redirect,render_to_response
from django.http.response import JsonResponse
from public_tool.user import getuserid
import os
from interface_control.models import *
import json
import time
os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})




def interface_create(request):
    username = request.session.get('username')
    user_id = getuserid(username)
    if request.method == 'POST' : 
        interface_name = request.POST.get('url_name')
        return_value = request.POST.get('return_value')
        timeout = request.POST.get('timeout')
        if timeout == None :
            timeout = 0
        host = request.get_host()
        url_info = "http://"+ host  + "/interface/return/" + username + "/" + interface_name
        try :
            InterfaceInfo.objects.create(url_info = url_info ,status = 1 ,return_value = return_value ,user_id = user_id,timeout=timeout)
            return redirect('/interface/list/')
        except  Exception , e:
            #此处需要记录日志
            render_to_response('interface/interface_create.html', {'username': username})
    return render_to_response('interface/interface_create.html',{'username':username})	

def interface_list(request):
    username = request.session['username']
    user_id = getuserid(username)
    if user_id : 
        http_list = list(InterfaceInfo.objects.filter(user_id = user_id).values("url_info","timeout","return_value","status","id"))
        return render_to_response('interface/interface_list.html',{'http_list':http_list,'username':username})

def interface_return(request):
    if request.method == 'POST' or request.method == 'GET':
        host = request.get_host()
        path = request.path
        url = "http://" + host + path
    if InterfaceInfo.objects.filter(url_info = url):
        data = InterfaceInfo.objects.values("return_value").get(url_info=url)["return_value"]
        timeout = InterfaceInfo.objects.values("timeout").get(url_info=url)["timeout"]
        time.sleep(timeout)
        if data.startswith("{"):
            data = eval(data)
            return JsonResponse(data) 
        else :
            return HttpResponse(data)
    return HttpResponse('result')

# def interface_start(request,id):
#     return HttpResponse('start')

def interface_detail(request,id):
    return HttpResponse('detail')

def interface_edit(request,id):
    return HttpResponse('edit')

def interface_delete(request,id):
    http_list = InterfaceInfo.objects.filter( id = id ).delete()
    return interface_list(request)

def index(request):	
    return HttpResponse("welcome {uname}".format(uname=http_list))
