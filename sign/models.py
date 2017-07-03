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
    phone = models.IntegerField(null = True)
    def __unicode__(self):
	return self.username
	

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __unicode__(self):
        return self.name
