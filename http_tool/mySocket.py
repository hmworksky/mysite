# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 15:25
# @Author  : Huangmin
# @Site    : 
# @File    : mySocket.py
# @Software: PyCharm


from django.shortcuts import render_to_response
from dwebsocket.decorators import accept_websocket,require_websocket
from django.http import HttpResponse
from django.views.generic.base import View
import socket

@accept_websocket
def echo(request):
	num =0
	if not request.is_websocket():
		try :
			message = request.GET['message']
			return HttpResponse(message)
		except:
			return render_to_response('http_tool/test_socket.html')
	else:
		for m in request.websocket:
			message_id = num
			request.websocket.send('recv data:{}\n sever_data:{}'.format(m,message_id).encode('utf-8'))
			num+=1
			
# class mySock(View):
#
# 	def conn(self,request):
		
