# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response,redirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from public_tool import tools
from urllib import unquote
from collections import defaultdict
import json
from html.parser import HTMLParser




def index(request):
    # username = request.session['username']
    branch = tools.branch_data(5)
    name_value = str(branch[0]).replace("'",'"')
    # name_value = branch.values()
    # size_value = map(int,branch.keys())
    return HttpResponse(isinstance(name_value,list))
    # parser = HTMLParser()
    # name_value= map(parser.unescape(),name_value)
    # return render_to_response('index.html', locals())


def get_create(request):
    username = request.session['username']
    return render_to_response('http_tool/get_create.html',{'username':username})
def ajax_dict():
    name_dict = {'测试':[1,50,35,20,56]}
    return JsonResponse(name_dict)
def ajax_dict1(request):
    name_dict = {'衬衫': '5', '羊毛衫': '2', '雪纺衫': '36', '裤子': '10', '高跟鞋': '10', '袜子': '20'}
    return JsonResponse(name_dict)