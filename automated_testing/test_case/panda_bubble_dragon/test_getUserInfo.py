# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:29
# @Author  : Huangmin
# @Site    : 获取用户信息-1
# @File    : test_getUserInfo.py
# @Software: PyCharm

from automated_testing.test_case.public.bubble_tool import assertResult
from automated_testing.config import  config


class getUserInfo(assertResult):
	def __init__(self):
		self.cmd = 'getUserInfo'
		super().__init__()
	
	def test_case_get_userinfo_01(self):
		'''
		正常获取用户信息
		:return:
		'''
		self.equal_result(self.cmd,userId = self.user_id)
		
	def test_case_get_userinfo_02(self):
		'''
		缺少参数
		:return:
		'''
		self.equal_result(self.cmd,is_equal=False)
	def test_case_get_userinfo_03(self):
		'''
		获取他人信息
		:return:
		'''
		self.equal_result(self.cmd,is_equal=False,userId = config.other_userid)




if __name__ == '__main__':
	result = s = [2,3,4]
	print(result)
	print(s)
	
	
	