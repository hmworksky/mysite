# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 20:19
# @Author  : Huangmin
# @Site    : 
# @File    : constant_1.py
# @Software: PyCharm


def url_config(key):
	data = {
		'GAME_PC':'http://www.1768.com',
		'GAME_WAP':'http://m.1768.com',
		'KADANG_GET_ACCOUNT':'https://m.1768.com/?act=game_gamebase&st=queryUserAccount&Type=1&gameId=547',
		'KADANG_TWO_STUCK':'https://m.1768.com/?act=game_crazystuck&st=get_two',
		'KADANG_THREE_STUCK':'https://m.1768.com/?act=game_crazystuck&st=get_three',
		'GAME_PC_TINGDOU_RECHARGE':'http://www.1768.com/?act=gamepay&st=platform_direct_charge',
		'GAME_PC_DAXIAOWANG':'http://www.1768.com/?act=game_daxiaowang&st=play&amount={amount}&isAutoBet=0'
	}
	return data.get(key)

def interface_config(key):
	from public_tool.tools import read_excel
	#从excel表中获取需要传递的参数
	form_data = read_excel(r'../data/interface.xlsx',key)
	data = {
		#游戏PC挺豆充值URL
		'game_pc_tingdou_recharge': {'name':'游戏PC挺豆充值'},
		'game_wap_kadang_two_stuck':{'name':'卡当WAP第二次发牌'},
		'game_wap_kadang_three_stuck': {'name': '卡当WAP第三次发牌'}
	}
	return data.get(key),form_data