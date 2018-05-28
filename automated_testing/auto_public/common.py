# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 19:04
# @Author  : Huangmin
# @Site    : 
# @File    : common.py
# @Software: PyCharm

import os,sys
import  configparser

def readconfig(file,key):
    cf = configparser.ConfigParser()
    cf.read(file)
    sections = cf.sections()
    for i in sections:
        kvs = dict(cf.items(i))
        if key.lower() in kvs.keys():
            return  kvs[key.lower()]
        else :
            pass

def strf_time(type = 'date'):
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
		from email.mime.multipart import MIMEMultipart
		import smtplib
		msg_from = readconfig(self.config_path, 'SERVER_MAIL_USER')
		s = smtplib.SMTP_SSL(readconfig(self.config_path, 'SERVER_MAIL_HOST'), readconfig(self.config_path, 'SERVER_MAIL_PORT'))
		try:
			s.login(msg_from, readconfig(self.config_path,'SERVER_MAIL_PWD'))
			if  types =='html':
				# msg = MIMEText(content,_subtype='html', _charset='utf-8')
				msg = MIMEMultipart()
				msg.attach(MIMEText(content, 'html', 'utf-8'))
			else:
				msg =MIMEText(content)
			msg['Subject'] = subject
			msg['From'] =msg_from
			msg['To'] = msg_to
			s.sendmail(msg_from,msg_to,msg.as_string())
			self._errors['status'] = '0000'
			self._errors['msg'] = 'success'
		except Exception as e:
			self._errors['status'] = '1001'
			self._errors['msg'] = 'fail,{}'.format(e)
		finally:
			s.quit()
		return self._errors
	def __str__(self):
		return str(self._errors)
	__repr__ = __str__


class Ut(object):
	def __init__(self):
		self.success = 0
		self.errors = list()
		self.status = 'pass'
		self.count_error = 0
	def assertEqual(self,data1,data2):
		try :
			assert data1==data2 ,"{}与{}不相等".format(data1,data2)
			self.success += 1
			return True
		except AssertionError as e:
			print(data1.__doc__)
			print(e)
	def assertTrue(self,data):
		try:
			assert data,"{}为真".format(data)
		except AssertionError as e:
			print(e)
		
def discover(dirs, starts):
	mod = __import__(dirs)
	mod_list = dir(mod)
	for i in mod_list:
		Func = getattr(mod, i)
		if type(Func).__name__ == 'classobj':
			# 找出类下面所有的函数
			method = [x for x in dir(Func) if x.startswith(starts)]
			# 循环执行类下面的函数
			for j in method:
				eval("Func().{}()".format(j))
		# 判断是否以传入参数starts开头的函数并执行
		elif type(Func).__name__ == 'function' and Func.__name__.startswith(starts):
			Func()
	
	


if __name__ == '__main__':
	ut = Ut()
	print(ut.assertEqual(1,1))