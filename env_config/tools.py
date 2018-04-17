# coding:utf-8



def get_branch():
	import requests
	r = eval(requests.get(url = 'http://caipiao3.stg3.1768.com/branch.txt').content)
	return r

