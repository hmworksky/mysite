# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response,redirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect





def index1(request):
    username = request.session['username']
    return render_to_response('http_tool/get_list.html', {'username': username})


def get_create(request):
    username = request.session['username']
    return render_to_response('http_tool/get_create.html',{'username':username})