#-*-coding:utf8-*-

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext,loader
from django.shortcuts import render
from django.utils import simplejson
from User.models import *
from Content.models import *

def SubjectHd(request):
	template = loader.get_template('content/subject.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def AboutHd(request):
	template = loader.get_template('content/about.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def FileHd(request):
	template = loader.get_template('content/file.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def MessageHd(request):
	template = loader.get_template('content/message.html')
	message = Message.objects.all()
	backmessage = BackMessage.objects.all()
	context = RequestContext(request,{'message':message,'backmessage':backmessage})
	return HttpResponse(template.render(context))

def TestHd(request):
	template = loader.get_template('content/test.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def stMsg(username,message):
	try:
		obj = Message(name = username,message = message)
		obj.save()
		return True
	except:
		return False

def getMessage(request):
	if request.method != 'post' or not request.is_ajax():
		raise Http404
	message = request.POST.get("message")
	if stMsg(request.user.username,message):
		return HttpResponse(simplejson.dumps({'message':'ok'}))
	else:
		return HttpResponse(simplejson.dumps({'message':'error'}))

def stBackMsg(msgid,contents):
	try:
		obj = BackMessage(msg_id = msgid,contents = contents)
		obj.save()
		return True
	except:
		return False

def backMessage(request):
	if request.method != 'POST' or not request.is_ajax():
		raise Http404
	msgid = request.POST.get("id")
	contents = request.POST.get("contents")
	if stBackMsg(msgid,contents):
		return HttpResponse(simplejson.dumps({'message':'ok'}))
	else:
		return HttpResponse(simplejson.dumps({'message':'error'}))
