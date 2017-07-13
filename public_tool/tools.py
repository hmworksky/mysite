# -*- coding:utf-8 -*-
# from ConfigParser import  ConfigParser


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

