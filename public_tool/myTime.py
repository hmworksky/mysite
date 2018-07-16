# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 13:59
# @Author  : Huangmin
# @Site    : 
# @File    : myTime.py
# @Software: PyCharm
from datetime import datetime
import time

class getTime(object):
	def __init__(self):
		
		
		self.datetime = datetime
	
	def getNow(self):
		'''
		获取当前年月日时分秒
		:return:
		'''
		now = self.datetime.now()
		thisTime = {'year': now.year, 'month': now.month, 'day': now.day, 'hour': now.hour, 'minute': now.minute, 'second': now.second}
		return thisTime
	
	def getStamp(self,decimal_flag=True):
		return time.time() if decimal_flag else time.time()*1000
	
	
	def getYear(self):
		return self.getNow['year']
	
	
	def getMonth(self):
		return self.getNow['month']
	
	
	def getDay(self):
		return self.getNow['day']
	
	
	def getMinute(self):
		return self.getNow['minute']
	
	
	def getSecond(self):
		return self.getNow['second']
	

if __name__ == '__main__':
	gt = getTime()
	year = gt.getYear
	print(year)