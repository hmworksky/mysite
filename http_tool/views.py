# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response


# Create your views here.
def http_get(request):
    return HttpResponse("ttt")
