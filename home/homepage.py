# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response,redirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from public_tool import tools
from urllib import unquote
from collections import defaultdict
import json




def index(request):
    username = request.session['username']
    branch = tools.branch_data(5,1)
    name_value = str(branch[0]).replace("'",'"')
    size_value = map(int,branch[1])
    return render_to_response('index.html', locals())


def get_create(request):
    username = request.session['username']
    return render_to_response('http_tool/get_create.html',{'username':username})
def ajax_dict():
    name_dict = {'测试':[1,50,35,20,55]}
    return JsonResponse(name_dict)
def ajax_dict1(request):
    name_dict = {'衬衫': '5', '羊毛衫': '2', '雪纺衫': '36', '裤子': '10', '高跟鞋': '10', '袜子': '20'}
    return JsonResponse(name_dict)