# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect,HttpResponseServerError
from django.shortcuts import render,redirect,render_to_response
from django.http.response import JsonResponse
from public_tool.user import getuserid
from public_tool.tools import zf_ticket_conctorl,wucai_ticket_conctorl
import os
from interface_control.models import *
import json
import time,logging,collections
os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})




def interface_create(request):
    username = request.session.get('username')
    user_id = getuserid(username)
    if request.method == 'POST' : 
        interface_name = request.POST.get('url_name')
        return_value = request.POST.get('return_value')
        timeout = request.POST.get('timeout')
        if timeout == None :
            timeout = 0
        host = request.get_host()
        url_info = "http://"+ host  + "/interface/return/" + username + "/" + interface_name
        try :
            InterfaceInfo.objects.create(url_info = url_info ,status = 1 ,return_value = return_value ,user_id = user_id,timeout=timeout)
            return HttpResponseRedirect('/interface/list/')
        except  Exception , e:
            #此处需要n记录日志
            render_to_response('interface/interface_create.html', {'username': username})
    return render_to_response('interface/interface_create.html',{'username':username})	

def interface_list(request):
    username = request.session['username']
    user_id = getuserid(username)
    if user_id : 
        http_list = list(InterfaceInfo.objects.filter(user_id = user_id).values("url_info","timeout","return_value","status","id"))
        return render_to_response('interface/interface_list.html',{'http_list':http_list,'username':username})

def interface_return(request):
    if request.method == 'POST' or request.method == 'GET':
        host = request.get_host()
        path = request.path
        url = "http://" + host + path
    if InterfaceInfo.objects.filter(url_info = url):
        data = InterfaceInfo.objects.values("return_value").get(url_info=url)["return_value"]
        timeout = InterfaceInfo.objects.values("timeout").get(url_info=url)["timeout"]
        time.sleep(timeout)
        if data.startswith("{"):
            data = eval(data)
            return JsonResponse(data) 
        else :
            return HttpResponse(data)
    return HttpResponse('result')

# def interface_start(request,id):
#     return HttpResponse('start')

def interface_detail(request,id):
    return HttpResponse('detail')

def interface_edit(request,id):
    return HttpResponse('edit')

def interface_delete(request,id):
    http_list = InterfaceInfo.objects.filter( id = id ).delete()
    return interface_list(request)


def index(request):
    li = ['0218562017071200000001']
    li1 = []
    return_str1 = ''' <?xml version="1.0" encoding="GBK"?><message version="2.0"id="0218562017071200000067"><header><messengerID>021856</messengerID><timestamp>20170712200104</timestamp><    transactionType>506</transactionType><digest>072e04839e04edd28dfc12e9fd9dd1e4</digest></header><body><responsecode="0000" message="鎴愬姛锛岀郴缁熷鐞嗘甯搞€�"><bonusQueryResult bonusNum    ber="01,02,03,04,05,06#07" totalItems="2"totalMoney="220"><issue number="2017075" gameName="ssq"/>'''
    str4 = '''</bonusQueryResult></response></body></message>'''
    for i in li:
        str2 = '''<bonusItem playType="103" money="200" levelBonusMoney="200"isBombBonus="false" bonusLevel="4" ticketID="{ticket}"size="1"/>'''.format(ticket=i)
        li1.append(str2)
    str3 = "".join(li1)
    str5 = return_str1+str3+str4
    return HttpResponse(str5)

def zfv2_touzhu(request):
    logger = logging.getLogger("django")
    #params = dict(request.POST)
    ticket_info = dict(request.POST)
    logger.info("ticket_info:{info}:".format(info=ticket_info))
    ticket_id = eval(ticket_info.keys()[0])["ticket_id"]
	#ticket_info = ticket_info.keys()
    logger.info("info:{info}".format(info=ticket_id))
    ticket_list = []
    if len(ticket_id) == 1:
        ticket_id = ticket_id[0]
        ticket_params = {"response":{"ticket":{"@attributes":{"ticketId":ticket_id,"status":"1000","msg":"test1"}},"code":"0000","msg":"test2"}}
        logger.info("return:{info}".format(info=ticket_params))
    else:
        for i in ticket_id:
            ticket_return = {}
            ticket_return = collections.OrderedDict()
            ticket_r = {}
            ticket_return["ticketId"] = i
            ticket_return["status"] = "1000"
            ticket_return["msg"] = "test"
            ticket_r["@attributes"] = ticket_return
            ticket_list.append(ticket_r)
    #ticket_params = collections.OrderedDict()
        ticket_params = {"response":{"ticket":ticket_list,"code":"0000","msg":"test2"}}
        logger.info("return:{info}".format(info=ticket_params))
    return JsonResponse(ticket_params)
def zf_test(request):
    logger = logging.getLogger("django")
    ticket_info = dict(request.POST)
    ticket_params = zf_ticket_conctorl(ticket_info,state = 1)
    logger.info("zf_test:{info}".format(info = ticket_params))
    return JsonResponse(ticket_params) 
def wucai_test(request):
    logger = logging.getLogger("django")
    ticket_info = dict(request.POST)
    ticket_params = wucai_ticket_conctorl(ticket_info,state = 0)
    logger.info("wucai_test:{info}".format(info = ticket_params))
    return JsonResponse(ticket_params)
