# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:55
# @Author  : Huangmin
# @Site    : 使用道具-20
# @File    : test_useItem.py
# @Software: PyCharm


import sys, os, time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from automated_testing.auto_public.auto_tools import Uts
from automated_testing.config import config
from automated_testing.test_case.panda_bubble_dragon.test_addBubbles import addBubbles
from ..public.bubble_tool import buildRequest


class useItem(addBubbles, Uts):
	def __init__(self):
		self.cmd = 'useItem'
		self.default_user = config.default_userid
		super().__init__()
	
	def build_skill_request(self, userid, itemId):
		default_data = {
			'userId': None,
			'itemId': None
		}
		
		if not userid:
			del default_data['userId']
		elif not itemId:
			del default_data['itemId']
		else:
			default_data['userId'] = userid
			default_data['itemId'] = itemId
		return default_data
	
	def build_result(self, userid=config.default_userid, itemId=1001, is_equal=True):
		my_request = buildRequest.build(self.cmd, self.build_skill_request(userid, itemId))
		dev_result = self.sock.result(my_request)
		if is_equal:
			self.assertEqual(dev_result['res']['code'], 200)
		else:
			self.assertNotEqual(dev_result['res']['code'], 200)
	
	def test_case_use_item_01(self):
		'''
		使用道具1001
		:return:
		'''
		self.build_result()
	
	def test_case_use_item_02(self):
		'''
		使用道具1002
		:return:
		'''
		self.build_result(itemId=1002)
	
	def test_case_use_item_03(self):
		'''
		使用道具1003
		:return:
		'''
		self.build_result(itemId=1003)
	
	def test_case_use_item_04(self):
		'''
		使用道具1004
		:return:
		'''
		self.build_result(itemId=1004)
	
	def test_case_use_item_05(self):
		'''
		userid为空
		:return:
		'''
		self.build_result(userid=False, is_equal=False)
	
	def test_case_use_item_06(self):
		'''
		itemId为空
		:return:
		'''
		self.build_result(itemId=False, is_equal=False)
	
	def test_case_use_item_07(self):
		'''
		给对方使用道具
		:return:
		'''
		self.build_result(userid=2038416866, is_equal=False)
	
	def test_case_use_item_08(self):
		'''
		并发使用道具
		:return:
		'''
		my_requst = self.build_skill_request(2038969797, 1001)
	
	def test_case_use_item_09(self):
		'''
		使用未携带的道具
		:return:
		'''
		self.build_result(itemId=1004, is_equal=False)  # 实际携带1001
	
	def test_case_use_item_10(self):
		'''
		使用未携带的道具
		:return:
		'''
		self.build_result(itemId=1004)  # 实际携带1001
	
	def test_case_use_item_11(self):
		
		'''
		道具在冷却中
		:return:
		'''
		my_requst = self.build_skill_request(2038969797, 1001)
		self.sock.send(my_requst)
		time.sleep(0.2)
		self.build_result(2038969797, 1001, False)


if __name__ == '__main__':
	s = useSkill()