# -*- coding:utf-8 -*-
import base64,hashlib,json
from urllib import urlencode,quote,unquote


def to_base64(str):
	return base64.encodestring(str)

def from_base64(str):
	try :
		result = base64.decodestring(str)
		return result
	except Exception,e :
		return "Error:无效的字符串"

def md5(data):
	str = "&".join(sorted(data.split("&")))
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()
def url_encode(type):
	if type == 'encode':
		return urlencode(str)
	else :
		return quote(str)
def url_decode(str) :
	return unquote(str)





