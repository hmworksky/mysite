# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from collections import OrderedDict
# Create your views here.
from models import  InterfaceAttr



def create_case(request,id):
	session_id = request.session.session_key
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
		case_value = case_conf[type].split(",")
		for item in case_value :
			str = "其它字段输入正常,{}字段输入:{}".format(field,item)
			case_list.append(str)
		check_len = list(set([0,1,max,max-1,max+1,min,min-1,min+1]))
		for len in check_len :
			if type == 'string':
				str = "其它字段输入正常[长度校验],{}字段输入:{}".format(field,len*'a')
				case_list.append(str)
	return render_to_response('automated_testing/create_case.html',{'case_list':case_list,'interface_name':session_id})

