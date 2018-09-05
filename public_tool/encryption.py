# -*- coding:utf-8 -*-
import base64,hashlib,json,rsa
from urllib.parse import urlencode,quote,unquote


def to_base64(str):
	return base64.encodestring(str)

def from_base64(str):
	try :
		result = base64.decodestring(str)
		return result
	except Exception as e :
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

def rsa_in(msg,pubkey):

	crypto = rsa.encrypt(msg.encode(), pubkey)
	return crypto


if __name__ == '__main__':
	# result = from_base64('+EG6CbdyU/KS6E3jhlxMxLxrfEQfZOrOweVCUYj0wM+gX0pX9xbMVdQmjwoeu7duIUO2mWFEFgRjNuPub8Wm3w==')
	# print(result)
	(pubkey, privkey) = rsa.newkeys(512)
	print('pubkey',pubkey)
	#print(to_base64(pubkey))
	key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvMCkMUkh7AJqwUAecmgHZwQbiR4u7ZdOhuzoxZEhAZUjrBarfHvttwfKLFM1r2uXvuu2rrYKjpa1iUV2A4rLeHlPnT07IeelAFiUKbjOaqS1K1ByTjIFCz466B8bMRYIOA6Za5j4OcVaQvpgXWZicshHssLFCeYnj2f5XAYQFiS9It6lJ0gGJWT2YSD6WxMAV1JRCpLJE0rtV5egAqAp9UImsZDjE2mVHXCTjlQKsdi+8jRJatZFLwDqOU0RGlgmwcjdg6u511xWWaQX1G3IhSMRAjrY4FDxxYRKBGrkNBPAp34NodGWL1iEHD+GdR3wRvbIAnLNU0XDf2bEenMPzwIDAQAB'
	result = rsa_in('hello',pubkey)
	print(result)



