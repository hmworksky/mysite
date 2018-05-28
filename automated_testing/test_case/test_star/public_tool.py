# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 14:42
# @Author  : Huangmin
# @Site    : 
# @File    : all.py
# @Software: PyCharm
#from automated_testing.auto_public.auto_tools import *
from multiprocessing import Lock,Pool
import os,time


#判断坐标横线是否连成直线
def x_line(data):
	#获取X轴
	x = [n[0] for n in data]
	#获取Y轴
	y = [n[1] for n in data]
	#判断x轴是否连线(横线)
	x_flag = max(x)- min(x) ==0 and max(y) -min(y) == (len(data)-1)
	#判断y轴是否连线(竖线)
	y_flag = max(x)- min(x) ==(len(data)-1) and max(y) -min(y) ==0
	#判断斜线是否连线
	z_flag = x ==list(range(1,max(x)+1)) and y in(list(range(1,max(y)+1)),list(range(1,max(y)+1)[::-1]))
	#只要满足其中一个就是成功消除
	return True if x_flag or y_flag or z_flag else False

#生成矩阵坐标,x代表横坐标长度,y代表纵坐标长度
def matrix(datas):
	'''
	:param datas:元组，如：（4,4）
	:return: 列表
	'''
	x = datas[0]
	y = datas[1]
	li = []
	for i in range(1,x+1):
		for j in range(1,y+1):
			li.append((i,j))
	return li

#列出所有排列组合,data_list是需要排列的列表,num是每个排列的数量
def comb(data_list,num):
	from itertools import combinations
	return list(combinations(data_list,num))
#将坐标转换成数字
def zuobiao_to_num(data):
	zuobiao = matrix((4,4))
	dic = dict(enumerate(zuobiao))
	new_dic = {v:k for k,v in dic.items()}
	return new_dic.get(data)
#字典中根据value获取key
def value_get_key(dicxx,value):
	return list(dicxx.keys())[list(dicxx.values()).index(value)]
def write_log(filename,msg):
	path = filename+'.log'
	with open(path,'a+',encoding='utf-8') as f:
		f.write(msg)

def get_seed_data(seed_type,id):
	import ast,requests
	url = 'http://tst-kangji-wap-stg35.1768.com/?act=game_stars&st=get_seed&type={}&seed_id={}'
	urlinfo = url.format(seed_type,id)
	r = requests.get(urlinfo)
	d_result = r.content.decode()
	result = ast.literal_eval(d_result)
	return result
#
# def init(l):
# 	global lock
# 	lock = l
# def run_all_case(id,types =2):
#
# 	class_flag = {1:'Star_arr_game',2:'Star_skill_seed',3:'Star_reward_seed'}
# 	map_data = get_seed_data(types,id)
# 	if len(map_data)==0:
# 		write_log('seed_detail', u'未获取到种子信息\n种子类型：{},种子ID:{}\n'.format(types, id))
# 		return
# 	data = {class_flag[types]:map_data}
# 	result = discover(dirs='test_star',class_data=data,is_exec=1)
# 	write_log('seed_detail', u'种子类型：{},种子ID:{}\n'.format(types,id))
# 	# write_log('seed_detail', u'所有的种子信息{}\n'.format(result))
# 	if len(result[1])>0:
# 		fail_list = [x['case_memo'] for x in result[1]]
# 		write_log(class_flag[types], u'错误的种子,类型为:{},ID:{}\n 详细的错误信息:{}\n'.format(types, id, fail_list))
#
# def run_all_queue(first,second,func,pool_num=4):
# 	import time
# 	start = time.time()
# 	data = map(str,range(first,second,2))
# 	lock = Lock()
# 	pool = Pool(pool_num,initializer=init,initargs=(lock,))
# 	pool.map_async (func, data)
# 	pool.close()
# 	pool.join()
# 	end = time.time()-start
# 	print(end)


class Ut():
	def __init__(self):
		pass
	
	def assertEqual(self, data1, data2):
		if not data1 == data2:
			# raise AssertionError
			return False
		else:
			return True
	
	def assertTrue(self, data):
		if bool(data):
			return True
		else:
			# raise AssertionError
			return False
	
	def assertIn(self, first, second):
		if first in second:
			return True
		else:
			# raise AssertionError
			return False
	
	def assertFalse(self, data):
		if not bool(data):
			return True
		else:
			# raise AssertionError
			return True


