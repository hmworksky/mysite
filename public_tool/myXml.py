# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 18:14
# @Author  : Huangmin
# @Site    : 
# @File    : myXml.py
# @Software: PyCharm



def read_xml(filename,xpath,property='text'):
	import lxml.etree as ET
	'''
	:param filename:文件路径
	:param xpath: 需要查找的xpath路径
	:param property: 需要查找的某个属性，查找内容则传递text
	:return:
	'''
	doc = ET.parse(filename)
	result = [x.get(property) for x in doc.xpath(xpath)]
	text_result =[x.text for x in doc.xpath(xpath)]
	return text_result if property=='text' else result




