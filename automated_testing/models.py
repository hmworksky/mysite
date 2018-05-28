# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from interface_control.models import  InterfaceInfo

# Create your models here.


# Create your models here.
class InterfaceConf(models.Model):
    url = models.URLField(max_length = 200 ,unique = True ,null = True)
    status = models.IntegerField(default=1)
    remark = models.CharField(max_length = 500)
    def __unicode__(self):
        return self.url

class InterfaceAttr(models.Model):
    type = models.CharField(default='string', max_length=50)
    min = models.CharField(default=0,null = True,max_length=50)
    max = models.CharField(default=0,null = True,max_length=50)
    field = models.CharField('字段名',max_length=50)
    is_null = models.CharField('非空标识',default=0, max_length=500)
    memo = models.CharField('描述',default=0,null=True,max_length=500)
    interface = models.ForeignKey(InterfaceInfo,on_delete=models.DO_NOTHING)
    def __unicode__(self):
        return self.type

    class Meta:
        unique_together = ('interface', 'field',)


class GameInfo(models.Model):
    name = models.CharField('游戏名', unique=True, max_length=50)
    memo = models.CharField('游戏描述',max_length=50)
    def __unicode__(self):
        return self.name

class CaseInfo(models.Model):
    case_name = models.CharField('用例名，即函数名', max_length=50)
    case_memo = models.CharField('用例描述',max_length=50)
    class_name = models.CharField('类名', max_length=50)
    class_memo = models.CharField( '类的描述',max_length=50)
    
    game = models.ForeignKey(GameInfo, on_delete=models.DO_NOTHING)
    
    def __unicode__(self):
        return self.case_name

    class Meta:
        unique_together = ('class_name', 'case_name',)