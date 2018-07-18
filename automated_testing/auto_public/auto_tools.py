# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 19:04
# @Author  : Huangmin
# @Site    : 
# @File    : tools.py
# @Software: PyCharm


import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from multiprocessing import Pool,Lock
from automated_testing.models import CaseInfo

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



#生成随机坐标,num:生成的坐标数量,max_x：最大的横坐标,max_y：最大的纵坐标,
def rdint(max_x,max_y,num,zero_flag =1):
	'''
	:param max_x: 最大的横坐标
	:param max_y: 最大的纵坐标
	:param num: 生成的坐标数量
	:param zero_flag: 是否从0开始,1代表从1开始
	:return: 列表
	'''
	from random import randint
	li = []
	for i in range(num):
		li.append((randint(zero_flag,max_x),randint(zero_flag,max_y)))
	return li

#判断2个坐标点是否相邻,data1及data2传递元组,如(1,2)
def adjacent(data1,data2):
	return False if abs(data1[0]-data2[0])>1 or abs(data1[1]-data2[1]) >1 else True


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

#找出与一个坐标相连的所有坐标点
def num_list(num,data_list):
	return [x for x in data_list if adjacent(x,num)]


#判断坐标点是否连线
def on_line(data):
	import queue
	if  not isinstance(data,tuple) and len(data) == 0:
		return False
	data_list = list(data)

	#接收找出的坐标结果
	result = list()
	#实例化队列
	q = queue.Queue()
	#首先加入一个到队列
	q.put(data_list.pop(0))
	while not q.empty():
		#循环取队列的数据
		for i in range(q.qsize()):
			num = q.get()
			#找出与该坐标点的所有坐标列表
			li = num_list(num,data_list)

			#将相邻的坐标点循环取出并放到队列
			for j in li:
				q.put(j)
				data_list.pop(data_list.index(j))
			result.append(num)
	#判断结果的长度是否和传入的元组长度一致，一致则代表相连
	return True if len(data) == len(result) else False


#此处示例表格中能连线的坐标
def conctorl(x,y):
	#生成矩阵坐标点
	mar = matrix((x,y))
	dic = {}
	#循环获取不同的连线方案
	for i in range(2,x*y+1):
		com = comb(mar,i)
		num = [x for x in com if on_line(x)]
		print("{}个点能连成线的坐标有{}个:\n{}".format(i,len(num),num))
		dic[i] ={'count':len(num),'data':num}
	return dic

#生成随机图案
def random_img():
	from random import choice
	#此处pic需要写配置
	pic = ('red','yellow','green','black','star')
	dic = {k:{'pic':choice(pic),'flag':0} for k in matrix((4,4))}
	return dic


def discover(dirs, starts='test', func_li='all', is_exec=0,**class_data):
	import sys, os
	#此处需要写配置
	sys_dir = 'D:\\Users\\huangmin\\git\\automated_testing\\test_case\\'
	from automated_testing.models import GameInfo
	game_name = dirs.split('_')[1]
	#根据文件名去数据库中获取游戏ID
	game_id = list(GameInfo.objects.filter(name=game_name).values('id'))[0]['id']
	
	path = sys_dir + dirs
	success_li = []
	fail_li = []
	if os.path.isdir(path):
		sys.path.append(path)
		#查找以传递进来的starts开头的py文件
		model = [x.split('.')[0] for x in os.listdir(path) if x.endswith('.py') and x.startswith(starts)]
		for i in model:
			if lazyimport(game_id, i, starts, func_li, is_exec,**class_data):
				#获取执行成功失败结果
				success, fail_list = lazyimport(game_id, i, starts, func_li, is_exec,**class_data)
				#将结果添加到结果集
				success_li.extend(success)
				fail_li.extend(fail_list)
		return success_li, fail_li
	else:
		msg = '错误的文件放置目录'
		return msg


def lazyimport(game_id, dirs, starts='test', func_li='all', is_exec=0,**class_data):
	u'''

	:param dirs: 文件名
	:param starts: 以starts开头的函数
	:param func_li: 需要执行的函数列表，默认全部执行
	:param is_exec: 是否执行,0不执行
	:return: 字典数据，第一层是类名,中间有类的属性，以及下面的函数列表
	'''
	import traceback
	from automated_testing.models import CaseInfo
	mod = __import__(dirs)
	mod_list = dir(mod)
	success = list()
	fail_list = list()
	for i in mod_list:
		Func = getattr(mod, i)
		class_memo = Func.__doc__
		class_name = i
		#筛选类
		if type(Func).__name__ == 'type':
			# 找出类下面所有的函数
			method = [x for x in dir(Func) if x.startswith(starts)]
			if len(method) > 0:
			# 循环执行类下面的函数
				for j in method:
					case_memo = getattr(Func, j).__doc__
					# 判断函数是否需要执行
					if is_exec:
						#判断类初始化是否需要传递参数
						if class_data:
							if class_name not in class_data['class_data'].keys():
								break
							#实例化类
							f = Func(class_data['class_data'][class_name])
						else:
							f = Func()
						#判断执行哪些函数
						if j in func_li or func_li == 'all':
							try:
								#执行函数
								getattr(f, j)()
								#未抛出异常则添加至成功信息
								success.append('{}:{}'.format(class_name, j))
							except AssertionError as e:
								#获取异常信息并添加到失败列表
								fail_list.append({'name': '{}:{}'.format(class_name, j),'case_memo':case_memo, 'fail_info': traceback.format_exc()})
						else:
							fail_list.append({'fail_info': '未找到该函数'})
					else:
						#不需要执行则入表，已经有了则不入表
						flag = CaseInfo.objects.filter(case_name = j,class_name = class_name)
						if not flag:
							CaseInfo.objects.get_or_create(case_name=j, class_name=class_name, case_memo=case_memo, class_memo=class_memo, game_id=game_id)
						#添加成功信息
						#success.append('{}:{}'.format(class_name, j))
	return success, fail_list


