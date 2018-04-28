#coding:utf-8
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

	def size_for_num(self,data):
		if data.endswith('G'):
			return float(data.replace('G', '')) * 1024 * 1024 * 1024
		if data.endswith('M'):
			return float(data.replace('M', '')) * 1024 * 1024
		if data.endswith('B'):
			return float(data.replace('B', '')) * 1024
	def get_branch(self,sort=False):
		import requests
		from public_tool.tools import Memcached
		r = eval(requests.get(url='http://caipiao3.stg3.1768.com/branch.txt').content)
		mem = Memcached()
		if sort:
			for i in r:
				i['size'] = self.size_for_num(i.get('size'))
			sort_data = sorted(r, key=lambda s: s.get('size'), reverse=True)
			mem.setmem('branch_sort', sort_data)
			return sort_data
		else:
			mem.setmem('branch', r)
			return r
	def run(self):
		self.get_branch()
		self.get_branch(sort = True)


if __name__ == '__main__':
	mem = Memcached()
	mem.run()