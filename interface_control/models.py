# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sign.models import  Login

# Create your models here.
class InterfaceInfo(models.Model):
    interface_name =models.CharField(max_length = 500)
    url_info = models.URLField(max_length = 200)
    request_type  =  models.IntegerField(default=0)
    return_value =  models.CharField(null = True,max_length = 2500)
    timeout = models.IntegerField(null = True ,default=0)
    user = models.ForeignKey(Login)

    class Meta:
        unique_together = ('url_info', 'user',)
    def __unicode__(self):
        return self.url_info