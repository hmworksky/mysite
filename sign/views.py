# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from .forms import RegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST' :
	form = RegisterForm(request.POST)
	if form.is_valid():
	    form.save()
	    return redirect('/login/index/')
    else :
	form = RegisterForm()
    return render_to_response('signup.html',context={'form':form})
def index(request):
   return HttpResponse("welcome")
