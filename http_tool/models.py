# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from sign.models import Login

# Create your models here.
class HttpSend(models.Model):
    send_url = models.URLField(max_length = 200 ,unique = True ,null = True)
    status  =  models.IntegerField(default=1)
    data =  models.CharField(default=None,null = True,max_length = 2500)
    headers =  models.CharField(default=None,null = True,max_length = 2500)
    cookie =  models.CharField(default=None,null = True,max_length = 2500)
    send_type = models.CharField(max_length = 50)
    thread_num = models.IntegerField(default=0)
    user = models.ForeignKey(Login)
    def __unicode__(self):
        return self.send_url