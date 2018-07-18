# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect,HttpResponseServerError
from django.shortcuts import render,redirect,render_to_response
from django.http.response import JsonResponse
from public_tool.user import getuserid
from public_tool.tools import logger
from django.db.models import Q
import os,requests
from interface_control.models import *
import json,time
import time,logging,collections
import traceback
os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})



#中福票处理返回函数
def zf_ticket_conctorl(ticket_info,state = 0):#0投注成功，1投注失败
    ticket_id = eval(ticket_info.keys()[0])["ticket_id"]
    ticket_list = []
    ticket_status = {0:"1000",1:"0007"}
    if len(ticket_id) == 1:
        if state == 0 :
            status = ticket_status.get(0)
        else:
            status = ticket_status.get(1)
        ticket_id = ticket_id[0]
        ticket_params = {"response":{"ticket":{"@attributes":{"ticketId":ticket_id,"status":status,"msg":"test1"}},"code":"0000","msg":"test2"}}
    else:
        times = 0
        for i in ticket_id:
            ticket_return = {}
            ticket_r = {}
            ticket_return["ticketId"] = i
            ticket_return["msg"] = "test"
            if times ==0:
                status = ticket_status.get(0)
                times += 1
            else:
                status = ticket_status.get(1)
            ticket_return["status"] = status
            ticket_r["@attributes"] = ticket_return
            ticket_list.append(ticket_r)
        ticket_params = {"response":{"ticket":ticket_list,"code":"0000","msg":"test2"}}
    return ticket_params

#吾彩票处理返回函数
def wucai_ticket_conctorl(ticket_info,state = 0):#state:0=投注成功，1=投注失败
    if state == 0 :
        status = "0000"
    else:
        status = "1011"
    ticket_params = {"response":{"code":status,"message":"wucai_test"}}
    return ticket_params

#中创票处理返回函数
def zc_ticket_conctorl(ticket_info,state = 0):
    ticket_list = []
    orderid = eval(ticket_info.keys()[0])["ticket_id"]
    uuid = eval(ticket_info.keys()[0])["uuid"]
    status_code = {0:10000,1:10001}
    times = 0
    for i in orderid:
        ticket_r = {}
        code = status_code.get(0)
        if state == 1:
            code = status_code.get(1)
        elif state not in (0,1):
            if times == 0:
                code = status_code.get(1)
                times += 1
        ticket_r["orderId"] = i
        ticket_r["code"] = code
        ticket_r["message"] = "zc_test"
        ticket_list.append(ticket_r)
    ticket_params = {"err":{"code":10000,"des":"zctest"},"tickets":ticket_list,"uuid":uuid}
    return ticket_params

#创建接口返回
def interface_create(request):
    username = request.session.get('username')
    user_id = getuserid(username)
    if request.method == 'POST' : 
        interface_name = request.POST.get('interface_name')
        url_info = request.POST.get('url_info')
        return_value = str(request.POST.get('return_value'))
        request_type = request.POST.get('request_type')
        timeout = request.POST.get('timeout')
        if len(timeout)  == 0:
            timeout = 0
        try :
            InterfaceInfo.objects.create(interface_name = interface_name,url_info = url_info ,request_type = request_type ,return_value = return_value ,user_id = user_id,timeout=timeout)
            return HttpResponseRedirect('/interface/list/')
        except  Exception as e:
            #此处需要n记录日志
            logger('insert',e)
            render_to_response('interface/interface_create.html', {'username': username})
    return render_to_response('interface/interface_create.html',{'username':username})


#接口列表展示
def interface_list(request):
    from automated_testing.models import InterfaceAttr
    username = request.session['username']
    user_id = getuserid(username)
    if user_id : 
        http_list = list(InterfaceInfo.objects.filter(Q(user_id = user_id) | Q(request_type = 11)).values("interface_name","url_info","timeout","return_value","request_type","id","user_id"))
        interface_id = http_list[0]['id']
        hidden_flag = False
        attr = list(InterfaceAttr.objects.filter(interface_id = interface_id).values('id'))
        if len(attr) >0:
            hidden_flag =True
        return render_to_response('interface/interface_list.html',{'http_list':http_list,'username':username,'hidden_flag':hidden_flag})

