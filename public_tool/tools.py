# -*- coding:utf-8 -*-
from ConfigParser import  ConfigParser
import os,requests
from lxml import etree
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()


def case(**args):
	case_list = []
	case_conf = {"string":"aaa, ,111,<>,NULL,c1,中文","int":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,4294967297","float":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,3.45,-3.45,3.555,4.5555,4.12345,1.1.1"}
	for key,type in args.items() :
		case_value = case_conf[type].split(",")
		for item in case_value :
			str = "其它字段输入正常,{}字段输入:{}".format(key,item)
			case_list.append(str)
	return case_list

def readconfig(file,key):
    cf = ConfigParser()
    cf.read(file)
    sections = cf.sections()
    for i in sections:
        kvs = dict(cf.items(i))
        if key.lower() in kvs.keys():
            return  kvs[key.lower()]
        else :
            pass



def round(data):  # 百分比函数，传递一个数组，返回每个值对应的百分比
	li = []
	for i in data:
		num = i * 100.0 / sum(data)
		li.append(float('%.2f' % num))
	return li


def getsize(sizeInBytes):
	for (cutoff, label) in [(1024 * 1024 * 1024, "GB"), (1024 * 1024, "MB"), (1024, "KB"), ]:
		if sizeInBytes >= cutoff:
			return "%.1f %s" % (sizeInBytes * 1.0 / cutoff, label)
		if sizeInBytes == 1:
			return "1 byte"
		else:
			bytes = "%.1f" % (sizeInBytes or 0,)
	return (bytes[:-2] if bytes.endswith('.0') else bytes) + ' bytes'

def load_data_file():
	data_path = "D:\\SOFTWARE\\study\\auto\\selenium\\data\\log"
	os.chdir(data_path)

def strf_time(type):
	import time
	if type == 'time':
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	else:
		return time.strftime("%Y-%m-%d", time.localtime())

def logger(title,msg):
	#load_data_file()
	log_path = "{}.log".format(strf_time('date'))
	with open(log_path,"a+") as f:
		f.write("\n{}:---[{}]---:{}".format(strf_time('time'),title,msg))


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

class Sendmail(object):
	def __init__(self):
		self._errors = {}
		self.config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'config.conf')
	def __call__(self,content,subject,msg_to,types = None):
		'''
		:param content: 发送的内容
		:param subject: 主题
		:param msg_to: 收件人
		:param types: 默认是文本，如传递了html，则发送的是html
		:return: 0000成功，1001失败
		'''
		from email.mime.text import MIMEText
		import smtplib
		try:
			msg_from =readconfig('.','SERVER_MAIL_USER')
			self._s = smtplib.SMTP_SSL(readconfig(self.config_path,'SERVER_MAIL_HOST'), readconfig(self.config_path,'SERVER_MAIL_PORT'))
			self._s.login(msg_from, readconfig(self.config_path,'SERVER_MAIL_PWD'))
			if  types =='html':
				msg = MIMEText(content,_subtype='html', _charset='utf-8')
			else:
				msg =MIMEText(content)
			msg['Subject'] = subject
			msg['From'] =msg_from
			msg['To'] = msg_to
			self._s.sendmail(msg_from,msg_to,msg.as_string())
			self._errors['status'] = '0000'
			self._errors['msg'] = '发送成功'
			print self._errors
		except Exception,e:
			self._errors['status'] = '1001'
			self._errors['msg'] = '发送失败,{}'.format(e)
		finally:
			self._s.quit()
		return self._errors
	def __str__(self):
		return str(self._errors)
	__repr__ = __str__


#将url中的参数转化为字典
def url2Dict(url):
	import urlparse
	query = urlparse.urlparse(url).query
	return dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])


class Login(object):
	def __init__(self):
		'''
			用户名及密码后期改成传参
		'''
		self.config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.conf')
		self.session = requests.Session()
		self.login_user = readconfig(self.config_path,'PAW_LOGIN_USER')
		self.login_pwd = readconfig(self.config_path,'PAW_LOGIN_PWD')
		self.passport_login_form_url = readconfig(self.config_path,'PASSPORT_LOGIN_URL')
	def __call__(self,source):
		if source == 'game_pc':
			return self._game_pc_login()
		elif source == 'game_wap':
			return self._game_wap_login()

	def _game_pc_login(self):
		session = self.session
		game_pc_url = readconfig(self.config_path,'GAME_PC_LOGIN_URL')
		passport_login_url = session.get(url=game_pc_url, allow_redirects=False).headers.get('Location')

		# 从页面获取登录的form参数
		passport_html = session.get(url=passport_login_url, verify=False).content
		etrees = etree.HTML(passport_html)
		datas = url2Dict(etrees.xpath('//*[@id="id_pawform"]/div[2]/a/@href')[0])

		# 添加用户名密码参数
		datas['loginName'] = self.login_user
		datas['pwd'] = self.login_pwd

		# 发送登录请求,获取passport登录后的location
		login_location_url = session.post(url=self.passport_login_form_url, data=datas, verify=False, allow_redirects=False).headers.get('Location')
		print login_location_url
		# 跳转游戏页面
		session.get(login_location_url)

		#返回session信息
		return session

	def _game_wap_login(self):
		session = self.session
		game_wap_login_url = readconfig(self.config_path,'GAME_WAP_LOGIN_URL')
		#从wap页面获取passport请求
		game_to_passport_location_url = session.get(game_wap_login_url, allow_redirects=False).headers.get('Location')

		#请求passport login请求返回的登录页html
		passport_login_page = session.get(game_to_passport_location_url, verify=False).content

		#通过BS4获取下一个登录请求所需要的参数信息
		soup = BeautifulSoup(passport_login_page, 'lxml')
		div = soup.find_all('div', id='pawList2')
		new_soup = BeautifulSoup(str(div), 'lxml')
		data = url2Dict(new_soup.find('a').attrs.get('href'))

		#添加用户名密码
		data['loginName'] = self.login_user
		data['pwd'] = self.login_pwd

		#发送登录请求,获取passport登录后的location
		login_location_url = session.post(url=self.passport_login_form_url, data=data, verify=False, allow_redirects=False).headers.get('Location')

		#登录后跳转
		session.get(login_location_url)

		# 返回session信息
		return session


def read_excel(filename = None,sheetname = None):
	'''
	:param filename: excel文件路径
	:param sheetname: sheet名
	:return: example:[{"a":1},{"b":2}]，一行是一个字典，第一行是key，后面的每行为value
	'''
	import xlrd
	data = xlrd.open_workbook(filename)
	table = data.sheet_by_name(sheetname)
	li = []
	for i in range(table.nrows):
		li.append(table.row_values(i))

	#将第一行设为key
	key = li[0]

	#获取从第二行开始的值
	values = li[1:]

	#转化为字典
	datas = [dict(zip(key,value)) for value in values ]
	return datas

def django_return(data,sleep_time = 0):
	from django.http import JsonResponse,HttpResponse
	import json,time
	logger(2,2)
	time.sleep(sleep_time)
	if data.startswith("{"):
		data = json.loads(data)
		return JsonResponse(data)
	else:
		return HttpResponse(data)

if __name__ == '__main__':
	login = Login()
	session = login('game_pc')
	cookie = requests.utils.dict_from_cookiejar(session.cookies)
	print cookie