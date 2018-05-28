# -*- coding:utf-8 -*-

from django.shortcuts import  render_to_response,HttpResponseRedirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect
from public_tool import user
from .models import HttpSend
def post_list(request):
    username = request.session['username']
    user_id = user.getuserid(username)
    if user_id:
        post_list = list(HttpSend.objects.filter(user_id=user_id, send_type="POST").values("send_url", "thread_num", "headers", "cookie", "status","data" ,"id"))
        return render_to_response('http_tool/post_list.html', {'post_list': post_list, 'username': username})


def post_create(request):
    username = request.session['username']
    user_id = user.getuserid(username)
    if request.method == 'POST':
        post_url = request.POST.get('post_url')
        post_cookie = request.POST.get('post_cookie')
        post_head = request.POST.get('post_head')
        post_thread = request.POST.get('post_thread')
        post_data = request.POST.get('post_data')
        if len(post_thread) == 0:
            post_thread = 0
        try:
            # 从表单获取数据插入HttpSend表
            HttpSend.objects.create(send_url=post_url, headers=post_head, cookie=post_cookie, send_type='POST', thread_num=post_thread, data = post_data, user_id=user_id)
            return HttpResponseRedirect('/http/post/list/')  # 插入成功跳转列表页
        except Exception as e:
            # 此处需要添加日志
            # 插入失败，刷新页面
            return HttpResponse(e)
    return render_to_response('http_tool/post_create.html', {'username': username})


def post_detail(request,id):
    username = request.session['username']
    return render_to_response('http_tool/post_create.html', {'username': username})

def post_edit(request,id):
    return render_to_response('http_tool/get_list.html', {'username': id})
def post_delete(request,id):
    HttpSend.objects.filter(id=id).delete()
    return post_list(request)