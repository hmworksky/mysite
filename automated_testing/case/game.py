# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 17:53
# @Author  : Huangmin
# @Site    :
# @File    : game.py
# @Software: PyCharm



import json,os,requests
from lxml import etree
from bs4 import BeautifulSoup
from ConfigParser import ConfigParser
#去除warnning警告
requests.packages.urllib3.disable_warnings()

#此函数需要移到配置相关目录，url其实可以相对路径，但是比较懒
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

#此函数需要移到配置相关目录，url其实可以相对路径，但是比较懒
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



#将url中的参数转化为字典
def url2Dict(url):
	import urlparse
	query = urlparse.urlparse(url).query
	return dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])


#读取配置文件，根据key去查询文件中的值，返回为字符串
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

class GamePc(object):

	def __init__(self):
		#初始化获取登录session
		login = Login()
		self.session = login('game_pc')
		self.base_url = url_config('GAME_PC')
		self.result = {}

	def tingdou_recharge(self):
		#从配置读取URL相关信息
		game_pc_recharge_url = url_config('GAME_PC_TINGDOU_RECHARGE')
		#从文件中读取需要传递的参数
		game_name,datas = interface_config('game_pc_tingdou_recharge')
		#获取userId,待完成
		#userId=
		#遍历文件中的用例
		for data in datas:
			data['userId'] = 97992407#此处userid写死了，因为不知道游戏获取用户ID的接口

			#发送充值请求
			tingdou_recharge = self.session.post(url = game_pc_recharge_url,data = data)

			#获取充值结果
			tingdou_recharge_result = tingdou_recharge.content


	def daxiaowang(self):
		amount = 100#amount其实可以通过传参，这里只是演示
		_url = url_config('GAME_PC_DAXIAOWANG').format(amount = amount)

		#发送投注请求
		_bet = self.session.post(url = _url)
		print _bet.content
		#获取投注结果
		result = _bet.content

		#此处只是简单做print，后续需要处理则拿到值断言或者做统计都可以
		if json.loads(result)['statusCode'] == '0000':
			print '请求成功'
			if json.loads(result)['prizeAmount']>0:
				print "中奖啦，奖金{prize}".format(prize = json.loads(result)['prizeAmount'])
			else:
				print "可惜，未中奖"
	def caijin_recharge(self):
		pass


class GameWap(object):
	def __init__(self):
		login = Login()
		self.session = login('game_wap')
		self.base_url = url_config('GAME_WAP')

	#WAP卡当试一试，哈哈感觉中奖率还可以~~~~
	def kadang_bet(self,Multiple=None):
		import time
		msg = list()

		null = 0# 避免非平安流量渠道用户获取不到pa_liuliang,初始化一个值

		# 调用接口获取余额信息
		account_url = url_config('KADANG_GET_ACCOUNT')
		account = self.session.get(url=account_url, verify=False)
		if account.content:
			# 转化为字典
			account = eval(account.content)
		# 拼接发牌需要的form_参数
		form_data = {
			'amount': 100,  # 参数化
			'timeStamp': int(round(time.time() * 1000)),
			'userAccountBalance[wltPoint]': account.get('wltScore'),
			'userAccountBalance[tdianPoint]': account.get('TScore'),
			'userAccountBalance[tbPoint]': account.get('TCoin'),
			'userAccountBalance[tdouPoint]': account.get('tingdou'),
			'userAccountBalance[cjPoint]': account.get('caijin'),
			'userAccountBalance[cfPoint]': account.get('caifen'),
			'userAccountBalance[jkPoint]': account.get('jiankangjin'),
			'userAccountBalance[paPoint]': account.get('pa_liuliang')
		}
		stuck_two_url = url_config('KADANG_TWO_STUCK')  # 这些都可以读取配置
		# 发送发牌请求
		two_send = self.session.post(url=stuck_two_url, data = form_data,verify=False)
		#获取发牌结果
		two_result = two_send.content

		#判断结果是否为成功(0000)
		if json.loads(two_result)['statusCode'] == '0000':
			print '发牌成功,发牌信息{}'.format(two_result)
		else:
			print '发牌失败,失败信息{}'.format(two_result)

		# 第二次发牌
		stuck_three_url = url_config('KADANG_THREE_STUCK')
		three_result = self.session.post(url=stuck_three_url, verify=False)
		print three_result.content

		# 判断是否中奖
		prize = eval(three_result.content).get('prizeAmount')
		if prize > 0:
			print '中奖,奖金{prize}'.format(**locals())
		else:
			print '可惜没中奖'


class Memcached:
	def __init__(self):
		from pymemcache.client.base import Client
		self.client = Client(('127.0.0.1',11211))

	# 设置修改缓存key
	def setmem(self,key,value):
		return self.client.set(key,value)
	#获取缓存的值
	def getmem(self,key):
		return self.client.get(key)
	#删除缓存
	def delmem(self,key):
		return self.client.delete(key)


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




if __name__ == '__main__':
	wap = GameWap()
	wap.kadang_bet()