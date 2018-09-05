# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 13:58
# @Author  : Huangmin
# @Site    : 
# @File    : myThread.py
# @Software: PyCharm
import threading,os,time,random
from public_tool.myDecorator import exec_time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
class MyThread(object):
	def __init__(self):
		self.t_pool =  ThreadPoolExecutor()
		self.p_pool = ProcessPoolExecutor()
		self.pool_list = []
	def exec_process(self,func,*args,**kwargs):
		obj = self.p_pool.submit(func,*args,**kwargs).result()
		return 	obj
	
	def exec_thread(self,func,*args,**kwargs):
		obj = self.t_pool.submit(func,*args,**kwargs).result()
		return 	obj
	def for_func(self,func,*args,**kwargs):
		for _ in range(5):
			func(*args,**kwargs)
		return
	
@exec_time
def hhh():
	print('pid is :',os.getpid())
	return 1


def test_thread():
	s = threading.Thread(target=hhh)
	s.start()
if __name__ == '__main__':
	test_thread()




