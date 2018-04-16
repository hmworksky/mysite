# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Property(models.Model):
    model = models.CharField(max_length = 200 ,unique = True ,null = True)
    version  =  models.CharField(default=None,null = True,max_length = 2500)
    from_people =  models.CharField(default=None,null = True,max_length = 2500)
    now_people =  models.CharField(default=None,null = True,max_length = 2500)
    def __unicode__(self):
        return self.model