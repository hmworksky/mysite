# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response,redirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from public_tool import tools,encryption
from public_tool.tools import logger
from urllib import unquote
from collections import defaultdict
import json
#from html.parser import HTMLParser




def index(request):
    username = request.session['username']
    # branch = tools.branch_data(5)
    # name_value = str(branch[0]).replace("'",'"')
    # name_value = branch.values()
    # size_value = map(int,branch.keys())
    # return HttpResponse(isinstance(name_value,list))
    # parser = HTMLParser()
    # name_value= map(parser.unescape(),name_value)
    # return render_to_response('index.html', locals())
    #return render_to_response('http_tool/get_create.html', {'username':'中文'})
    size_value = [1,2,3,4,5,6]
    name_value = str(["branch", "test", "test2", "test3", "test4", "test5"]).decode(encoding='utf-8', errors='strict')
    return render_to_response('index.html', locals())


def get_create(request):
    username = request.session['username']
    return render_to_response('http_tool/get_create.html',{'username':username})
def ajax_dict():
    name_dict = {'测试':[1,50,35,20,57]}
    return JsonResponse(name_dict)
def ajax_dict1(request):
    import json
    name_dict = {u'test1': 333333, 'test-2': 2342342234, 'test3': 23434, 'test4': 22,'test5': 33, 'test6': 44}
    size_value = map(int, name_dict.values())

    #name_dict = json.dumps(name_dict,encoding='UTF-8',ensure_ascii=False)
    name_value = [i.decode('string_escape') for i in name_dict.keys()]
    logger("test1:{}".format(name_value))
    name_value = str(["branch","test","test2","test3","test4","test5"]).decode(encoding='utf-8',errors='strict')

    logger("name_value:{}".format(name_value))
    logger("size_value:{}".format(size_value))
    # return JsonResponse(name_dict)
    return render_to_response('index.html',locals())
    #return HttpResponse(name_value)
