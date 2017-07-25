# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response,redirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect,JsonResponse





def index(request):
    username = request.session['username']
    return render_to_response('index.html', {'username': username})


def get_create(request):
    username = request.session['username']
    return render_to_response('http_tool/get_create.html',{'username':username})
def ajax_dict():
    name_dict = {'衬衫': '5', '羊毛衫': '2', '雪纺衫': '36', '裤子': '10', '高跟鞋': '10', '袜子': '20'}
    return JsonResponse(name_dict)
def ajax_dict1():
    name_dict = {'衬衫': '5', '羊毛衫': '2', '雪纺衫': '36', '裤子': '10', '高跟鞋': '10', '袜子': '20'}
    return JsonResponse(name_dict)