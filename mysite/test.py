#! /usr/bin/python
#-*- coding:utf-8 -*-
import MySQLdb
from ConfigParser import ConfigParser
li = []
sql = "select *  from person "
cf = ConfigParser()
cf.read("../config.conf")
conn_host = cf.get('MySQL_conn','MYSQL_HOST')
conn = MySQLdb.connect(host = conn_host ,user = "root",passwd = "test1324",port = 3306,db = "test",charset = "utf8")
cursor = conn.cursor()
cursor.execute(sql)
f = cursor.fetchall()
for i in f :
    li.append(i)
print i
conn.close()
