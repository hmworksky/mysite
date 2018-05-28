# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sign.models import Login
import  django.utils.timezone as timezone


# Create your models here.
class ProjectInfo(models.Model):
	project_name = models.CharField('项目名称', max_length=200, unique=True)
	start_time = models.DateTimeField('开始时间', default=timezone.now)
	smock_time = models.DateTimeField('冒烟时间', default=timezone.now)
	online_time = models.DateTimeField('上线时间', default=timezone.now)
	add_date = models.DateTimeField('添加时间', default=timezone.now)
	participant = models.CharField('参与人员',default = None , null = True, max_length=200)
	project_manager = models.CharField('测试负责人',default = None ,null = True ,max_length=200)
	current_phase = models.CharField('当前阶段',default = '0' ,null = True ,max_length=200)
	user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)

	def __unicode__(self):
		return self.project_name
