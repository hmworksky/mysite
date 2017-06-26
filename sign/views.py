# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from .forms import RegisterForm
from tools import *
import os
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
	        request.session['user']=username
	        return redirect('/tool/index/')
	    else :
	        return render_to_response('signup.html',{'errormsg':'用户名已注册'})
	else :
	    return render_to_response('signup.html',{'errormsg':'请输入相同密码'})
    return render_to_response('signup.html')
def login(request):
	
def index(request):
   return HttpResponse("welcome")
