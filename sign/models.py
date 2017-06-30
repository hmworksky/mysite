# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Login(models.Model):
    nick_name = models.CharField(max_length = 50, default = '0',  blank = True)
    username = models.CharField(max_length = 50, unique = True ,blank = True)
    password = models.CharField(max_length = 50,blank = True)
    email = models.EmailField(max_length = 50 , null = True)
    phone = models.IntegerField(max_length = 50 , null = True)
    def __unicode__(self):
	return self.username
	
class InterfaceInfo(models.Model):
    url_info = models.URLField(max_length = 200 ,unique = True)
    status  =  models.IntegerField()
    return_value =  models.CharField(max_length = 2500)
    timeout = models.IntegerField(default=0)
    user = models.ForeignKey(Login)
    def __unicode__(self):
	return self.url_info,status,return_value,timeout
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
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __unicode__(self):
	return u'%s %s'%(name,age)
