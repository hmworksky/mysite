# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:53
# @Author  : Huangmin
# @Site    : 客户端将掉落N排泡泡的结果通知服务器端-13
# @File    : test_land.py
# @Software: PyCharm

from automated_testing.test_case.public.bubble_tool import assertResult,parse_replay_data,addBubble
import json
class Land(assertResult,addBubble):
	def __init__(self):
		self.cmd = 'land'
		super().__init__()
	
		
	def test_case_land_01(self):
		'''
		正常通知,此处添加了3排，第一排是单数，假定面板中最上面一排是双数
		'''

		self.equal_result(self.cmd,userId = self.user_id,pannel = self.get_new_pannel,dropBubbles = self.add_many_bubble(3))
	
	
	def test_case_land_02(self):
		'''
		异常通知,此处添加了0行泡泡
		'''
		self.equal_result(self.cmd,is_equal=False,userId = self.user_id,pannel = self.get_new_pannel,dropBubbles = self.add_many_bubble(0))
	
	def test_case_land_03(self):
		'''
		添加的泡泡中有异常数据，一行全是爆炸泡泡（单数行）
		'''
		self.equal_result(self.cmd,is_equal=False,userId = self.user_id,pannel = self.get_new_pannel,dropBubbles = self.add_one_bubble(type=2))
		
	def test_case_land_04(self):
		'''
		添加的泡泡中有异常数据，错误的泡泡颜色
		'''
		self.equal_result(self.cmd, is_equal=False, userId=self.user_id, pannel=self.get_new_pannel, dropBubbles=self.add_one_bubble(color='hhh'))
		
	def test_case_land_05(self):
		'''
		错误的userid
		'''
		self.equal_result(self.cmd, is_equal=False, userId=self.config.other_userid, pannel=self.get_new_pannel, dropBubbles=self.add_one_bubble())
	
	def test_case_land_06(self):
		'''
		空的userid
		'''
		self.equal_result(self.cmd, is_equal=False, pannel=self.get_new_pannel, dropBubbles=self.add_one_bubble())
	
	def test_case_land_07(self):
		'''
		空的params
		'''
		self.equal_result(self.cmd, is_equal=False)
	
	def test_case_land_08(self):
		'''
		并发请求
		'''
		pass
	
	def test_case_land_09(self):
		'''
		发送多次请求
		'''
		self.equal_result(self.cmd, userId=self.user_id, pannel=self.get_new_pannel, dropBubbles=self.add_many_bubble(3))
		#第二次判断为失败
		self.equal_result(self.cmd,is_equal=False, userId=self.user_id, pannel=self.get_new_pannel, dropBubbles=self.add_many_bubble(3))
	
	def test_case_land_10(self):
		'''
		正常通知,此处添加了3排，第一排是双数，假定面板中最上面一排是双数
		'''
		
		self.equal_result(self.cmd, userId=self.user_id, pannel=self.get_new_pannel, dropBubbles=self.add_many_bubble(3,is_singular=False))



