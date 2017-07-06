# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# Create your models here.
class InterfaceConf(models.Model):
    url = models.URLField(max_length = 200 ,unique = True ,null = True)
    status  =  models.IntegerField(default=1)
    remark =  models.CharField(max_length = 500)
    type =  models.CharField(max_length = 50)
    min =  models.IntegerField(default=0)
    max = models.IntegerField(default=0)
    is_null = models.CharField(default=0,max_length = 50)
    def __unicode__(self):
        return self.url

class CaseConf(models.Model):
    type = models.CharField(max_length=50)
    value = models.CharField(max_length = 500)
    interface = models.ForeignKey(InterfaceConf)
    def __unicode__(self):
        return self.url