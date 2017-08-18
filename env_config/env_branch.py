# -*- coding:utf-8 -*-
import sys
from urllib import unquote
reload(sys)
sys.setdefaultencoding("utf-8")
from public_tool import tools
from django.http import JsonResponse,HttpResponse
import json
def get_branch(request):
    dic = {}
    branch = tools.branch_data(5, 1)
    dic['name'] = branch[0]
    dic['value'] = branch[1]
    dic = json.dumps(dic)
    if request.method == 'POST' :
        return HttpResponse(dic,content_type='application/json; charset= utf-8')
    else :
        raise TypeError()