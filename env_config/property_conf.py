from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Property
from public_tool.tools import logger

def property_create(request):
	username = request.session['username']
	if request.method == 'POST':
		model = request.POST.get('model')
		version = request.POST.get('version')
		from_people = request.POST.get('from_people')
		now_people = request.POST.get('now_people')
		try:
			Property.objects.create(model= model,version=version,from_people=from_people,now_people=now_people)
			return HttpResponseRedirect('/env/property/list/')
		except Exception,e:
			logger('property create fail num:17',e)
			return HttpResponseRedirect('/env/property/create/')
	return render_to_response('env_config/property_create.html',locals())


def property_list(request):
	username = request.session['username']
	try:
		property_info = Property.objects.filter().values("model","version","from_people","now_people","id")
		return render_to_response('env_config/property_list.html',locals())
	except Exception,e:
		logger('property_list num:28',e)
		return HttpResponseRedirect('/env/property/list/')
def property_edit(request,id):
	username = request.session['username']
	try:
		property_info = Property.objects.filter(id=id).values("model","version","from_people","now_people","id")
	except Exception,e:
		logger('property_edit fail',e)
		return HttpResponseRedirect('/env/property/list/')
	return render_to_response('env_config/property_edit.html',locals())


def property_update(request):
	id = request.POST.get("id")
	model = request.POST.get("model")
	version = request.POST.get("version")
	from_people = request.POST.get("from_people")
	now_people = request.POST.get("now_people")
	try:
		Property.objects.filter(id = id).update(model=model,version=version,from_people=from_people,now_people=now_people)
		return HttpResponseRedirect('/env/property/list/')
	except Exception,e:
		logger('property_update fail',e)
def property_delete(request,id):
	try:
		Property.objects.filter(id = id ).delete()
		return HttpResponseRedirect('/env/property/list/')
	except Exception,e:
		logger('property_update fail',e)