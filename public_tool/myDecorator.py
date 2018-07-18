# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 11:25
# @Author  : Huangmin
# @Site    : 
# @File    : myDecorator.py
# @Software: PyCharm

import time,traceback,inspect
from public_tool.myLog import Log



def logs(filename,name,msg):
	def wrapper(func):
		def _wrapper(*args, **kwargs):
			logger = Log(filename=filename,name=name)
			logger.info(msg)
			return func(*args, **kwargs)
		return _wrapper
	return wrapper

def exec_time(func):
	'''
	计算函数执行时间
	:param func: 函数名
	:return:
	'''
	def wraper(*args,**kwargs):
		log = Log(name='print_func_exec_time',filename='func_exec')
		start_time = time.time()
		try:
			func(*args,**kwargs)
			end_time = time.time()
			log.info('{}函数消耗了{}秒'.format(func.__name__,end_time-start_time))
		except:
			log.error(traceback.format_exc())
	return wraper

	



def record_func_information(func):
	log = Log(name='print_func_information', filename='func_information')
	def _wrapper(*args,**kwargs):
		model = inspect.getmodule(func)
		source = inspect.getsource(func)
		log.info('{}函数的moudle信息是:{}'.format(func.__name__,str(model).encode('utf-8')))
		#print(model)
		print(func.__dict__)
		return func(*args,**kwargs)
	return _wrapper





@logs("record_func_caller", 'record_func_caller', 'record')
def record_func_caller(func):
	def _wrapper(*args,**kwargs):
		caller_name = traceback.extract_stack()
		sourcelines = inspect.getsourcelines(func)
		members = inspect.getmembers(func)
		file = inspect.getfile(func)
		print(file)
		# print(sourcelines)
		# print(caller_name)
		return func(*args,**kwargs)
	return _wrapper

