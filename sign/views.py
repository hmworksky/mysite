# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from django.http.response import JsonResponse
from tools import *
import os
from models import *
import json
os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})


# Create your views here.

def register(request):
    if request.method == 'POST' :
	username  = request.POST.get('username')
	password = request.POST.get('password')
	pwdagain = request.POST.get('pwdagain')
	if password == pwdagain :
  	    if signup_judge(username = username):
	        signup(username,password)
	        request.session['username']=username
	        return redirect('/tool/index/')
	    else :
	        return render_to_response('signup.html',{'errormsg':'用户名已注册'})
	else :
	    return render_to_response('signup.html',{'errormsg':'请输入相同密码'})
    return render_to_response('signup.html')

def login(request):
    if request.method == 'POST' :
        username  = request.POST.get('username')
        password = request.POST.get('password')
        if login_judge(username,password):
		request.session['username'] = username
                return redirect('/tool/index/')
        else :
            return render_to_response('login.html',{'errormsg':'用户名密码错误'})
    return render_to_response('login.html')

def resetlogin(request):
    if request.method == 'POST' :
        username  = request.POST.get('username')
        password = request.POST.get('password')
        pwdagain = request.POST.get('pwdagain')
        if password == pwdagain :
	    if signup_judge(username = username) is False:
                resetpwd(username,password)
                request.session['username']=username
                return redirect('/tool/index/')
	    else :
                return render_to_response('reset.html',{'errormsg':'用户名不存在'})
        else :
            return render_to_response('reset.html',{'errormsg':'请输入相同密码'})
    return render_to_response('reset.html')	
def interface_create(request):
    if request.method == 'POST' : 
        interface_name = request.POST.get('url_name')
        commit_type = request.POST.get('commit_type')
        return_value = request.POST.get('return_value')
        username = request.session.get('username')
        user_id = Login.objects.values("id").get(username = username)["id"]
	host = request.get_host()
	url_info = "http://"+ host  + "/tool/interface/return/" + username + "/" + interface_name
	try :
            InterfaceInfo.objects.create(url_info = url_info ,status = 1 ,return_value = return_value ,user_id = user_id)
	except  Exception , e:
	    return HttpResponse("接口已存在")
        return HttpResponse("生成接口地址为:{url},返回值为:{re}".format(url=url_info,re=return_value))
    return render_to_response('interface_create.html')	
def interface_return(request):
    if request.method == 'POST' or request.method == 'GET':
	host = request.get_host()
	path = request.path
	url = "http://" + host + path
        if InterfaceInfo.objects.filter(url_info = url):
	    data = InterfaceInfo.objects.values("return_value").get(url_info=url)["return_value"]
	    if data.startswith("{"):
		data = eval(data)
	        return JsonResponse(data) 
	    else :
		return HttpResponse(data)
    return HttpResponse('result')
def index(request):
    host = request.get_host()
    path = request.path
    username = request.session.get('username')
    url_info = "http://"+ host  + path + username + "/"  
    p = Login.objects.values("id").get(username = 'test22')["id"]
    return HttpResponse("welcome {uname}".format(uname=p))
