# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 18:01
# @Author  : Huangmin
# @Site    : 
# @File    : checkinterface.py
# @Software: PyCharm

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from automated_testing.models import InterfaceAttr
from interface_control.models import InterfaceInfo
class CheckInterface(object):
	def __init__(self,interface_id):
		self.interface_id= interface_id
		self.field_info = list(InterfaceAttr.objects.filter(interface_id=self.interface_id).values('type', 'min', 'max', 'field', 'is_null'))
		self.type_list = {"string": ['aaa','111','<>','NULL','c1','中文'], "int": [2,10000,0,-1,3.3,-3.3,'中文','a','<>',4294967297],
				 "float": [2,10000,0,-1,3.3,-3.3,'中文','a','<>','Null',3.45,-3.45,3.555,4.5555,4.12345,'1.1.1'],"date":['a',13,'2018-05-20']}
		self.data = self.set_default_data
		pass
	
	def check_type(self,dev_type):
		if dev_type == 1:
			return self.type_list['string']
		elif dev_type == 2:
			return self.type_list['int']
		elif dev_type ==3:
			return self.type_list['date']
		elif dev_type == 4:
			return self.type_list['float']
		
	@property
	def set_default_data(self):
		data = {}
		for x in self.field_info:
			data[x.get('field')]=1 if int(x.get('type')) in (1,2) else 'a'
		return data
	
	def check_null(self,field):
		dev_null_flag = InterfaceAttr.objects.get(interface_id = self.interface_id,field=field).is_null
		if dev_null_flag == 0:
			return ''
		else:
			null_list = ['',' ','Null','null',None]
			for i in null_list:
				tmp_data = self.data
				tmp_data[field] = i
				
	def check_max(self):
		pass
	def check_min(self):
		pass
	def request_data(self,data):
		import requests
		url = InterfaceInfo.objects.get(id = self.interface_id).url_info
		result = requests.post(url = url,data=data)
		return result
		
	def check_all_field(self):
		self.check_max()
		self.check_min()
		self.check_null()
		self.check_type()
		

if __name__ == '__main__':
	ck = CheckInterface(12)
	ck.check_null('userId')