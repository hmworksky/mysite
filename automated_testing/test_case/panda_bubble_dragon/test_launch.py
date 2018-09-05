# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 17:28
# @Author  : Huangmin
# @Site    : 自己发射泡泡-9
# @File    : test_launch.py
# @Software: PyCharm





from automated_testing.test_case.public.bubble_tool import assertResult, addBubble,Bubble



class Launch(Bubble,assertResult, addBubble):
	def __init__(self):
		self.cmd = 'land'
		Bubble.__init__(self,'self')
		self.bubble = {
			"c":"red",
			"s":1,#status泡泡状态，1：未销毁，0:已销毁
			"t":1,#泡泡的类型（1：普通泡泡，2：爆炸泡泡，3：闪电泡泡，4：精灵泡泡）
			"id":1#泡泡编号
		}
		self.step = 0
	@property
	def add_step(self):
		self.step += 1
		return self.step
	
	def test_case_land_01(self):
		'''
		正常发射一个普通泡泡
		'''
		#获取发射前的面板
		old_pannel = self.get_new_pannel
		path = self.bubble_path(34)#34为角度，此处计算路径
		drop = self.find_all_eliminate(path[-1],self.bubble.get('c'))
		parse_drop = [dict(zip(('x','y'),i)) for i in drop]
		eliminate = parse_drop
		
		
		self.equal_result(self.cmd, userId=self.user_id, pannel=self.get_new_pannel, dropBubbles=self.add_many_bubble(3))
	
	def test_case_land_02(self):
		'''
		异常通知,此处添加了0行泡泡
		'''
		self.equal_result(self.cmd, is_equal=False, userId=self.user_id, pannel=self.get_new_pannel, dropBubbles=self.add_many_bubble(0))
	
	def test_case_land_03(self):
		'''
		添加的泡泡中有异常数据，一行全是爆炸泡泡（单数行）
		'''
		self.equal_result(self.cmd, is_equal=False, userId=self.user_id, pannel=self.get_new_pannel, dropBubbles=self.add_one_bubble(type=2))
	
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
		# 第二次判断为失败
		self.equal_result(self.cmd, is_equal=False, userId=self.user_id, pannel=self.get_new_pannel, dropBubbles=self.add_many_bubble(3))


if __name__ == '__main__':
	b = Launch()