# -*- coding:utf-8 -*-
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from django.http.response import JsonResponse
import os
from models import *
os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})


def register(request):
    if request.method == 'POST' :
        username  = request.POST.get('username')
        password = request.POST.get('password')
        pwdagain = request.POST.get('pwdagain')
        if password == pwdagain :
            if Login.objects.filter(username = username) :
                return render_to_response('signup.html', {'errormsg': '用户名已注册'})
            else :
                try:
                    Login.objects.get_or_create(username=username,password=password)
                    request.session['username']=username
                    return redirect('/index/')
                except Exception ,e :
                    #此处需要添加日志
                    return   render_to_response('login/signup.html')
        else :
            return render_to_response('login/signup.html',{'errormsg':'请输入相同密码'})
    return render_to_response('signup.html')

def login(request):
    if request.method == 'POST' :
        username  = request.POST.get('username')
        password = request.POST.get('password')
        if Login.objects.filter(username = username,password=password):
            request.session['username'] = username
            return redirect('/interface/create/')
        else :
            return render_to_response('login/login.html',{'errormsg':'用户名密码错误'})
    return render_to_response('login/login.html')

def resetlogin(request):
    if request.method == 'POST' :
        username  = request.POST.get('username')
        password = request.POST.get('password')
        pwdagain = request.POST.get('pwdagain')
        if password == pwdagain :
            if Login.objects.filter(username = username) :#判断用户名是否存在
                try :
                    Login.objects.filter(username = username ).update(password = password)
                    request.session['username']=username
                    return redirect('/index/')
                except Exception ,e :
                    #此处需要添加日志
                    return render_to_response('login/reset.html')
            else :
                return render_to_response('login/reset.html',{'errormsg':'用户名不存在'})
        else :
            return render_to_response('login/reset.html',{'errormsg':'请输入相同密码'})
    return render_to_response('login/reset.html')
def index(request):
    return HttpResponse("welcome")