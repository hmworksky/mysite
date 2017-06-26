# -*- coding:utf-8 -*-
import MySQLdb
from ConfigParser import ConfigParser

def mysql_operation(sql):
    host = readconfig("MYSQL_HOST".lower())
    username = readconfig("MYSQL_USERNAME".lower())
    passwd = readconfig("MYSQL_PASSWORD".lower())
    db = readconfig("MYSQL_DBNAME".lower())
    port = readconfig("MYSQL_PORT".lower())
    try:
        conn = MySQLdb.connect(host = '127.0.0.1',
	user = 'root',
	passwd = 'test1324' ,
	db = 'test1', 
	port = 3306 ,
	charset = "utf8")
    except Exception , e :
	#此处需要将获取到的异常添加日志
        return e
    cursor = conn.cursor()
    try:
        data = []
        cursor.execute(sql)
	conn.commit()
	if sql.startswith('select'):
            li = cursor.fetchall()
            for i in li :
                data.append(i)
            return data
	else :
	    return cursor.rowcount
    except Exception , e :
	#此处需要将获取到的异常添加日志
        return e
    finally:
        cursor.close()
        conn.close()

def readconfig(key):
    cf = ConfigParser()
    cf.read("config.conf")
    sections = cf.sections()
    for i in sections :
        kvs = dict(cf.items(i))
        if key in kvs.keys() :
            return  kvs[key]
        else :
            return False
#判断用户名是否注册
def signup_judge(username):
    sql = "select username from sign_login where username = '{uname}';".format(uname = username)
    result = mysql_operation(sql)
    #判断用户名是否在结果集中
    if len(result)> 0 :
	return False 
    else :
	return True
#注册
def signup(username,password):
    sql = "insert into sign_login (username,password) values('{uname}','{pwd}');".format(uname = username , pwd = password)
    result = mysql_operation(sql)
    return result #此处返回插入行数
#if __name__ == '__main__' :
#    p = signup_judge("test3")
#    print p
