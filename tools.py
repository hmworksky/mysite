import MySQLdb
from ConfigParser import ConfigParser

def mysql_query(sql):
    host = readconfig("MYSQL_HOST".lower())
    username = readconfig("MYSQL_USERNAME".lower())
    passwd = readconfig("MYSQL_PASSWORD".lower())
    db = readconfig("MYSQL_DBNAME".lower())
    port = int(readconfig("MYSQL_PORT".lower()))
    try :
        conn = MySQLdb.connect(host = host ,user = username,passwd = passwd ,db=db, port = port ,charset = "utf8")
    except Exception , e :
        return e
    cursor = conn.cursor()
    try :
        data = []
        cursor.execute(sql)
        li = cursor.fetchall()
        for i in li :
            data.append(i)
        return data
    except Exception , e :
        return e
    finally :
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
