# -*- coding:utf-8 -*-
from ConfigParser import  ConfigParser
import requests
import re,os
from collections import defaultdict, OrderedDict
import heapq


def case(**args):
	case_list = []
	case_conf = {"string":"aaa, ,111,<>,NULL,c1,中文","int":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,4294967297","float":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,3.45,-3.45,3.555,4.5555,4.12345,1.1.1"}
	for key,type in args.items() :
		case_value = case_conf[type].split(",")
		for item in case_value :
			str = "其它字段输入正常,{}字段输入:{}".format(key,item)
			case_list.append(str)
	return case_list

def readconfig(key):
    cf = ConfigParser()
    cf.read("config.conf")
    sections = cf.sections()
    for i in sections:
        kvs = dict(cf.items(i))
        if key in kvs.keys():
            return  kvs[key]
        else :
            pass








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

def load_data_file():
	data_path = "D:\\SOFTWARE\\study\\auto\\selenium\\data\\log"
	os.chdir(data_path)

def strf_time(type):
	import time
	if type == 'time':
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	else:
		return time.strftime("%Y-%m-%d", time.localtime())

def logger(title,msg):
	load_data_file()
	log_path = "{}.log".format(strf_time('date'))
	with open(log_path,"a+") as f:
		f.write("\n{}:---[{}]---:{}".format(strf_time('time'),title,msg))


class Memcached:
	def __init__(self):
		from pymemcache.client.base import Client
		self.client = Client(('127.0.0.1',11211))

	def setmem(self,key,value):#设置修改缓存key
		return self.client.set(key,value)
	def getmem(self,key):
		return self.client.get(key)
	def delmem(self,key):
		return self.client.delete(key)



def zf_ticket_conctorl(ticket_info,state = 0):#0投注成功，1投注失败
    ticket_id = eval(ticket_info.keys()[0])["ticket_id"]
    ticket_list = []
    ticket_status = {0:"1000",1:"0007"}
    if len(ticket_id) == 1:
        if state == 0 :
            status = ticket_status.get(0)
        else:
            status = ticket_status.get(1)
        ticket_id = ticket_id[0]
        ticket_params = {"response":{"ticket":{"@attributes":{"ticketId":ticket_id,"status":status,"msg":"test1"}},"code":"0000","msg":"test2"}}
    else:
        times = 0
        for i in ticket_id:
            ticket_return = {} 
            ticket_r = {}
            ticket_return["ticketId"] = i
            ticket_return["msg"] = "test"
            if times ==0:
                status = ticket_status.get(0)
                times += 1
            else:
                status = ticket_status.get(1)
            ticket_return["status"] = status
            ticket_r["@attributes"] = ticket_return
            ticket_list.append(ticket_r)
        ticket_params = {"response":{"ticket":ticket_list,"code":"0000","msg":"test2"}}
    return ticket_params
def wucai_ticket_conctorl(ticket_info,state = 0):#state:0=投注成功，1=投注失败
    if state == 0 :
        status = "0000"
    else:
        status = "1011"
    ticket_params = {"response":{"code":status,"message":"wucai_test"}}
    return ticket_params
def zc_ticket_conctorl(ticket_info,state = 0):
    ticket_list = []
    orderid = eval(ticket_info.keys()[0])["ticket_id"]
    uuid = eval(ticket_info.keys()[0])["uuid"]
    status_code = {0:10000,1:10001}
    times = 0 
    for i in orderid:
        ticket_r = {}
        code = status_code.get(0)
        if state == 1:
            code = status_code.get(1)
        elif state not in (0,1):
            if times == 0:
                code = status_code.get(1)
                times += 1
        ticket_r["orderId"] = i
        ticket_r["code"] = code
        ticket_r["message"] = "zc_test"
        ticket_list.append(ticket_r)
    ticket_params = {"err":{"code":10000,"des":"zctest"},"tickets":ticket_list,"uuid":uuid}
    return ticket_params    
