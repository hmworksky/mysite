# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:54
# @Author  : Huangmin
# @Site    : 服务器通知客户端需要新加N个泡泡-16
# @File    : test_needAddBubbles.py
# @Software: PyCharm
from ..public.bubble_tool import Bubble,addBubble,assertResult
class NeedAddBubbles(Bubble,assertResult,addBubble):
	def __init__(self):
		self.cmd = 'needAddBubbles'
		Bubble.__init__(self,'self')
	
	def test_case_land_01(self):
		'''
		正常请求增加
		'''
		self.equal_result(self.cmd,userId=123,noticeId="111111")
		
