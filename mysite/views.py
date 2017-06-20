#coding:utf-8
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.http.response import JsonResponse
from  django.shortcuts import render_to_response
import json

def hello(request):
    #return HttpResponse('hello\n')
    if request.method == 'GET' or request.method == 'POST':
	sid =dict(request.POST.iterlists())
#	sid = eval(sid.keys()[0].encode())
	s = sid.get('uid')
	t = isinstance(sid,dict)
        d = {"errorCode":"0000","errMsg":"test","yqbCode":"3002","balance":"300","uid":"ttt"}
	if t :
	    return HttpResponse(s)
	else :
	    return HttpResponse("2")
def hh(request):
    return HttpResponse("this is test page")
