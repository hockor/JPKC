#-*-coding:utf8-*-

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext,loader
from django.shortcuts import render
from django.utils import simplejson
from User.models import *
from Content.models import *
from Content.serializers import AnnouncementSerializer,NewSerializer,ExamSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
	tests = Paper.objects.all()
	getscores = FinishExam.objects.filter(user_id = request.user.id)
	template = loader.get_template('content/test.html')
	context = RequestContext(request,{'tests':tests,'getscores':getscores})
	return HttpResponse(template.render(context))

def NewTestHd(request):
	template = loader.get_template('content/newtest.html')
	context = RequestContext(request,{})
	return HttpResponse(template.render(context))

def ComplateTestHd(request):
	template = loader.get_template('content/complatetest.html')
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

class AnnouncementList(APIView):
	def get(self,request,format=None):
		announcements = Announcement.objects.all()
		serializer = AnnouncementSerializer(announcements,many = True)
		return Response({'status':200,'data':serializer.data})

class NewList(APIView):
	def get(self,request,format=None):
		news = New.objects.all()
		serializer = NewSerializer(news,many = True)
		return Response({'status':200,'data':serializer.data})

class ExamDetail(APIView):
	def get(self,request,pk,format = None):
		exams = Exam.objects.filter(test_id = pk)
		serializer = ExamSerializer(exams,many = True)
		return Response({'status':200,'data':serializer.data})


def getAnswer(request):
	if request.method != 'POST' or not request.is_ajax():
		raise Http404
	id = request.POST.get("id")
	answer = request.POST.get("answer")
	try:
		obj = Exam.objects.get(id = id)
		if obj.answer == answer:
			return HttpResponse(simplejson.dumps({'score':obj.score}))
		else:
			return HttpResponse(simplejson.dumps({'score':0}))
	except:
		return HttpResponse(simplejson.dumps({'score':'error'}))

def getAllScore(request):
	if request.method != 'POST' or not request.is_ajax():
		raise Http404
	score = request.POST.get('score')
	paperid = request.POST.get('paperid')
	try:
		obj = FinishExam(user_id = request.user.id,paper_id = paperid,score = score)
		obj.save()
		return HttpResponse(simplejson.dumps({'score':score}))
	except:
		return HttpResponse(simplejson.dumps({'score':'error'}))

