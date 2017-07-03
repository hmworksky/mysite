# -*- coding:utf-8 -*-

from django.shortcuts import  render_to_response,redirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect
def post_list(request):
    username = request.session['username']
    return render_to_response('http_tool/post_list.html', {'username': username})


def post_create(request):
    username = request.session['username']
    return render_to_response('http_tool/post_create.html', {'username': username})