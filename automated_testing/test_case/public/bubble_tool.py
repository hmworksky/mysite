# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 14:51
# @Author  : Huangmin
# @Site    : 
# @File    : bubble_tool.py
# @Software: PyCharm
import traceback,json
from random import choice
from automated_testing.config import config
from public_tool import mySocket,myDecorator
from automated_testing.auto_public.auto_tools import Uts





class addBubble(object):
	def __init__(self):
		self.color_list = ['red','green','blue','white','purple']
		super(addBubble,self).__init__()
	
	def add_one_bubble(self,is_singular=True,type = 1,color = 'random'):
		'''
		增加一行泡泡
		:param type: 泡泡类型,1.普通泡泡、2爆炸泡泡、3闪电泡泡、4精灵泡泡
		:param is_singular: 首行是否是单行
		:param color: 泡泡颜色，传入random则代表所有泡泡随机
		:return: 列表
		'''
		bubble_num = config.line_num if is_singular else  config.line_num+1
		result = [{'color':self.get_random_color if color =='random' else color,'status':1,'type':type} for _ in range(bubble_num) ]
		return  result
	def add_many_bubble(self,nums, is_singular=True,type = 1,color = 'random'):
		'''
			增加多行泡泡
			:param nums: 生成多少行泡泡
			:param type: 泡泡类型
			:param is_singular: 首行是否是单行
			:param color: 泡泡颜色，传入random则代表所有泡泡随机
			:return: 列表
		'''
		result = []
		if nums>0:
			for _ in range(nums):
				result.append(self.add_one_bubble(is_singular,type,color))
				is_singular = self.set_true_false(is_singular)
		return result
	def set_true_false(self,status):
		'''
		返回相反的布尔值
		:param status:布尔值
		:return:True or False
		'''
		return False if status else True
		
	@property
	def get_random_color(self):
		'''
		获取随机的泡泡颜色
		:return:
		'''
		color = choice(self.color_list)
		return color
	
	def update_bubble_map(self):
		pass
	

class buildRequest:
	'''
	构造请求数据
	'''
	default = {
			"cmd":None,
			"params":{}
		}
	@classmethod
	def build(cls,cmd,is_list=None,**kwargs):
		cls.default['cmd'] = cmd
		cls.default['params'] = kwargs if not isinstance(is_list,list) else is_list
		return str(cls.default)
	
class assertResult(Uts):
	def __init__(self):
		self.config = config
		self.user_id = config.default_userid
		self.sock = mySocket.gameSock(self.config.bubbles_dev_socket_url)
		#self.add = addBubble()
		self.build = buildRequest()
		super(assertResult, self).__init__()
	
	def equal_result(self,cmd,is_equal=True,is_list = None,**kwargs):
		my_request = self.build.build(cmd,is_list,**kwargs)
		dev_result = self.sock.result(my_request)
		if is_equal:
			self.assertEqual(dev_result['res']['code'], 200)
		else:
			self.assertNotEqual(dev_result['res']['code'], 200)
	
	@property
	def get_new_pannel(self):
		return parse_replay_data(self.sock.result(buildRequest.build('replay', roomId=1001)), 'res_data_self_pannel')


def parse_replay_data(data,key):
	try:
		json_data = json.loads(data) if isinstance(data,str) else data
		for i in key.split('_'):
			json_data = json_data[i]
	except :
		return {}
	return json_data


