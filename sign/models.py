# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Login(models.Model):
    nick_name = models.CharField(max_length = 50, default = '0',  blank = True)
    username = models.CharField(max_length = 50, unique = True ,blank = True)
    password = models.CharField(max_length = 50,blank = True)
    def __unicode__(self):
	return self.username
	
class InterfaceInfo(models.Model):
    url_info = models.URLField(max_length = 200 ,unique = True ,null = True)
    status  =  models.IntegerField()
    return_value =  models.CharField(max_length = 2500)
    user = models.ForeignKey(Login)
    def __unicode__(self):
	return self.url_info
class HttpSend(models.Model):
    send_url = models.URLField(max_length = 200 ,unique = True ,null = True)
    status  =  models.IntegerField()
    data =  models.CharField(max_length = 2500)
    headers =  models.CharField(max_length = 2500)
    cookie =  models.CharField(max_length = 2500)
    send_type = models.CharField(max_length = 50)
    user = models.ForeignKey(Login)
    def __unicode__(self):
        return self.send_url
