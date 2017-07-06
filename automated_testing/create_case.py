# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
# Create your views here.
from public_tool.tools import case
from models import  InterfaceAttr



def create_case(request,id):
	case_list = []
	case_conf = {"string": "aaa, ,111,<>,NULL,c1,中文", "int": "2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,4294967297",
				 "float": "2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,3.45,-3.45,3.555,4.5555,4.12345,1.1.1"}
	result = InterfaceAttr.objects.filter(interface_id = int(id)).values("field","type","max","min","is_null")
	for item in result :
		field = item['field']
		type = item['type']
		max = item['max']
		min = item['min']
		is_null = item['is_null']
		re = case(field = field ,type = type )
	return HttpResponse(re)


def case(**args):
	case_list = []
	case_conf = {"string":"aaa, ,111,<>,NULL,c1,中文","int":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,4294967297","float":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,3.45,-3.45,3.555,4.5555,4.12345,1.1.1"}
	for key,type in args.items() :
		case_value = case_conf[type].split(",")
		for item in case_value :
			str = "其它字段输入正常,{}字段输入:{}".format(key,item)
			case_list.append(str)
	return case_list