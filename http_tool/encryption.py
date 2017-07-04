# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response,redirect
from django.http import  HttpResponse,Http404,HttpResponseRedirect
from public_tool import user,encryption



def encry_base64(request):
    username = request.session['username']
    user_id = user.getuserid(username)
    if request.method == 'POST' :
        base64_status = request.POST.get('base64')
        base64_decode = request.POST.get('base64_decode')
        url_decode = request.POST.get('url_decode')
        json_decode = request.POST.get('json_decode')
        encry_before = request.POST.get('encry_before')
        if base64_status == 'on' :
            encry_end = encryption.to_base64(encry_before)
        elif base64_decode == 'on':
            encry_end = encryption.from_base64(encry_before)
        elif url_decode == 'on' :
            encry_end = encryption.unquote(encry_before)
        else:
            return render_to_response('http_tool/encry_base64.html',{'username': username,'errormsg':'请选择一个转换类型'})
        return render_to_response('http_tool/encry_base64.html', {'username': username,'encry_end':encry_end})
    return render_to_response('http_tool/encry_base64.html')