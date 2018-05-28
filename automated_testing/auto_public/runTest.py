# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 11:42
# @Author  : Huangmin
# @Site    : 
# @File    : runTest.py
# @Software: PyCharm
from automated_testing.models import  CaseInfo
class RunTest(object):
	def __init__(self, class_data=None):
		self.data = class_data
		self.sys_dir = 'D:\\Users\\huangmin\\git\\automated_testing\\test_case\\'
	
	def get_case_info(self, id):
		info = CaseInfo.objects.get(id=id)
		return info.class_name, info.case_name, info.case_memo
	
	def find_exec_file(self, id):
		class_name, _, _ = self.get_case_info(id)
		file_path = 'test_{}'.format(class_name.split('_')[0].lower())
		file_name = 'test_{}'.format(class_name.split('_')[1])
		return file_path, file_name, class_name
	
	def exec_test(self, id):
		import sys, traceback
		u'''
		执行单个测试
		:return:
		'''
		file_path, file_name, class_name = self.find_exec_file(id)
		path = self.sys_dir + file_path
		sys.path.append(path)
		mod = __import__(file_name)
		class_func = getattr(mod, class_name)
		_, case_name, case_memo = self.get_case_info(id)
		if self.data:
			# 实例化类
			f = class_func(self.data)
		else:
			f = class_func()
		try:
			# 执行函数
			getattr(f, case_name)()
			# 未抛出异常则添加至成功信息
			result = {'name': '{}:{}'.format(class_name, case_name), 'status': 'success'}
		except AssertionError as e:
			# 获取异常信息并添加到失败列表
			result = {'name': '{}:{}'.format(class_name, case_name), 'case_memo': case_memo, 'fail_info': traceback.format_exc(), 'status': 'fail'}
		return result
	
	@property
	def run(self):
		from public_tool.tools import get_pool
		t_key = 'auto_cron_list'
		pool = get_pool()
		if pool.llen(t_key) == 0:
			return
		queue_detail = eval(pool.lpop(t_key).decode())
		run_test_list = queue_detail.get('cron_list')
		queue_id = queue_detail.get('queue_id')
		success_list = []
		fail_list = []
		for i in run_test_list:
			# 获取执行结果
			result = self.exec_test(i)
			# 判断执行结果是成功还是失败
			if result['status'] == 'success':
				success_list.append(result.get('name'))
			elif result['status'] == 'fail':
				fail_list.append(result)
		# 组装返回数据
		result = {'queue_id': queue_id, 'success': success_list, 'fail': fail_list}
		pool.hmset('queue:result:{}'.format(queue_id), result)
		return result