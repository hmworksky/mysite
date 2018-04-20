# coding:utf-8



def get_branch(sort = False):
	import requests
	from public_tool.tools import Memcached
	r = eval(requests.get(url = 'http://caipiao3.stg3.1768.com/branch.txt').content)
	mem = Memcached()
	if sort:
		for i in r:
			i['size'] = size_for_num(i.get('size'))
		sort_data = sorted(r, key=lambda s: s.get('size'), reverse=True)
		mem.setmem('branch_sort',sort_data)
		return sort_data
	else:
		mem.setmem('branch', r)
		return r

def size_for_num(data):
	if data.endswith('G'):
		return float(data.replace('G',''))*1024*1024*1024
	if data.endswith('M'):
		return float(data.replace('M',''))*1024*1024
	if data.endswith('B'):
		return float(data.replace('B',''))*1024


#数字转成字符串size
def getsize(sizeInBytes):
	for (cutoff, label) in [(1024 * 1024 * 1024, "GB"), (1024 * 1024, "MB"), (1024, "KB"), ]:
		if sizeInBytes >= cutoff:
			return "%.1f %s" % (sizeInBytes * 1.0 / cutoff, label)
		if sizeInBytes == 1:
			return "1 byte"
		else:
			bytes = "%.1f" % (sizeInBytes or 0,)
	return (bytes[:-2] if bytes.endswith('.0') else bytes) + ' bytes'
if __name__ == '__main__':
	print get_branch(sort = True)