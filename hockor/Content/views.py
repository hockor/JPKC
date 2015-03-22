#-*-coding:utf8-*-

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext,loader
from django.shortcuts import render
from django.utils import simplejson
from User.models import *

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
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def TestHd(request):
	template = loader.get_template('content/test.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))