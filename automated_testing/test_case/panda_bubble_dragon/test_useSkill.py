# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:55
# @Author  : Huangmin
# @Site    : 使用技能-19
# @File    : test_useSkill.py
# @Software: PyCharm
import sys,os,time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from automated_testing.auto_public.auto_tools import Uts
from automated_testing.config import config
from automated_testing.test_case.panda_bubble_dragon.test_addBubbles import addBubbles
from ..public.bubble_tool import buildRequest
class useSkill(addBubbles,Uts):
	def __init__(self):
		self.cmd = 'useSkill'
		self.default_user = config.default_userid
		super().__init__()
	
	def build_skill_request(self,userid,skillid):
		default_data = {
			'userId':None,
			'skillId':None
		}
		if not userid:
			del default_data['userId']
		elif not skillid:
			del default_data['skillId']
		else:
			default_data['userId'] = userid
			default_data['skillId'] = skillid
		return default_data
	def build_result(self,userid = config.default_userid,skillid = 1001,is_equal = True):
		my_request = buildRequest.build(self.cmd,self.build_skill_request(userid,skillid))
		dev_result = self.sock.result(my_request)
		if is_equal:
			self.assertEqual(dev_result['res']['code'],200)
		else:
			self.assertNotEqual(dev_result['res']['code'], 200)
		
	def test_case_use_skill_01(self):
		'''
		使用技能1001
		:return:
		'''
		self.build_result()
		
	def test_case_use_skill_02(self):
		'''
		使用技能1002
		:return:
		'''
		self.build_result(skillid=1002)
	def test_case_use_skill_03(self):
		'''
		使用技能1003
		:return:
		'''
		self.build_result(skillid=1003)
	def test_case_use_skill_04(self):
		'''
		使用技能1004
		:return:
		'''
		self.build_result(skillid=1004)
	def test_case_use_skill_05(self):
		'''
		userid为空
		:return:
		'''
		self.build_result(userid=False,skillid=1004,is_equal=False)
	
	def test_case_use_skill_06(self):
		'''
		skillid为空
		:return:
		'''
		self.build_result(skillid=False,is_equal=False)
		
	def test_case_use_skill_07(self):
		'''
		给对方使用技能
		:return:
		'''
		self.build_result(userid=2038416866,is_equal=False)
	
	def test_case_use_skill_08(self):
		'''
		并发使用技能
		:return:
		'''
		my_requst = self.build_skill_request(2038969797,1001)
		
	def test_case_use_skill_09(self):
		'''
		使用未携带的技能
		:return:
		'''
		self.build_result(skillid=1004,is_equal=False)#实际携带1001
		
	def test_case_use_skill_10(self):
		'''
		使用未携带的技能
		:return:
		'''
		self.build_result(skillid=1004)#实际携带1001
	def test_case_use_skill_11(self):
		
		'''
		技能在冷却中
		:return:
		'''
		my_requst = self.build_skill_request(2038969797, 1001)
		self.sock.send(my_requst)
		time.sleep(0.2)
		self.build_result(2038969797,1001,False)
	
	
if __name__ == '__main__':
	s = useSkill()