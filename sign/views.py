# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,render_to_response
from .forms import RegisterForm


# Create your views here.

def register(request):
    if request.Method == 'POST' :
	form = RegisterForm(request.POST)
	if form.is_valid():
	    form.save()
	    return redirect('/')
    else :
	form = RegisterForm()
    return render_to_response('login/signup.html',context={'form':form})
