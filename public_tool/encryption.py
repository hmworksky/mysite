# -*- coding:utf-8 -*-
import base64,hashlib,json
from urllib import urlencode,quote,unquote


def to_base64(data):
	return base64.encodestring(data)

def from_base64(data):
	try :
		result = base64.decodestring(data)
		return result
	except Exception,e :
		return "Error:无效的字符串"

def md5(data,upper = False):#MD5加密
	m = hashlib.md5()
	m.update(data)
	if upper:
		return m.hexdigest().upper()
	return m.hexdigest()
def capstring(data):#排序后首字母大写
	data = "&".join(map(str.capitalize,sorted(data.split("&"))))
	return data
def url_encode(data):
	if data.startswith("{"):
		return urlencode(data)
	else :
		return quote(data)
def url_decode(data) :
	return unquote(data)

import HTMLParser

def decodeHtml(input):
    h = HTMLParser.HTMLParser()
    s = h.unescape(input)
    return s
# if __name__ == '__main__':
# 	print decodeHtml('\u96ea\u7eba\u886b')
# 	data ="http://caipiao.1768.com/?act=login&st=aetUserInfo&r=0.6611363720645511"
# 	print md5(data,upper=1)