class Tc:
	def __init__(self):
		self.pic = ('a', 'b', 'c', 'd', 'e')  # a:梅花,b:方块,c:红桃,d:黑桃,e:百搭
		self.rate = {'a': 0.2, 'b': 0.5, 'c': 1.0, 'd': 2.0, 'e': 3.0}  # 返奖倍率
		self.win_line_zuobiao = {#中奖线对应坐标
			"1":[0,1,2,3], "2":[4,5,6,7],"3":[8,9,10,11],"4":[12,13,14,15],
			"5":[0,4,8,12],"6":[1,5,9,13],"7":[2,6,10,14],"8":[3,7,11,15],
			"9":[0,5,10,15], "10":[3,6,9,12]
		}
	#单个版面中奖连线
	def win(self,maps):
		'''
		:param maps:传递版面图 列表，如['a','a','a','a','a','a','a','a','a',]
		:return: 返回中奖的连线，字典形式返回，如：{"1":[0,1,2,3], "2":[4,5,6,7]}
		'''
		self_martix = matrix((4, 4))  # 生成矩阵坐标
		self_martix_img = dict(zip(self_martix,maps))  # 将开发的首页图标对应到坐标中
		colour = [(x, 'e') for x in self.pic]
		win_list = {}
		for num, i in enumerate(colour):
			# 获取相同图标的坐标
			zuobiao = [k for k, v in self_martix_img.items() if v in i]
			# 组成排列组合
			new = comb(zuobiao, 4)
			_prize_num = [sorted(list(map(zuobiao_to_num,x))) for x in new if x_line(x)]
			if _prize_num:
				for i in _prize_num:
					win_list['{}'.format(value_get_key(self.win_line_zuobiao,i))] = i
		return win_list
	
	#单个版面倍数
	def rates(self,data):
		'''
		:param data: 传递列表，如['a','a','a','a','a','a','a','a','a',]
		:return: 此次版面的赔率
		'''
		win_list = self.win(data)
		count_rate = 0
		if len(win_list):
			for i in win_list.values():
				color = [data[x] for x in i]
				color = list(set(color))
				#判断是否只有一种颜色
				if len(color) == 1:
					color = color[0]
				#判断多种颜色
				elif len(color) ==2:
					color = [x for x in color if x !='e'][0]
				_rate = self.rate.get(color)
				count_rate += _rate
		return round(count_rate,2)
	
	def cmp_reward_page(self,map_list,reward_coord,reward_pic):
		'''
		:param map_list: 传递单个版面的列表
		:param reward_coord: 百搭的坐标位置
		:return: True or False
		'''
		result = [map_list[x] for x in reward_coord]
		return True if result.count(reward_pic) == len(result) else False
	
	#更新版面函数
	def update_banmian(self,map_list,update_data):
		'''
		:param map_list: 需要更新的列表
		:param update_data: 需要更新的版面，传递坐标及替换的图片，字典形式，ep:{'1':'a','4':'b'}
		:return: 返回更新后的列表
		'''
		for i in update_data.keys():
			value = update_data[i]
			i = int(i)
			map_list[i] = value
		return map_list
	
	#获取所有版面
	def all_banmian(self,data):
		import copy
		banmian_list = list()
		banmian_list.append(data.get('map'))
		_tmp_line = data.get('line')
		for i in _tmp_line:
			#获取列表中最后一个值
			_tmp_li = copy.deepcopy(banmian_list)[-1]
			#将最后一个值拿到后替换成新的版面
			_li = self.update_banmian(_tmp_li,i.get('replace'))
			#将新版面添加到整个版面列表
			banmian_list.append(_li)
		return banmian_list
		
	#统计总返奖倍数
	def count_rate(self,data):
		banmian_list = self.all_banmian(data)
		result = list(map(self.rates, banmian_list))
		return result[:-1]
	#统计所有的中奖线
	def all_win(self,data):
		banmian_list = self.all_banmian(data)
		all_win_result = list(map(self.win,banmian_list))
		return all_win_result
	#统计每屏的返奖倍数
	def all_rate(self,data):
		banmian_list = self.all_banmian(data)
		all_win_rate = list(map(self.rates,banmian_list))
		return  all_win_rate


	
	def get_list_index(self,first,second_list):
		return second_list[first]
	
	def prize_game(self,data):
		prize_list = self.all_win(data)
		banmian_list = self.all_banmian(data)
		prize_num = []
		for num ,data in enumerate(prize_list):
			for i in data.values():
				s = [self.get_list_index(x,banmian_list[num]) for x in i]
				if s.count('e')==4:
					prize_num.append(num)
		return prize_num
	
	def all_replace(self,data):
		def list_re(first):
			result = []
			for i in first:
				result.extend(i)
			return list(sorted(set(result)))
		all_win_list = self.all_win(data)
		li = []
		for x in all_win_list:
			tmp = list_re(x.values())
			li.append(tmp)
		return li


if __name__ == '__main__':
	maps = {'map': ['b', 'a', 'a', 'd', 'b', 'b', 'b', 'b', 'b', 'd', 'b', 'd', 'c', 'c', 'c', 'b'], 'line': [{'win': {'2': [4, 5, 6, 7], '9': [0, 5, 10, 15]}, 'odd': 1, 'replace': {'0': 'b', '4': 'a', '5': 'b', '6': 'a', '7': 'a', '10': 'b', '15': 'b'}}, {'win': {'9': [0, 5, 10, 15]}, 'odd': 0.5, 'replace': {'0': 'a', '5': 'a', '10': 'b', '15': 'c'}}, {'win': {'2': [4, 5, 6, 7], '4': [12, 13, 14, 15]}, 'odd': 1.2, 'replace': {'4': 'd', '5': 'a', '6': 'a', '7': 'd', '12': 'c', '13': 'c', '14': 'c', '15': 'c'}}, {'win': {'4': [12, 13, 14, 15]}, 'odd': 1, 'replace': {'12': 'd', '13': 'd', '14': 'd', '15': 'd'}}, {'win': {'4': [12, 13, 14, 15], '8': [3, 7, 11, 15]}, 'odd': 4, 'replace': {'3': 'c', '7': 'd', '11': 'a', '12': 'd', '13': 'd', '14': 'd', '15': 'd'}}, {'win': {'4': [12, 13, 14, 15]}, 'odd': 2, 'replace': {'12': 'e', '13': 'e', '14': 'e', '15': 'e'}}, {'win': {'4': [12, 13, 14, 15]}, 'odd': 3, 'replace': {'12': 'c', '13': 'b', '14': 'b', '15': 'd'}}], 'odd': 12.7, 'clear_page': 7, 'is_free': 1}
	t = Tc()
	s = t.all_replace(maps)
	print(s)
	dev = [list(map(int,x['replace'].keys())) for x in maps['line']]
	print(dev)
	#print(t.all_win(maps))
	print(s[:-1]==dev)