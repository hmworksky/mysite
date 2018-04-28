# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response,redirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from public_tool import tools
from urllib import unquote
from collections import defaultdict
import json
#from html.parser import HTMLParser




def index(request):
    from public_tool.tools import Memcached,logger
    mem = Memcached()
    #获取大小最大的5个应用
    logger('mem',mem.getmem('branch_sort'))
    branch_data = eval(mem.getmem('branch_sort'))[:5]
    logger('branchtype',type(branch_data))
    name_value = str([x.get('app') for x in branch_data])
    size_value = [x.get('size') for x in branch_data]
    return render_to_response('index.html', locals())


def get_create(request):
    username = request.session['username']
    return render_to_response('http_tool/get_create.html',{'username':username})
def ajax_dict():
    name_dict = {'测试':[1,50,35,20,57]}
    return JsonResponse(name_dict)
def ajax_dict1(request):
    from env_config.env_tools import get_branch
    branch_data = get_branch(sort = True)[:5]
    name_value = str([x.get('app') for x in branch_data])
    size_value = str([x.get('size') for x in branch_data])
    return render_to_response('index.html',locals())

