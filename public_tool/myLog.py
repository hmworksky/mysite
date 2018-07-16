# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 11:28
# @Author  : Huangmin
# @Site    : 
# @File    : myLog.py
# @Software: PyCharm
import logging,os,time


class Log(logging.Logger):
	def __init__(self,filename='default',name='default',time_flag='hour'):
		'''
		:param filename:生成的文件名
		:param name: 可设置标签
		:param time_flag: 创建日志文件以传入的time_flag来创建文件夹，默认是小时
		'''
		self.BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		self.logger = logging.getLogger(name)
		self.logger.setLevel(logging.DEBUG)
		# 建立一个filehandler来把日志记录在文件里，级别为debug以上
		self.filename = filename+'.log'
		self.filepath = os.path.join(self.create_path(is_exec=0),self.filename)
		self.create_path(time_flag)
		self.fh = logging.FileHandler(self.filepath,encoding='utf-8')
		self.fh.setLevel(logging.DEBUG)
		# 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
		self.ch = logging.StreamHandler()
		self.ch.setLevel(logging.ERROR)
		# 设置日志格式
		self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
		self.ch.setFormatter(self.formatter)
		self.fh.setFormatter(self.formatter)
		# 将相应的handler添加在logger对象中
		self.logger.addHandler(self.ch)
		self.logger.addHandler(self.fh)
		
	def create_path(self,flag='hour',is_exec=1):
		'''
		创建年月日时分文件夹
		:param flag:
		:param is_exec:是否创建文件夹,默认执行
		:return: None
		'''
		corresponding = {'year': -5, 'month': -4, 'day': -3, 'hour': -2, 'minute': -1}
		if flag not in corresponding.keys():
			flag = 'hour'
		#只获取到flag标识的时间
		log_path = self.get_log_path[:corresponding[flag]]
		tmp_path = os.path.join(self.BASEDIR,'log')
		for i in log_path:
			tmp_path = os.path.join(tmp_path,i)
			if is_exec==1:
				if not os.path.exists(tmp_path):#判断路径是否存在
					os.mkdir(tmp_path)
		return tmp_path
	
	@property
	def get_log_path(self):
		'''
		获取年月日时分秒列表
		:return:['2018','7','11','10','20','34']
		'''
		path = time.strftime("%Y/%m/%d/%H/%M/%S",time.localtime(time.time())).split('/')
		return path
	

	

	def info(self,msg):
		return self.logger.info(msg)
	
	def debug(self,msg):
		return self.logger.debug(msg)
	
	def error(self,msg):
		return self.logger.error(msg.encode('utf-8'))
		
	def warn(self, msg):
		return self.logger.warn(msg)
	
	def critical(self, msg):
		return self.logger.critical(msg)
	
	
if __name__ == '__main__':
	log = Log('name')
	log.warn('test')
	
	

