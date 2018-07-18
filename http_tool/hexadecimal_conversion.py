# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 17:06
# @Author  : Huangmin
# @Site    : 
# @File    : hexadecimal_conversion.py
# @Software: PyCharm
from django.shortcuts import render_to_response



def hex_conversion(request):
	username = request.session['username']
	
	