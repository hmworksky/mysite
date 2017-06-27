# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from tools import *
import os
from models import *
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

def interface_return(request):
    if request.method == 'POST' : 
        url_info = request.POST.get('url_info')
        commit_type = request.POST.get('commit_type')
        return_value = request.POST.get('return_value')
	username = request.session.get('username')
	

def index(request):
    username = request.session.get('username')
    p = Login.objects.get(username = 'test22')
    return HttpResponse("welcome {uname}".format(uname=p))
