# -*- coding:utf-8 -*-
from django.shortcuts import  render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from env_config.models import Property
from public_tool.tools import logger


def property_create(request):
	username = request.session['username']
	logger(dict(request.POST))
	if request.method == 'POST':
		model = request.POST.get('model')
		version = request.POST.get('version')
		from_people = request.POST.get('from_people')
		now_people = request.POST.get('now_people')
		try :
			Property.objects.create(model = model,version = version,from_people = from_people,now_people = now_people)
			logger('Property数据入库成功')
			return HttpResponseRedirect('/env/property/list/')
		except Exception,e:
			logger("property_create_fail:{0}".format(e))
	return render_to_response('env_config/property_create.html', locals())

def property_list(request):
	username = request.session['username']
	try :
		property_info = list(Property.objects.filter().values("model","version","from_people","now_people","id"))
		logger(property_info)
	except Exception,e:
		logger("property_list:{0}".format(e))
	return render_to_response('env_config/property_list.html', locals())
def property_edit(request,id):
	username = request.session['username']
	try :
		property_info = list(Property.objects.filter(id = id).values("model", "version", "from_people", "now_people", "id"))
		logger("edit_list:{0}".format(property_info))
	except Exception,e:
		logger("property_edit:{0}".format(e))
	return render_to_response('env_config/property_edit.html', locals())

def property_update(request):
	id = request.POST.get("id")
	now_people = request.POST.get("now_people")
	version = request.POST.get("version")
	try :
		Property.objects.filter(id = id).update(now_people = now_people,version = version)
		return HttpResponseRedirect('/env/property/list/')
	except Exception,e :
		logger("property_update:{0}".format(e))
		return HttpResponseRedirect('/env/property/list/{0}/'.format(id))
def property_delete(request,id):
	try :
		Property.objects.filter(id = id).delete()
	except Exception,e:
		logger("property_delete_exception:{0}".format(e))
	return property_list(request)


