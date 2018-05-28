# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 18:54
# @Author  : Huangmin
# @Site    : 
# @File    : case_info.py
# @Software: PyCharm
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import CaseInfo,GameInfo
from public_tool.tools import logger,get_pool
from automated_testing.auto_public.auto_tools import get_queue_id
from public_tool.user import getuserid



def case_info(request):
	username = request.session['username']
	user_id = getuserid(username)
	case_list =  list(CaseInfo.objects.all().values('id','case_memo','class_memo','game_id'))
	for i in case_list:
		game_id = i.get('game_id')
		game_name = GameInfo.objects.filter(id = game_id).values('memo')[0].get('memo')
		i['game_id'] = game_name
	return render_to_response('automated_testing/case_info.html',locals())

def case_queue(request):
	username = request.session['username']
	user_id = getuserid(username)
	#获取前端form的数据
	data = dict(request.POST)
	#分配一个新的queue_id
	#if not bool(queue_id):
	queue_id = get_queue_id(1)
	logger('case_queue', queue_id)
	#获取redis连接
	pool = get_pool()
	#组装入队列数据
	data = {'queue_id':queue_id,'cron_list':data.get('case_check')}
	#插入需要执行的任务list
	pool.lpush('auto_cron_list', data)
	#记录该用户的队列ID
	pool.lpush('user:queue:list:{}'.format(user_id),queue_id)
	#记录日志
	logger('data',data.get('case_check'))
	return case_info(request)

