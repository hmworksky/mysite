# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 17:16
# @Author  : Huangmin
# @Site    : 
# @File    : request_server.py
# @Software: PyCharm
from requests import post



class requestServer(object):
	def __init__(self, server_host: object) -> object:
		self.server_host = server_host
	
	def my_request(self,data):
		result = post(self.server_host,data).content
		return result