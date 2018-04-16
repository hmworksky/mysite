# -*- coding:utf-8 -*-
import sys
from urllib import unquote
from env_config import tools
from django.shortcuts import  render_to_response
reload(sys)
sys.setdefaultencoding("utf-8")
from django.http import JsonResponse,HttpResponse
import json
def get_branch(request):
    branch = tools.branch_list()
    return render_to_response('env_config/branch.html',{'branch_list':branch})