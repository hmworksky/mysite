# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 11:44
# @Author  : Huangmin
# @Site    : 
# @File    : translation.py
# @Software: PyCharm

from django.shortcuts import  render_to_response
from public_tool.youdao import Youdao
from django.http import HttpResponse,JsonResponse
import json





def viewTranslation(request):
	username = request.session['username']
	return render_to_response('http_tool/translation.html',locals())

def getTranslationResult(request):
	if request.method == 'POST':
		msg = request.POST.get('msg')
		result = Youdao(msg).get_result()
		return HttpResponse(result)
	else:
		error = {'message':'method error,peease use POST','code':1001}
		error = json.dumps(error)
		return JsonResponse(error,safe=False)
		
		