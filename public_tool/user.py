# -*- coding:utf-8 -*-
from sign.models import Login
from django.contrib.sessions.models import Session
def getuserid(username):
    try :
        user_id = Login.objects.values("id").get(username = username)["id"]
    except Exception as e :
	    return False
    return user_id


