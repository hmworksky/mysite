# -*- coding:utf-8 -*-
from sign.models import Login
from django.contrib.sessions.models import Session
def getuserid(username):
    try :
        user_id = Login.objects.values("id").get(username = username)["id"]
    except Exception , e :
	    return False
    return user_id

# def getusername(sessionid):
# 	try :
# 		sess = Session.objects.get(pk=sessionid).session_data

