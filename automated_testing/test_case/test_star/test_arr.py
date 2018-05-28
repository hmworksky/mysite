# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 19:02
# @Author  : Huangmin
# @Site    :
# @File    : test_star_all.py
# @Software: PyCharm


# coding:utf-8
# import sys
# sys.path.append('..')
from public_tool import Ut
from public_tool import Tc,write_log
from multiprocessing import Lock,Pool


class Star_arr_game(Ut):
	u'''星星风暴普通种子'''
	
	# def __init__(self):
	# 	super(Star_all_game,self).__init__()
	def __init__(self, data):
		# 种子信息
		self.data = data
		self.tc = Tc()
		self.first_win_flag = bool(self.data.get('line'))
		self.fail= []
	@property
	def test_case01(self):
		u'''判断首屏中奖线'''
		if self.first_win_flag:
			dev_first_win = self.data.get('line')[0].get('win')  # 获取开发的首屏中奖连线
			self_win = self.tc.win(self.data.get('map'))  # 自己算出来的首屏中奖连线
			if not  self.assertEqual(dev_first_win, self_win):
				self.fail.append(self.test_case01.__doc__)
		else:
			self.test_case04
	@property
	def test_case02(self):
		u'''判断首屏中奖线数量'''
		if self.first_win_flag:
			dev_first_win_len = len(self.data.get('line')[0].get('win'))
			self_win_len = len(self.tc.win(self.data.get('map')))
			if not self.assertEqual(dev_first_win_len, self_win_len):
				self.fail.append(self.test_case02.__doc__)
		else:
			self.test_case04
	@property
	def test_case03(self):
		u'''判断首屏中奖倍率'''
		if self.first_win_flag:
			dev_first_rate = self.data.get('line')[0].get('odd')
			self_first_rate = self.tc.rates(self.data.get('map'))
			if not  self.assertEqual(dev_first_rate, self_first_rate):
				self.fail.append(self.test_case03.__doc__)
		else:
			self.test_case04
	@property
	def test_case04(self):
		u'''首屏未中奖'''
		dev_win_line = self.data.get('line')
		if not dev_win_line:
			self_win = self.tc.win(self.data.get('map'))
			if not  self.assertEqual(bool(dev_win_line), bool(self_win)):
				self.fail.append(self.test_case04.__doc__)
		else:
			pass
	@property
	def test_case05(self):
		u'''首屏判断是否所有中奖坐标补充了图案'''
		if self.first_win_flag:
			dev_first_insert_img = list(self.data.get('line')[0].get('replace').keys())
			self_first_insert = list()
			[self_first_insert.extend(x) for x in self.tc.win(self.data.get('map')).values()]
			self_first_insert = list(map(str, sorted(set(self_first_insert))))
			if not self.assertEqual(self_first_insert, dev_first_insert_img):
				self.fail.append(self.test_case05.__doc__)
		else:
			self.test_case04
	@property
	def test_case06(self):
		u'''判断返奖总倍数'''
		if self.first_win_flag:
			dev_count_rate = self.data.get('odd')
			self_count_rate = round(sum(self.tc.count_rate(self.data)),2)
			if not  self.assertEqual(dev_count_rate, self_count_rate):
				self.fail.append(self.test_case06.__doc__)
		else:
			self.test_case04
	@property
	def test_case07(self):
		u'''判断消除层数'''
		if self.first_win_flag:
			dev_clear_page = self.data.get('clear_page')
			self_clear_page = len(self.tc.all_banmian(self.data)) - 1
			if not  self.assertEqual(dev_clear_page, self_clear_page):
				self.fail.append(self.test_case07.__doc__)
		else:
			self.test_case04
	@property
	def test_case08(self):
		u'''判断每个中奖线是否正确'''
		if self.first_win_flag:
			dev_all_win = [x.get('win') for x in self.data.get('line') ]
			self_all_win = [x for x in self.tc.all_win(self.data) if len(x)>0]
			if not self.assertEqual(dev_all_win, self_all_win):
				self.fail.append(self.test_case08.__doc__)
		else:
			self.test_case04
	@property
	def test_case09(self):
		u'''判断每个返奖倍数是否正确'''
		if self.first_win_flag:
			dev_all_rate = [x.get('odd') for x in self.data.get('line') ]
			#将最后不中奖的倍数加到列表
			dev_all_rate.append(0)
			#将列表的每个值转换成浮点
			dev_all_rate = list(map(float,dev_all_rate))
			#自己计算出每个返奖倍数
			self_all_rate = [x for x in self.tc.all_rate(self.data)]
			if not  self.assertEqual(dev_all_rate, self_all_rate):
				self.fail.append(self.test_case09.__doc__)
		else:
			self.test_case04
	@property
	def test_case10(self):
		u'''判断是否免费游戏'''
		if self.first_win_flag:
			dev_free_flag = self.data.get('is_free')
			self_free_flag = self.tc.prize_game(self.data)
			self_free_flag = 1 if len(self_free_flag)>0 else 0
			if not  self.assertEqual(dev_free_flag, self_free_flag):
				self.fail.append(self.test_case10.__doc__)
		else:
			self.test_case04
	@property
	def test_case11(self):
		u'''判断是否免费游戏位置'''
		if self.first_win_flag:
			self_free_flag = self.tc.prize_game(self.data)
			if len(self_free_flag)>0:
				if not self.assertEqual(len(self.tc.all_banmian(self.data))-2,self_free_flag[0]):
					self.fail.append(self.test_case11.__doc__)
			else:
				self.test_case10
		else:
			self.test_case04
	@property
	def test_case12(self):
		u'''判断每次替换坐标是否正确'''
		if self.first_win_flag:
			dev_replace = [list(map(int,x['replace'].keys())) for x in self.data['line']]
			self_replace = self.tc.all_replace(self.data)[:-1]
			if not self.assertEqual(dev_replace,self_replace):
				self.fail.append(self.test_case12.__doc__)
		else:
			self.test_case04
	
	def run_all_case(self,id):
		self.test_case01
		self.test_case02
		self.test_case03
		self.test_case04
		self.test_case05
		self.test_case06
		self.test_case07
		self.test_case08
		self.test_case09
		self.test_case10
		self.test_case11
		self.test_case12
		return self.fail
if __name__ == '__main__':
	from public_tool import get_seed_data
	import time,traceback
	start = time.time()
	for i in range(700000,1000000,2):
		
		data = get_seed_data(1,i)
		if len(data) == 0 :
			write_log('normal_null', 'id:{}\n'.format(i))
			continue
		
		try:
			tc = Star_arr_game(data)
			result = tc.run_all_case(i)
			write_log('normal_detail', 'id:{},detail:{}\n'.format(i, result))
			if len(result)>0:
				write_log('normal_fail', 'id:{}\n,detail:{}\n'.format(i, result))
		except:
			write_log('normal_except', 'id:{}\n,detail:{}\n'.format(i, traceback.format_exc()))
	
	end = time.time()-start
	print(end)
	
	
