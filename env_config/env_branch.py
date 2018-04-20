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
    mem = tools.Memcached()
    branchs = eval(mem.getmem('branch'))
    #branchs = get_branch()#获取分支信息
    tools.logger('branch',type(branchs))

    return render_to_response('env_config/branch_list.html',locals())