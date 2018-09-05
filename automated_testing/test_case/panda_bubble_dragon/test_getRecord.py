# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:33
# @Author  : Huangmin
# @Site    : 获取对战信息(6)
# @File    : test_getRecord.py
# @Software: PyCharm

from automated_testing.auto_public.auto_tools import Uts
from .test_getBubbles import getBubbles
from automated_testing.test_case.public.bubble_tool import buildRequest
class getRecord(getBubbles,Uts):
	def __init__(self):
		self.cmd = 'getRecord'
		self.userid = 2038969797
		super().__init__()
		
	def test_case_get_record_01(self):
		'''
		正常获取自己的对战信息
		:return:
		'''
		my_request = buildRequest.build(self.cmd,super().build_userid(self.userid))
		dev_result = self.sock.result(my_request)
		self.assertEqual(dev_result['res']['code'],200)