def get_exec_test(is_exec=0,**class_data):
	u'''
	获取test_case目录下面所有需要的case
	is_exec=1代表执行这些用例,0代表不执行
	'''
	sys_dir = 'D:\\Users\\huangmin\\git\\automated_testing\\test_case\\'
	test_dir = [x for x in os.listdir(sys_dir) if x.startswith('test')]
	result = {'success':[],'fail':[]}
	for i in test_dir:
		success, fail_list = discover(dirs=i, is_exec=is_exec,class_data=class_data.get(i))
		result['success'].extend(success)
		result['fail'].extend(fail_list)
	return result

def get_queue_id(flag = 0):
	'''
	:param flag:0:获取最大的队列ID,
	:return:
	'''
	from public_tool.tools import get_pool
	pool = get_pool()
	#此处需要写配置
	auto_queue_key = 'auto_queue_max'
	queue_id = int(pool.get(auto_queue_key))
	if flag == 0 :
		return queue_id
	elif flag ==1:
		pool.set(auto_queue_key,queue_id+1)
		return int(pool.get(auto_queue_key))

#将坐标转换成数字
def zuobiao_to_num(data):
	zuobiao = matrix((4,4))
	dic = dict(enumerate(zuobiao))
	new_dic = {v:k for k,v in dic.items()}
	return new_dic.get(data)

#字典中根据value获取key
def value_get_key(dicxx,value):
	return list(dicxx.keys())[list(dicxx.values()).index(value)]
#时间换算成秒数
def time_to_second(flag,num=1):
	if flag == 'year':
		return num*365*24*60*60
	elif flag == 'month':
		return num*30*24*60*60
	elif flag == 'week':
		return num*7 * 24 * 60 * 60
	elif flag == 'day':
		return num*24*60*60
	elif flag == 'hour':
		return num*60*60
	elif flag == 'minute':
		return num*60
class Uts():
	def __init__(self):
		pass
	def assertEqual(self,data1,data2):
			if not data1 == data2:
				raise AssertionError
			else:
				return True
	def assertTrue(self,data):
		if bool(data):
			return True
		else:
			raise AssertionError
	
	def assertIn(self,first,second):
		if first in second:
			return True
		else:
			raise AssertionError
	
	def assertFalse(self,data):
		if not bool(data):
			return True
		else:
			raise AssertionError
	
def write_log(filename,msg):
	path = '../report/'
	logname = path +filename+'.log'
	logfile = os.path.join(path,logname)
	with open(logname,'a+',encoding='utf-8') as f:
		f.write(msg)
	


def get_seed_data(seed_type,id):
	import ast,requests
	url = 'http://tst-kangji-wap-stg35.1768.com/?act=game_stars&st=get_seed&type={}&seed_id={}'
	urlinfo = url.format(seed_type,id)
	r = requests.get(urlinfo)
	d_result = r.content.decode()
	result = ast.literal_eval(d_result)
	return result

def init(l):
	global lock
	lock = l
def run_all_case(id,types =2):
	class_flag = {1:'Star_arr_game',2:'Star_skill_seed',3:'Star_reward_seed'}
	map_data = get_seed_data(types,id)
	if len(map_data)==0:
		write_log('seed_detail', u'未获取到种子信息\n种子类型：{},种子ID:{}\n'.format(types, id))
		return
	data = {class_flag[types]:map_data}
	result = discover(dirs='test_star',class_data=data,is_exec=1)
	write_log('seed_detail', u'种子类型：{},种子ID:{}\n'.format(types,id))
	# write_log('seed_detail', u'所有的种子信息{}\n'.format(result))
	if len(result[1])>0:
		fail_list = [x['case_memo'] for x in result[1]]
		write_log(class_flag[types], u'错误的种子,类型为:{},ID:{}\n 详细的错误信息:{}\n'.format(types, id, fail_list))

def run_all_queue(first,second,pool_num=4):
	import time
	start = time.time()
	data = map(str,range(first,second,2))
	lock = Lock()
	pool = Pool(pool_num,initializer=init,initargs=(lock,))
	pool.map_async (run_all_case, data)
	pool.close()
	pool.join()
	end = time.time()-start
	print(end)
	
if __name__ == '__main__':
	run_all_queue(30140,100000)




	


