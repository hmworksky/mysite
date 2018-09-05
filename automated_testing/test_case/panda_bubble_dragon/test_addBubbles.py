# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:54
# @Author  : Huangmin
# @Site    : 客户端将新添加N个泡泡通知服务器(17)
# @File    : test_addBubbles.py
# @Software: PyCharm

from automated_testing.auto_public.auto_tools import Uts
from public_tool import mySocket
from automated_testing.config import config
from automated_testing.test_case.public.bubble_tool import addBubble,buildRequest

class addBubbles(Uts):
	'''
		命令：
		{
			'cmd':addBubbles,
			'params':[{
				'color':'red',
				'status':1,		//1:未销毁	0：已销毁
				'type':1		//泡泡的类型(1:普通泡泡、2：爆炸泡泡、3：闪电泡泡、4：精灵泡泡)
			},{},{}
			]
		}
	'''
	def __init__(self):
		self.sock = mySocket.gameSock(config.bubbles_dev_socket_url)
		self.res = None
		self.replay = None
		self.add = addBubble()
		
		# super(requestServer.__init__(server_host='server_url'))
		
	def test_case_01(self):
		'''
		测试一行多个爆炸泡泡
		'''
		
		res_data = {
				'cmd': 'addBubbles',
				'params': []
		}
		tmp = {'color': 'red', 'status': 1, 'type': 2}
		for _ in range(10):
			res_data['params'].append(tmp)
		dev_result = self.my_request(res_data)
		self.assertNotEqual(dev_result['res']['code'],200)
		
		
		
	def test_case_02(self):
		'''
		测试3行内含有多个爆炸泡泡
		'''
		my_bubbles = buildRequest.build('addBubbles',self.add.add_many_bubble(3,type=2))
		dev_result = self.sock.result(my_bubbles)
		self.assertNotEqual(dev_result['res']['code'],200)
		
		
		
	def test_case_03(self):
		'''
		测试增加超过11排泡泡
		'''
		my_bubbles = self.add.add_many_bubble(12)
		dev_result = self.sock.result(my_bubbles)
		self.assertNotEqual(dev_result['res']['code'],200)
		
	
	def test_case_04(self):
		'''
		游戏已结束，发送命令
		'''
	def test_case_05(self):
		'''
		正常添加一排泡泡
		'''
		my_bubbles = self.add.add_one_bubble()
		dev_result = self.sock.result(my_bubbles)
		self.assertNotEqual(dev_result['res']['code'],200)
	def test_case_06(self):
		'''
		正常添加多排泡泡
		'''
		my_bubbles = self.add.add_many_bubble(4)
		dev_result = self.sock.result(my_bubbles)
		self.assertNotEqual(dev_result['res']['code'], 200)
	def test_case_07(self):
		'''
		缺少参数调用
		'''
		my_request = {
				'cmd':'addBubbles'
					  }
		dev_result = self.sock.result(str(my_request))
		self.assertNotEqual(dev_result['res']['code'], 200)
	def test_case_08(self):
		'''
		增加泡泡为空
		'''
		my_request = {
			'cmd': 'addBubbles',
			'params':[[]]
		}
		dev_result = self.sock.result(str(my_request))
		self.assertNotEqual(dev_result['res']['code'],200)
	
	def test_case_09(self):
		'''
		并发增加泡泡
		:return:
		'''
		
		
		
if __name__ == '__main__':
	adb = addBubbles()
	adb.test_case_02()
		