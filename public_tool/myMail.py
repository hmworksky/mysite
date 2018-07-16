# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 18:17
# @Author  : Huangmin
# @Site    : 
# @File    : myMail.py
# @Software: PyCharm
import os
from public_tool.tools import readconfig
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