# -*- coding:utf-8 -*-
from ConfigParser import  ConfigParser


def case(**args):
	case_list = []
	for key,value in args.items() :
		case_value = readconfig(key).split(",")
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
            return False

