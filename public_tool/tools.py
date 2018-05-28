# -*- coding:utf-8 -*-
from configparser import  ConfigParser
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
import redis



def case(**args):
	case_list = []
	case_conf = {"string":"aaa, ,111,<>,NULL,c1,中文","int":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,4294967297","float":"2,10000,0,-1,3.3,-3.3,中文,a, ,NULL,<>,3.45,-3.45,3.555,4.5555,4.12345,1.1.1"}
	for key,type in args.items() :
		case_value = case_conf[type].split(",")
		for item in case_value :
			str = "其它字段输入正常,{}字段输入:{}".format(key,item)
			case_list.append(str)
	return case_list

def readconfig(file = 'config.conf',key = None):
    cf = ConfigParser()
    cf.read(file).decode('utf-8')
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

def strf_time(type='date'):
	import time
	if type == 'time':
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	else:
		return time.strftime("%Y-%m-%d", time.localtime())

def logger(title,msg):
	#load_data_file()
	log_path = "log/{}.log".format(strf_time('date'))
	if os.path.exists(log_path):
		with open(log_path,"a+") as f:
			f.write("\n{}:---[{}]---:{}".format(strf_time('time'),title,msg))
	else:
		with open(log_path,"w") as f:
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
		except Exception as e:
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
	from urllib import parse
	query = parse.urlparse(url).query
	return dict([(k, v[0]) for k, v in parse.parse_qs(query).items()])




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


def get_pool():
	u'''获取redis连接池'''
	p = redis.ConnectionPool(host ='127.0.0.1',port=6379)
	pool = redis.Redis(connection_pool=p)
	return pool





	

