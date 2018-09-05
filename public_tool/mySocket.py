# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 20:26
# @Author  : Huangmin
# @Site    : 
# @File    : mySocket.py
# @Software: PyCharm

import socket,json
from websocket import create_connection,WebSocket


class NewWebSocket(WebSocket):
	# def __new__(cls, url):
	# 	sock_conn = create_connection(url, sockopt= ((socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),), class_=cls)
	# 	return sock_conn
	def recv_frame(self):
		frame = super().recv_frame()
		# print('frame on ',frame)
		return frame


class gameSock:
	def __init__(self,url):
		self.conn = create_connection(url,sockopt=((socket.IPPROTO_TCP,socket.TCP_NODELAY,1),),class_ = NewWebSocket)
	@property
	def get_ws_connect(self):
		return self.conn
	def close(self):
		self.conn.close()
	def send(self,msg,router = "router"):
		self.conn.send(router,msg)
	def result(self,msg):
		self.send(msg)
		return self.conn.recv()
	
if __name__ == '__main__':
	
	sock = gameSock('wss://tst-bubble2-dev-stg74.1768.com/primus/primus.js')
	# sock = gameSock('wss://nodejs-test.games.1768.com:8464')
	cmd = {"cmd":"poolAmount","params":{"jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyMDM4OTgxNTA3IiwiaWF0IjoxNTM2MTMyNjgzLCJleHAiOjE1MzYyMTkwODN9.FbiBaqYfTHKJy5np-0opcHMpSaLknYWpyWDQw8XwEVM"},"status":{"time":1536132692107}}
	result = sock.result(bytes(cmd))
	# sock.close
	#sock.send('2')
	print(result)
	print(type(result))
	#ms.close()
	# print(abs(3,4))