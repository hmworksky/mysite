# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    nick_name = models.CharField(max_length = 50,blank = True)
    class Meta(AbstractUser.Meta):
	pass
class InterfaceInfo(models.Model):
    url_info = models.CharField(max_length = 500)
    commit_type =  models.CharField(max_length = 50)
    return_value =  models.CharField(max_length = 2500)
    def __str__(self):
	return self.url_info
