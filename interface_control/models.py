# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sign.models import  Login

# Create your models here.
class InterfaceInfo(models.Model):
    url_info = models.URLField(max_length = 200 ,unique = True)
    status  =  models.IntegerField()
    return_value =  models.CharField(max_length = 2500)
    timeout = models.IntegerField(null = True ,default=0)
    user = models.ForeignKey(Login)
    def __unicode__(self):
	    return self.url_info