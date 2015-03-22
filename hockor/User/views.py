#!/usr/bin/env python
#-*-coding:utf8-*-

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext,loader
from django.shortcuts import render
from django.utils import simplejson
from User.models import *

def Login(request):
	template = loader.get_template('user/login.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def RegisterHd(request):
	if request.method != 'POST' or not request.is_ajax():
		raise Http404
	username = request.POST.get("username")
	password = request.POST.get("password")
	email = request.POST.get("email")
	number = request.POST.get("number")
	professional = request.POST.get("professional")
	if User.objects.filter(username = username).count()>0:
		return HttpResponse(simplejson.dumps({'message':'error'}))
	if User.objects.filter(email = email).count()>0:
		return HttpResponse(simplejson.dumps({'message':'error'}))
	try:
		CreateUser(username,password,email,number,professional)
	except:
		return HttpResponse(simplejson.dumps({'message':'error'}))
	return HttpResponse(simplejson.dumps({'message':'ok'}))

def LoginHd(request):
	if request.method != 'POST' or not request.is_ajax():
		raise Http404
	username = request.POST.get("username")
	password = request.POST.get("password")
	user = authenticate(username = username,password = password)
	if not user:
		return HttpResponse(simplejson.dumps({'message':'error'}))
	login(request,user)
	return HttpResponse(simplejson.dumps({'message':'ok'}))

def LogoutHd(request):
	logout(request)
	return HttpResponseRedirect(reverse('hockor.views.logoHd'))