#实际接口返回处理
def interface_return(request):
    if request.method == 'POST' or request.method == 'GET':
        host = request.get_host()
        path = request.path
        url = "http://{host}{path}".format(**locals())
        request_host = request.get_host()
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

def interface_return_new(request):
    default_java_host = '18test-app.stg3.1768.com:8080'
    path = request.path
    #获取请求地址中的用户名
    uname = path.split('/')[3]
    user_id = getuserid(uname)
    request_path = path.split('/')[4:][0]
    result = list(InterfaceInfo.objects.filter(user_id = user_id,url_info__contains =request_path).values('id','request_type','return_value','timeout','url_info'))
    if len(result)==0:
        request_type = 3
        timeout = 0
        java_url = "http://{default_java_host}{path}".format(**locals())
        return HttpResponse(java_url)
    else:
    #列表转化为字典
        result = result[0]
        request_type = result['request_type']
        return_data = result['return_value']
        timeout = result['timeout']
        java_url = result['url_info']
    if request.method =='POST':
        post_flag = True
        request_data = request.POST
    else:
        post_flag = False
        request_data = request.GET
    def request_java(flag,url,data=None):
        if flag:
            java_result = requests.post(url =url ,data = data).content
        else:
            if data:
                java_result = requests.get(url =url ,data = data).content
            else:
                java_result = requests.get(url).content
        return java_result

    #该接口来源过滤
    if request_type == 1:
        time.sleep(timeout)
        return HttpResponse('error')
    #返回指定结果
    elif request_type ==2:
        time.sleep(timeout)
        if return_data.startswith("{"):
            data = json.loads(return_data)
            return JsonResponse(data)
        else:
            return HttpResponse(return_data)

    #继续请求JAVA获取JAVA结果
    elif request_type ==3:
        java_result = request_java(post_flag,java_url,request_data)
        return HttpResponse(java_result)

    # 继续请求JAVA返回指定结果
    elif request_type ==4:
        request_java(post_flag, java_url, request_data)
        return HttpResponse(return_data)
    return HttpResponse('result')

def test_get(request):
    return HttpResponse('get')
def test_post(request):
    return HttpResponse('post')

def interface_attr(request,id):
    from automated_testing.models import InterfaceAttr
    username = request.session['username']
    field_name = request.POST.get('field_name')
    field_max = request.POST.get('field_max')
    field_min = request.POST.get('field_min')
    field_type = request.POST.get('field_type')
    field_null = request.POST.get('field_null')
    memo = request.POST.get('field_memo')
    logger('request',request.POST)
    try:
        InterfaceAttr.objects.create(field = field_name,max = field_max,min = field_min,type = field_type,is_null = field_null,interface_id = id,memo = memo)
        return HttpResponseRedirect('/interface/list/')
    except Exception as e:
        logger('InterfaceAttr insert fail',traceback.format_exc())
        return render_to_response('interface/interface_conf.html',locals())
    return render_to_response('interface/interface_conf.html',locals())

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

def zf_test(request):
    logger = logging.getLogger("django")
    ticket_info = dict(request.POST)
    ticket_params = zf_ticket_conctorl(ticket_info,state = 1)
    logger.info("zf_test:{info}".format(info = ticket_params))
    #time.sleep(80)
    return JsonResponse(ticket_params) 
    #return HttpResponse(None)
def wucai_test(request):
    logger = logging.getLogger("django")
    ticket_info = dict(request.POST)
    ticket_params = wucai_ticket_conctorl(ticket_info,state = 1)
    logger.info("wucai_test:{info}".format(info = ticket_params))
    return JsonResponse(ticket_params)
def zc_test(request):
    logger  = logging.getLogger("django")
    ticket_info = dict(request.POST)
    ticket_params = zc_ticket_conctorl(ticket_info,state = 0)
    logger.info("zc_test:{info}".format(info = ticket_info))
    return JsonResponse(ticket_params)
    #return HttpResponse(ticket_info)
