# -*- coding:utf-8 -*-
from sign.models import Login
from functools import wraps
from django.shortcuts import  render_to_response
import logging,time
from django.contrib.sessions.models import Session
def getuserid(username):
    try :
        user_id = Login.objects.values("id").get(username = username)["id"]
    except Exception , e :
	    return False
    return user_id


def verifyUser(username):
	def load(func):
		@wraps(func)
		def wraper(*args,**kwargs):
			try:
				user_id = Login.objects.values("id").get(username=username)["id"]
				return func(*args,**kwargs)
			except Exception, e:
				log = logging.getLogger('django')
				strtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				log.info("时间{}:{}".format(strtime,log))
				return render_to_response('login/login.html')
		return wraper
	return load


# def getusername(sessionid):
# 	try :
# 		sess = Session.objects.get(pk=sessionid).session_data
