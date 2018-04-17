# -*- coding:utf-8 -*-
import sys
from urllib import unquote
from tools import get_branch
reload(sys)
sys.setdefaultencoding("utf-8")
from public_tool import tools
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render_to_response
import json
def branch_list(request):
    username = request.session['username']
    branchs = get_branch()
    return render_to_response('env_config/branch_list.html',locals())