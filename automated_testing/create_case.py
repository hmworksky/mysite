from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
# Create your views here.
from public_tool.tools import readconfig


def create_case(request):
	result = readconfig("string")
	return HttpResponse(result)