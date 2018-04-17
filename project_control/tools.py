# coding:utf-8
from functools import wraps
from models import ProjectInfo
from public_tool.tools import strf_time

def update_project(func):
	@wraps
	def kwraps(request,*args,**kwargs):
		ProjectInfo.objects.filter(online_time__gt = strf_time('time')).update(current_phase = 3 )
		return func(request,*args,**kwargs)
	return kwraps

def time_conctrol(str):
	str = str+":00"
	str = str.replace('/','-')
	return str
