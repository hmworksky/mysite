# # -*- coding: utf-8 -*-
# # @Time    : 2018/4/26 15:29
# # @Author  : Huangmin
# # @Site    :
# # @File    : 1.py
# # @Software: PyCharm
#
#coding:utf-8

import requests,urllib
#屏蔽warning
requests.packages.urllib3.disable_warnings()
#
#
#
#将url中的参数转化为字典
def url2Dict(url):
	import urlparse
	query = urlparse.urlparse(url).query
	return dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])
#
#
# url = 'http://www.1768.com'
# # #get请求
# r = requests.get(url)
#
# print r.content
# #
# # #带header的请求
# # header = {
# # 	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
# # 	'xxx':'test'
# # }
# # h = requests.get(url , header)
#
#
# #带参数的get
# params = url2Dict('https://www.baidu.com/s?ie=utf-8&newi=1&mod=1&isbd=1&isid=9527eab800018904&wd=%E4%BA%8C%E5%93%88&rsv_spt=1&rsv_iqid=0x8c3281d200013789&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq=%25E4%25BA%258C%25E5%2593%2588&rsv_t=1d82c4iBn%2BO%2FI3u4tNatgg7Qsi7WYSZagHRkdrUVIYzgSqAtnzWuk7BYCvu7JT77pGgr&rsv_pq=9527eab800018904&bs=%E4%BA%8C%E5%93%88&rsv_sid=1454_21083_22073&_ss=1&clist=3551fa0a59604915%0935a1057c73f40554%09be498e4a9b127566%092e09ee3500ee5703&hsug=&f4s=1&csor=2&_cr1=35858')
# # p = requests.get(url = url ,params=params)
#
# #带cookie的请求
# cookie1= {'DEFAULT_TAB-IN_000040': 'paw', 'YOUXISID': '68249515c071d89d28282e8ead16b296ceba91dd', 'PHPSESSID': '35kdvmqs1b8k8gk02ufamio906', 'JSESSIONID': '1i2o8YpOb31qcivBwCwDZSBT.undefined'}
# c = requests.get(url = url,cookies = cookie1)
# print c.content
#
# # #POST请求
# # _p = requests.post(url,data)
#
# #证书、302跳转处理
# #证书设置不校验verify=False,禁止302跳转：allow_redirects=False

# #session
# s = requests.Session()
# s.get('***')

# #encode,decode
# # en = urllib.quote(params)
# # print en
# # print urllib.unquote(en)
#
# # #返回状态码
# # print r.status_code
# #
# # #查看编码
# # print r.encoding
# #
# # #查看头部header
# # print r.headers
# #
# # #查看cookie
# # print r.cookies
# #
# # #查看返回结果
# #
# # #字节流,原始串
# # print r.content


def  login():
	session = requests.Session()
	result = session.get('http://www.1768.com/?act=login',allow_redirects=False)
	location = result.headers.get('Location')
	passport_login = session.get(location,verify = False)
	print passport_login.content


if __name__ =='__main__':
	login()