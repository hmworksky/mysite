# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 11:25
# @Author  : Huangmin
# @Site    : 
# @File    : myDecorator.py
# @Software: PyCharm

import time,traceback,inspect
from public_tool.myLog import Log
from functools import wraps
from concurrent.futures import ThreadPoolExecutor


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
		for i in caller_name:
			print(type(i))
			print(i)
		# print(type(caller_name))
		return func(*args,**kwargs)
	return _wrapper

def multi_threading(number):
	'''
	多线程装饰器
	:param number:
	:return:
	'''
	def wrapper(func):
		def inner(*args,**kwargs):
			func(*args,**kwargs)
		return inner
	return wrapper
def key_exists(func):
	'''
	判断key是否存在，不存在返回一个空字典
	'''
	def inner(*args,**kwargs):
		try:
			func(*args,**kwargs)
		except KeyError:
			return {}
	return inner

def multi_process(number = 2):
	'''
	多进程装饰器
	:param number:
	:return:
	'''
	p = ThreadPoolExecutor()
	l = []
	def wrapper(func):
		def inner(*args,**kwargs):
			for _ in range(number):
				obj = p.submit(func,*args,**kwargs)
				l.append(obj)
				p.shutdown()
				result = [x.result() for x in l]
				return result
		return inner
	return wrapper

def record_exception(func):
	@wraps
	def inner(*args,**kwargs):
		try:
			func(*args,**kwargs)
		except:
			log = Log
@multi_process(3)
def test(*args,**kwargs):
	if args != None:
		return  args[0]
	elif kwargs != None:
		return kwargs
if __name__ == '__main__':
	print(test(2,3))