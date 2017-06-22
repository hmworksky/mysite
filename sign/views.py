# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from .forms import RegisterForm
from tools import *


# Create your views here.

def register(request):
    if request.method == 'POST' :
	username  = request.POST.get('username')
	password = request.POST.get('password')
	if signup_judge(username):
	    signup(username,password)
	    request.session['user']=username
	    return HttpResponse("signup")
#	    return redirect('/login/index/')
	else :
	    return render_to_response('signup.html',{'errormsg':'用户名已注册'})
def index(request):
   return HttpResponse("welcome")
