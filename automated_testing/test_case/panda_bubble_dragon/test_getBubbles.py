# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:34
# @Author  : Huangmin
# @Site    : 炮台产生新泡泡(7)
# @File    : test_getBubbles.py
# @Software: PyCharm
from automated_testing.auto_public.auto_tools import Uts
from .test_addBubbles import addBubbles
from automated_testing.test_case.public.bubble_tool import buildRequest
class getBubbles(addBubbles,Uts):
	def __init__(self):
		self.cmd = 'getBubbles'
		super().__init__()
	
	def build_userid(self,userId):
		data = {
			'userId': userId
		}
		return data
	
	def test_case_get_bubbles_01(self):
		'''
		不存在的userid
		:return:
		'''
		
		my_request = buildRequest.build(self.cmd,self.build_userid(0))
		dev_result = self.sock.result(my_request)
		self.assertNotEqual(dev_result['res']['code'],200)
	
	def test_case_get_bubbles_02(self):
		'''
		生成一个正常的泡泡
		:return:
		'''
		my_request = buildRequest.build(self.cmd,self.build_userid(2038969797))
		dev_result = self.sock.result(my_request)
		self.assertEqual(dev_result['res']['code'],200)
		
		
	def test_case_get_bubbles_03(self):
		'''
		连续发送2个命令(未使用泡泡时，无法生成新泡泡)
		:return:
		'''
		my_request = buildRequest.build(self.cmd, self.build_userid(2038969797))
		self.sock.send(my_request)
		dev_result2 = self.sock.result(my_request)
		self.assertNotEqual(dev_result2['res']['code'], 200)
		
	def test_case_get_bubbles_04(self):
		'''
		缺少参数
		:return:
		'''
		my_request = buildRequest.build(self.cmd)
		dev_result = self.sock.result(my_request)
		self.assertNotEqual(dev_result['res']['code'],200)

	def test_case_get_bubbles_05(self):
		'''
		并发发送消息
		:return:
		'''
	
	def test_case_get_bubbles_06(self):
		'''
		给别人炮台产生新泡泡
		:return:
		'''
		my_request = buildRequest.build(self.cmd, self.build_userid(2038416866))#2038416866为对方userid
		dev_result = self.sock.result(my_request)
		self.assertNotEqual(dev_result['res']['code'], 200)
		
			