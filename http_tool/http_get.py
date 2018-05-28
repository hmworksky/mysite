# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response,HttpResponseRedirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect
from http_tool.models import HttpSend
from public_tool import user



def get_create(request):
    username = request.session['username']
    user_id = user.getuserid(username)
    if request.method == 'POST' :
        get_url = request.POST.get('get_url')
        get_cookie = request.POST.get('get_cookie')
        get_head = request.POST.get('get_head')
        get_thread = request.POST.get('get_thread')
        if len(get_thread) == 0:
            get_thread = 0
        try:
            #从表单获取数据插入HttpSend表
            HttpSend.objects.create(send_url = get_url , headers = get_head ,cookie = get_cookie, send_type = 'GET',thread_num =get_thread ,user_id = user_id )
            return HttpResponseRedirect('/http/get/list/')#插入成功跳转列表页
        except Exception as e :
            #此处需要添加日志
            #插入失败，刷新页面
            return HttpResponse(e)
    return render_to_response('http_tool/get_create.html',{'username':username})


def get_list(request):
    username = request.session['username']
    user_id = user.getuserid(username)
    if user_id :
        get_list = list(HttpSend.objects.filter(user_id = user_id,send_type = "GET").values("send_url","thread_num","headers","cookie","status","id"))
        return render_to_response('http_tool/get_list.html',{'get_list':get_list,'username':username})


def get_edit(request,id):
    return render_to_response('http_tool/get_list.html', {'username': id})

def get_detail(request,id):
    return render_to_response('http_tool/get_list.html',{'username':id})

def get_delete(request,id):
    HttpSend.objects.filter(id=id).delete()
    return get_list(request)

