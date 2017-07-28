# -*- coding:utf-8 -*-
# from ConfigParser import  ConfigParser
import requests
import re
from collections import defaultdict, OrderedDict
import heapq

import MySQLdb


def case(**args):
	case_list = []
	case_conf = {"string":"aaa, ,111,<>,NULL,c1,中文","int":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,4294967297","float":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,3.45,-3.45,3.555,4.5555,4.12345,1.1.1"}
	for key,type in args.items() :
		case_value = case_conf[type].split(",")
		for item in case_value :
			str = "其它字段输入正常,{}字段输入:{}".format(key,item)
			case_list.append(str)
	return case_list

# def readconfig(key):
#     cf = ConfigParser()
#     cf.read("config.conf")
#     sections = cf.sections()
#     for i in sections:
#         kvs = dict(cf.items(i))
#         if key in kvs.keys():
#             return  kvs[key]
#         else :
#             return False
def mysql_conn(sql):
	try :
		conn = MySQLdb.connect(host = "127.0.0.1",port = "3306",user='root',passwd='test1324',db='test1324',charset='utf8')
	except Exception ,e :
		return e
	cursor = conn.cursor()
	li = []
	if sql.startswith("select"):
		cursor.execute(sql)
		values = cursor.fetchall()
		for i in values :
			li.append(i)
		return li
	else :
		cursor.execute(sql)
		return cursor.rowcount

def time_conctrol(str):
	str = str+":00"
	str = str.replace('/','-')
	return str





# 从页面读取分支环境信息，返回列表
def datas():
	r = requests.get(url='http://10test71.stg3.1768.com/branch3.txt')
	text = r.text
	text1 = text.split(".")
	list_result = []
	re_branch = re.compile(r'^\*(.*)')
	re_pwd = re.compile(r'^/data.*')
	re_size = re.compile(r'^\d(.*)')
	for i in text1:

		i = i.encode('utf-8')
		i = i.split("\n")
		i = [x for x in i if re_branch.findall(x) or re_pwd.findall(x) or re_size.findall(x)]
		if len(i) == 0:
			del i
		elif len(i) == 2:
			i.insert(1, 'None')
			list_result.append(i)
		else:
			list_result.append(i)
	return list_result


# 接收返回数量以及返回类型，0代表字典，1代表列表
def branch_data(nums, type=0):
	branchs = datas()
	k = defaultdict(str)
	for data in branchs:
		dirs = data[0].split("/")[-2]
		app = data[0].split("/")[-1]
		branch = data[1]
		size = int(data[2])
		k[size] = "{}/{}:{}".format(dirs, app, getsize(size))
		size_p = getsize(size)
	max_size = map(int, k.keys())
	max_size = heapq.nlargest(nums, max_size)
	li = []
	application = []
	size1 = []
	for i in max_size:
		application.append(k[i])
		size1.append(i)
	li.append(application)
	li.append(size1)
	result = OrderedDict(map(list, sorted(k.iteritems(), key=lambda d: d[0], reverse=True)[0:nums]))  # 获取最大的nums数量的key的字典
	if type == 1:
		return li
	else:
		return result


def round(data):  # 百分比函数，传递一个数组，返回每个值对应的百分比
	li = []
	for i in data:
		num = i * 100.0 / sum(data)
		li.append(float('%.2f' % num))
	return li


def getsize(sizeInBytes):
	for (cutoff, label) in [(1024 * 1024 * 1024, "GB"), (1024 * 1024, "MB"), (1024, "KB"), ]:
		if sizeInBytes >= cutoff:
			return "%.1f %s" % (sizeInBytes * 1.0 / cutoff, label)
		if sizeInBytes == 1:
			return "1 byte"
		else:
			bytes = "%.1f" % (sizeInBytes or 0,)
	return (bytes[:-2] if bytes.endswith('.0') else bytes) + ' bytes'



