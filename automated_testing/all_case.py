# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 20:10
# @Author  : Huangmin
# @Site    : 
# @File    : all_case.py
# @Software: PyCharm

import os
from automated_testing.auto_public.common import Sendmail,strf_time
import HTMLTestRunner
import unittest,requests
requests.urllib3.disable_warnings=False


def createsuitel(lists):
	testunit = unittest.TestSuite()
	all_case = unittest.defaultTestLoader.discover(lists,pattern='test*.py',top_level_dir=None)
	for case in all_case:
		testunit.addTests(case)
	return testunit

def run_all_test(list_dir = None):
	u'''this is zhushi'''
	runner = unittest.TextTestRunner()
	list_dir = 'test_case\\test_star'
	alltestnames = createsuitel(list_dir)
	print(alltestnames)
	t = runner.run(alltestnames)
	print(50*'=')
	print(type(t))


def imp():
	# CC = __import__('game.public.tools',fromlist=True)
	# func = 'random_img'
	# f = getattr(CC,func,None)
	# print(f())
	from public_tool.tools import  discover
	discover('test_star','test')


class PrizeGame1(unittest.TestCase):
	print('222')
	def __init__(self):
		print('create')
	
	def test_case01(self):
		s2 = self.name+1
		print(s2)


if __name__ == '__main__':
	# unittest.main()
	s = PrizeGame1()

	
