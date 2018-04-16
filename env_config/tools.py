# -*- coding:utf-8 -*-
def branch_list():
	import requests
	branch = eval(requests.get(url = 'http://caipiao3.stg3.1768.com/branch.txt').text)
	return branch



