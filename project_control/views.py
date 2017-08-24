# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response,HttpResponseRedirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect
from public_tool import user,tools
from http_tool.models import HttpSend
from .models import ProjectInfo

def project_create(request):
    username = request.session['username']
    user_id = user.getuserid(username)
    if request.method == 'POST' :
        project_name = request.POST.get('project_name')
        start_time = tools.time_conctrol(request.POST.get('start_time'))
        smock_time = tools.time_conctrol(request.POST.get('smock_time'))
        online_time = tools.time_conctrol(request.POST.get('online_time'))
        participant = request.POST.get('participant')
        project_manager = request.POST.get('project_manager')
        try:
            #从表单获取数据插入ProjectInfo表
            ProjectInfo.objects.create(project_name = project_name , start_time = start_time ,smock_time = smock_time, online_time = online_time,participant =participant ,user_id = user_id,project_manager=project_manager )
            return HttpResponseRedirect('/project/list/')#插入成功跳转列表页
        except Exception , e :
            #此处需要添加日志
            #插入失败，刷新页面
            return HttpResponse(e)
    return render_to_response('project_control/project_process_create.html',{'username':username})


def project_list(request):
    username = request.session['username']
    user_id = user.getuserid(username)
    if user_id :
        project_list = list(ProjectInfo.objects.filter(user_id = user_id).values("project_name","start_time","smock_time","online_time","participant","project_manager","current_phase"))
        return render_to_response('project_control/project_process_list.html',{'project_list':project_list,'username':username})


def get_edit(request,id):
    return render_to_response('http_tool/get_list.html', {'username': id})

def get_detail(request,id):
    return render_to_response('http_tool/get_list.html',{'username':id})

def get_delete(request,id):
    HttpSend.objects.filter(id=id).delete()
    return project_create(request)


