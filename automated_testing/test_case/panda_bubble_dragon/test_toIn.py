# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:30
# @Author  : Huangmin
# @Site    : 加入房间-3
# @File    : test_toIn.py
# @Software: PyCharm
import sys, os, time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from automated_testing.test_case.public.bubble_tool import assertResult



class toIn(assertResult):
	def __init__(self):
		self.cmd = 'toIn'
		super().__init__()
	def test_case_toIn_01(self):
		'''
		正常加入房间
		:return:
		'''
		self.equal_result(self.cmd,roomId=2)
	def test_case_toIn_02(self):
		'''
		加入多个房间
		:return:
		'''
		self.equal_result(self.cmd, roomId=2)
		self.equal_result(self.cmd, is_equal=False,roomId=3)
		
	def test_case_toIn_03(self):
		'''
		加入不存在的房间号
		:return:
		'''
		self.equal_result(self.cmd,is_equal=False, roomId='xxx')
	def test_case_toIn_04(self):
		'''
		重复加入房间
		:return:
		'''
		self.equal_result(self.cmd, roomId=2)
		self.equal_result(self.cmd, is_equal=False,roomId=2)
		
	def test_case_toIn_05(self):
		'''
		余额不足加入房间
		:return:
		'''
		self.equal_result(self.cmd,is_equal=False, roomId=2)
		
	def test_case_toIn_06(self):
		'''
		加入已开始的房间
		:return:
		'''
		self.equal_result(self.cmd,is_equal=False, roomId=2)
	def test_case_toIn_07(self):
		'''
		缺少roomid参数
		:return:
		'''
		self.equal_result(self.cmd,is_equal=False)
	def test_case_toIn_08(self):
		'''
		并发请求加入房间
		:return:
		'''
		self.equal_result(self.cmd,is_equal=False)
if __name__ == '__main__':
	def test(a):
		return a+1
	#t = toIn()
	print(test.__dict__)
	

