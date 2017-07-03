# -*- coding:utf-8 -*-
from sign.models import Login
def getuserid(username):
    try :
        user_id = Login.objects.values("id").get(username = username)["id"]
    except Exception , e :
	    return False
    return user_id