class Bubble(object):
	def __init__(self, role):
		self.role = 'self' if role == 1 else 'enemy'
		self.res = self.get_layout
		# layout整个版面布局
		self.layout = self.res['data'][self.role]['bubbles']
		self.need_eliminate_list = []
		self.error = {'code': None, 'message': None}
		super(Bubble,self).__init__()
	
	@property
	def get_layout(self):
		'''
		获取整个版面信息,待完成
		目前从generate_layout(自己写的测试函数)中获取
		:return:字典
		'''
		return self.generate_layout
	
	def find_around_bubble(self, eliminate_list):
		'''
		找出所有需要消除的泡泡
		:param bubble_flag:
		:param initial_coordinate:
		:return: list
		'''
		self.need_eliminate_list += eliminate_list
		self.need_eliminate_list = list(set(self.need_eliminate_list))
		print('tmp_list', self.need_eliminate_list)
		for num, x in enumerate(eliminate_list):
			result = self.find_six_bubble(x, self.get_coordinate_color(x))
			print('获取周围6个结果:', result)
			# 筛选不在已递归的列表内的数据
			result = [x for x in result if x not in self.need_eliminate_list]
			print('find_around_bubble:', result)
			if len(result) == 0:
				continue
			else:
				self.need_eliminate_list += result
				self.find_around_bubble(result)
		
		return self.need_eliminate_list
	
	def bubble_path(self,angle):
		'''待补充'''
		pass
	def find_all_eliminate(self,initial_coordinate,color):
		'''
		找出所有需要消除的泡泡
		:param initial_coordinate:
		:param color:
		:return:
		'''
		six = self.find_six_bubble(initial_coordinate, color)
		print('入口函数，打印find_six_bubble函数结果', six)
		all_eliminate = self.find_around_bubble(six)
		return all_eliminate
	
	def random_blasting(self):
		import random
		'''
		随机泡泡5个单位
		:return:
		'''
		all_coordinates = list()
		for x, y in enumerate(self.layout):
			for m in range(len(y) - 1):
				all_coordinates.append((m, x))
		return random.sample(all_coordinates, 5)
	
	def horizontally_blasting(self, initial_coordinate):
		'''
		横排爆破
		:param initial_coordinate: 元组类型,example:(2,3)
		:return: list
		'''
		y = initial_coordinate[1]
		x_len = len(self.layout[y])
		return [(x, y) for x in range(x_len)]
	
	def landscape_blasting(self, initial_coordinate):
		'''
		竖排爆破
		:param initial_coordinate: 元组类型,example:(2,3)
		:return: list
		'''
		x = initial_coordinate[0]
		y_len = len(self.layout)
		return [(x, y) for y in range(y_len)]
	
	def six_units_per_week(self, initial_coordinate):
		x, y = initial_coordinate
		if y % 2 == 0:
			result = [(x - 1, y), (x + 1, y), (x, y - 1), (x - 1, y - 1), (x, y + 1), (x - 1, y + 1)]
		else:
			result = [(x - 1, y), (x + 1, y), (x, y - 1), (x + 1, y - 1), (x, y + 1), (x + 1, y + 1)]
		return result
	
	def find_six_bubble(self, initial_coordinate, color, bubble_flag=1):
		'''
		找出发射落点位置周围的6个泡泡
		:param initial_coordinate: 元组类型,example:(2,3)
		:param bubble_flag: 1->普通泡泡,2-》爆炸泡泡，3-》闪电泡泡，4-》精灵泡泡，5-》无色泡泡
		:return: list
		'''
		print('this initial_coordinate', initial_coordinate)
		print('find_six_bubble color', color)
		self.update_layout_status(initial_coordinate, 0)
		x, y = initial_coordinate
		if y % 2 == 0:
			result = [(x - 1, y), (x + 1, y), (x, y - 1), (x - 1, y - 1), (x, y + 1), (x - 1, y + 1)]
		else:
			result = [(x - 1, y), (x + 1, y), (x, y - 1), (x + 1, y - 1), (x, y + 1), (x + 1, y + 1)]
		
		# 判断坐标边界
		# result ={x:self.check_coordinate(x) for x in result}
		
		
		result = [x for x in result if self.check_coordinate(x) == True]
		print('result_1', result)
		result1 = {x: self.get_coordinate_color(x) for x in result}
		print('find_six_bubble,查看颜色:', result1)
		
		# 筛选未消除的泡泡
		result = [x for x in result if self.check_coordinate_status(x) == 1]
		
		# 判断该坐标点是否重叠未消除
		if y < len(self.layout) - 1:
			if self.check_coordinate_status(initial_coordinate) == 1:
				# print('进入重叠判断')
				self.error['code'] = 1001
				self.error['message'] = 'Wrong coordinate point'
				return self.error
		
		# 判断如果是普通泡泡则筛选颜色相同的,后续有其它颜色继续添加elif判断
		if bubble_flag == 1:
			result = [x for x in result if color == self.get_coordinate_color(x)]
			result = self.determine_length(result)
		
		return result
	
	def determine_length(self, data, length=3):
		'''
		查看列表长度是否小于3，小于3则返回空列表
		:param data:
		:return: list
		'''
		return [] if len(data) < length else data
	
	def get_coordinate_color(self, coordinate):
		'''
		获取坐标点对应的颜色
		:param coordinate: 元组类型,example:(2,3)
		:return: 字符串,example:'red'
		'''
		x, y = coordinate
		color = self.res['data'][self.role]['bubbles'][y][x]['color']
		# print('第{}行,第{}个，颜色为：'.format(y,x),color)
		return color
	
	def check_coordinate_status(self, coordinate):
		'''
		检查坐标状态
		:param coordinate:
		:return:
		'''
		x, y = coordinate
		coordinate_value = self.res['data'][self.role]['bubbles'][y][x]
		status = 1 if len(coordinate_value) > 0 else 0
		return status
	
	def check_coordinate(self, coordinate):
		'''
		检查坐标点是否符合要求
		:param coordinate:
		:return: bool
		'''
		
		x, y = coordinate
		if y % 2 == 0:
			if x > 10 or x < 0:
				return False
		else:
			if x > 9 or x < 0:
				return False
		
		y_rows = len(self.res['data'][self.role]['bubbles'])
		if y < 0 or y > y_rows - 1:  # 判断Y轴是否小于0
			return False
		return True
	
	def update_layout_status(self, coordinate, status):
		'''
		更新版面状态
		:return:
		'''
		x, y = coordinate
		if y > len(self.layout) - 1:
			return 'y长度超过版面'
		print('y:', self.res['data'][self.role]['bubbles'][y])
		print('y:', len(self.res['data'][self.role]['bubbles'][y]))
		self.res['data'][self.role]['bubbles'][y][x]['status'] = status
		return
	
	def generate_x(self, flag):
		import random
		color_list = ['red', 'yellow', 'blue', 'green', 'violet']
		tmp_list = []
		
		for _ in range(11):
			data = {
				'color': random.choice(color_list),
				'status': 1,
				'type': 1
			}
			tmp_list.append(data)
		return tmp_list if flag else tmp_list[:-1]
	
	@property
	def generate_layout(self):
		'''
		测试用，生成整个res
		:return:
		'''
		
		bubbles = []
		for x in range(10):
			flag = 1
			if x % 2 != 0:
				flag = 0
			data = self.generate_x(flag)
			bubbles.append(data)
		response = {
			'code': 200,
			'id': 1,
			'data': {
				'self': {
					'config': {
						'skin': {'vs': '1111', 'bubble': '111', 'head': '222'}
					},
					'bubbles': bubbles
				},
				'enemy': {
					'config': {
						'skin': {'vs': '1111', 'bubble': '111', 'head': '222'}
					},
					'bubbles': bubbles
				}
			}
		}
		return response
	
	

if __name__ == '__main__':
	# t = parse_replay_data('{"res":1,"dev":{"r":2}}','dev_r')
	# print(t)
	b = Bubble('self')
	b.find_all_eliminate((5,6),'red')
	